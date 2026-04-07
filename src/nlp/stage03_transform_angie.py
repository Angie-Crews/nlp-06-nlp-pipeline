"""
stage03_transform_angie.py

Custom transform stage copied from the case example.
Adds sentence-level features to support deeper analysis of abstract structure.
"""

import logging
import re
import string

from bs4 import BeautifulSoup, Tag
import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")


def _get_text(element: Tag | None, strip_prefix: str = "", separator: str = "") -> str:
    """Return element text or 'unknown' if element is None."""
    if element is None:
        return "unknown"
    text = element.get_text(separator=separator, strip=True)
    return text.replace(strip_prefix, "").strip() if strip_prefix else text


def _clean_text(text: str, nlp_model: spacy.language.Language) -> str:
    """Clean and normalize a text string for NLP analysis."""
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()

    doc = nlp_model(text)
    text = " ".join(
        [token.text for token in doc if not token.is_stop and not token.is_space]
    )

    return text


def _get_sentence_lengths(text: str, nlp_model: spacy.language.Language) -> list[int]:
    """Return sentence lengths in words from the raw abstract."""
    if text == "unknown":
        return []

    doc = nlp_model(text)
    sentence_lengths: list[int] = []
    for sentence in doc.sents:
        word_count = sum(1 for token in sentence if token.is_alpha)
        if word_count > 0:
            sentence_lengths.append(word_count)
    return sentence_lengths


def run_transform(
    soup: BeautifulSoup,
    LOG: logging.Logger,
) -> pd.DataFrame:
    """Transform HTML into a clean, analysis-ready DataFrame."""
    LOG.info("========================")
    LOG.info("STAGE 03: TRANSFORM starting...")
    LOG.info("========================")

    LOG.info("Extracting metadata from HTML")

    LOG.info("------------------------")
    LOG.info("Project specific: Extract title, authors, abstract")
    LOG.info("------------------------")

    title_tag: Tag | None = soup.find("h1", class_="title")
    title: str = _get_text(title_tag, strip_prefix="Title:")
    LOG.info(f"Extracted title: {title}")

    authors_tag: Tag | None = soup.find("div", class_="authors")
    author_tags_list: list[Tag] = authors_tag.find_all("a") if authors_tag else []
    authors: str = (
        ", ".join([tag.get_text(strip=True) for tag in author_tags_list])
        .replace("Authors:", "")
        .strip()
        if authors_tag
        else "unknown"
    )
    LOG.info(f"Extracted authors: {authors}")

    abstract_tag: Tag | None = soup.find("blockquote", class_="abstract")
    abstract_raw: str = _get_text(abstract_tag, strip_prefix="Abstract:")
    LOG.info(f"Extracted abstract: {abstract_raw[:100]}...")

    LOG.info("------------------------")
    LOG.info("Project specific: Extract subjects from subheader")
    LOG.info("------------------------")

    subheader: Tag | None = soup.find("div", class_="subheader")
    subjects: str = _get_text(subheader, strip_prefix="Subjects:")
    LOG.info(f"Extracted subjects: {subjects}")

    LOG.info("------------------------")
    LOG.info("Project specific: Extract submission date from dateline")
    LOG.info("------------------------")

    dateline: Tag | None = soup.find("div", class_="dateline")
    date_submitted_str: str = _get_text(dateline)
    LOG.info(f"Extracted submission date: {date_submitted_str}")

    LOG.info("------------------------")
    LOG.info("Project specific: Extract arxiv_id from canonical link")
    LOG.info("------------------------")

    canonical: Tag | None = soup.find("link", rel="canonical")

    if canonical is None:
        LOG.warning("Canonical link not found, setting arXiv ID to 'unknown'")
        arxiv_id: str = "unknown"
    else:
        href: str = str(canonical["href"])
        arxiv_id = href.split("/abs/")[-1]

    LOG.info(f"Extracted arxiv_id: {arxiv_id}")

    LOG.info("========================")
    LOG.info("PHASE 3.2: Clean and normalize text fields")
    LOG.info("========================")

    abstract_clean: str = (
        _clean_text(abstract_raw, nlp) if abstract_raw != "unknown" else "unknown"
    )

    LOG.info(f"  abstract (raw):   {abstract_raw[:120]}...")
    LOG.info(f"  abstract (clean): {abstract_clean[:120]}...")
    LOG.info(
        f"  characters removed: {len(abstract_raw) - len(abstract_clean)} "
        f"({100 * (1 - len(abstract_clean) / max(len(abstract_raw), 1)):.1f}%)"
    )

    LOG.info("========================")
    LOG.info("PHASE 3.3: Engineer derived features")
    LOG.info("========================")

    abstract_raw_word_count: int = (
        len(abstract_raw.split()) if abstract_raw != "unknown" else 0
    )
    LOG.info(f"  abstract_word_count: {abstract_raw_word_count}")

    author_count: int = (
        len([a.strip() for a in authors.split(",")]) if authors != "unknown" else 0
    )
    LOG.info(f"  author_count:        {author_count}")

    tokens: list[str] = abstract_clean.split() if abstract_clean != "unknown" else []
    token_count: int = len(tokens)
    LOG.info(f"  token_count:         {token_count}")

    unique_token_count: int = len(set(tokens))
    LOG.info(f"  unique_token_count:  {unique_token_count}")

    type_token_ratio: float = (
        round(unique_token_count / token_count, 4) if token_count > 0 else 0.0
    )
    LOG.info(f"  type_token_ratio:    {type_token_ratio}")

    sentence_lengths: list[int] = _get_sentence_lengths(abstract_raw, nlp)
    sentence_count: int = len(sentence_lengths)
    average_sentence_length: float = (
        round(sum(sentence_lengths) / sentence_count, 2) if sentence_count > 0 else 0.0
    )
    LOG.info(f"  sentence_count:      {sentence_count}")
    LOG.info(f"  avg_sentence_words:  {average_sentence_length}")
    LOG.info(f"  sentence_lengths:    {sentence_lengths}")
    LOG.info(f"  top 10 tokens:       {tokens[:10]}")

    LOG.info("========================")
    LOG.info("PHASE 3.4: Build record and create DataFrame")
    LOG.info("========================")

    record = {
        "arxiv_id": arxiv_id,
        "title": title,
        "authors": authors,
        "subjects": subjects,
        "submitted": date_submitted_str,
        "abstract_raw": abstract_raw,
        "abstract_clean": abstract_clean,
        "tokens": " ".join(tokens),
        "abstract_word_count": abstract_raw_word_count,
        "token_count": token_count,
        "unique_token_count": unique_token_count,
        "type_token_ratio": type_token_ratio,
        "author_count": author_count,
        "sentence_count": sentence_count,
        "avg_sentence_length_words": average_sentence_length,
        "sentence_lengths": ";".join(str(length) for length in sentence_lengths),
    }

    df = pd.DataFrame([record])

    LOG.info(f"Created DataFrame with {len(df)} row and {len(df.columns)} columns")
    LOG.info(f"Columns: {list(df.columns)}")
    LOG.info(
        f"  DF preview:\n{df[['arxiv_id', 'title', 'token_count', 'sentence_count', 'avg_sentence_length_words']].head()}"
    )

    LOG.info("Sink: Pandas DataFrame created")
    LOG.info("Transformation complete.")
    return df
