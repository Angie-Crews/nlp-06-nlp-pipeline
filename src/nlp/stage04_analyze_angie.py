"""
stage04_analyze_angie.py

Custom analyze stage copied from the case example.
Adds a sentence-length histogram to complement the new derived metrics.
"""

from collections import Counter
import logging
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud


def _plot_top_tokens(
    tokens: list[str],
    top_n: int,
    output_path: Path,
    title: str,
    LOG: logging.Logger,
) -> None:
    """Plot a horizontal bar chart of the top N most frequent tokens."""
    counter = Counter(tokens)
    most_common = counter.most_common(top_n)

    if not most_common:
        LOG.warning("No tokens to plot.")
        return

    words, counts = zip(*most_common, strict=False)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(list(reversed(words)), list(reversed(counts)), color="steelblue")
    ax.set_xlabel("Frequency")
    ax.set_title(title)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()

    LOG.info(f"  Saved bar chart to {output_path}")


def _plot_wordcloud(
    text: str,
    output_path: Path,
    title: str,
    LOG: logging.Logger,
) -> None:
    """Generate and save a word cloud from cleaned text."""
    if not text or text == "unknown":
        LOG.warning("No text available for word cloud.")
        return

    wc = WordCloud(
        width=800,
        height=400,
        background_color="white",
        max_words=80,
        colormap="viridis",
    ).generate(text)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    ax.set_title(title, fontsize=14)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()

    LOG.info(f"  Saved word cloud to {output_path}")


def _plot_sentence_length_histogram(
    sentence_lengths: list[int],
    output_path: Path,
    title: str,
    LOG: logging.Logger,
) -> None:
    """Plot sentence lengths to show how dense the abstract is by sentence."""
    if not sentence_lengths:
        LOG.warning("No sentence lengths to plot.")
        return

    fig, ax = plt.subplots(figsize=(10, 6))
    bins = range(min(sentence_lengths), max(sentence_lengths) + 2)
    ax.hist(
        sentence_lengths, bins=bins, color="darkorange", edgecolor="black", align="left"
    )
    ax.set_xlabel("Words per sentence")
    ax.set_ylabel("Sentence count")
    ax.set_title(title)
    ax.set_xticks(list(range(min(sentence_lengths), max(sentence_lengths) + 1)))
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()

    LOG.info(f"  Saved sentence-length histogram to {output_path}")


def run_analyze(
    df: pd.DataFrame,
    LOG: logging.Logger,
    output_dir: Path = Path("data/processed"),
    top_tokens_path: Path | None = None,
    wordcloud_path: Path | None = None,
    sentence_lengths_path: Path | None = None,
    top_n: int = 20,
) -> None:
    """Analyze the transformed DataFrame and produce visualizations."""
    LOG.info("========================")
    LOG.info("STAGE 04: ANALYZE starting...")
    LOG.info("========================")

    output_dir.mkdir(parents=True, exist_ok=True)

    row = df.iloc[0]

    title: str = str(row.get("title", "unknown"))
    tokens_str: str = str(row.get("tokens", ""))
    token_count: int = int(row.get("token_count", 0))
    unique_token_count: int = int(row.get("unique_token_count", 0))
    type_token_ratio: float = float(row.get("type_token_ratio", 0.0))
    abstract_word_count: int = int(row.get("abstract_word_count", 0))
    author_count: int = int(row.get("author_count", 0))
    sentence_count: int = int(row.get("sentence_count", 0))
    avg_sentence_length_words: float = float(row.get("avg_sentence_length_words", 0.0))
    sentence_lengths_raw: str = str(row.get("sentence_lengths", ""))

    tokens: list[str] = tokens_str.split() if tokens_str else []
    sentence_lengths: list[int] = [
        int(value) for value in sentence_lengths_raw.split(";") if value.strip()
    ]

    LOG.info(f"  Paper: {title}")
    LOG.info(f"  Abstract word count (raw):    {abstract_word_count}")
    LOG.info(f"  Token count (clean):          {token_count}")
    LOG.info(f"  Unique token count:           {unique_token_count}")
    LOG.info(f"  Type-token ratio:             {type_token_ratio}")
    LOG.info(f"  Author count:                 {author_count}")
    LOG.info(f"  Sentence count:               {sentence_count}")
    LOG.info(f"  Avg sentence length:          {avg_sentence_length_words}")

    top_tokens_output = top_tokens_path or output_dir / "angie_top_tokens.png"
    wordcloud_output = wordcloud_path or output_dir / "angie_wordcloud.png"
    sentence_lengths_output = (
        sentence_lengths_path or output_dir / "angie_sentence_lengths.png"
    )

    _plot_top_tokens(
        tokens=tokens,
        top_n=top_n,
        output_path=top_tokens_output,
        title=f"Top {top_n} Tokens: {title}",
        LOG=LOG,
    )

    _plot_wordcloud(
        text=tokens_str,
        output_path=wordcloud_output,
        title=f"Word Cloud: {title}",
        LOG=LOG,
    )

    _plot_sentence_length_histogram(
        sentence_lengths=sentence_lengths,
        output_path=sentence_lengths_output,
        title=f"Sentence Lengths: {title}",
        LOG=LOG,
    )

    counter = Counter(tokens)
    top_tokens = counter.most_common(top_n)

    LOG.info(f"  Top {top_n} tokens by frequency:")
    for rank, (word, count) in enumerate(top_tokens, start=1):
        LOG.info(f"    {rank:>3}. {word:<30} {count}")

    LOG.info(f"  Sentence lengths (words):     {sentence_lengths}")
    LOG.info("Sink: visualizations saved to data/processed/")
    LOG.info("Analysis complete.")
