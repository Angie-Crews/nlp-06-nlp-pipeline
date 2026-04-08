"""
src/nlp/config_angie.py - Custom Configuration

Custom configuration copied from the case example.
This version now targets a second arXiv paper for Phase 5 and writes
separate phase-5 outputs so earlier custom artifacts remain intact.
"""

from pathlib import Path

# ============================================================
# API CONFIGURATION
# ============================================================

PAGE_URL: str = "https://arxiv.org/abs/1706.03762"

HTTP_REQUEST_HEADERS: dict = {
    "User-Agent": "Mozilla/5.0 (educational-use; web-mining-course)"
}

# ============================================================
# PATH CONFIGURATION
# ============================================================

ROOT_PATH: Path = Path.cwd()
DATA_PATH: Path = ROOT_PATH / "data"
RAW_PATH: Path = DATA_PATH / "raw"
PROCESSED_PATH: Path = DATA_PATH / "processed"

RAW_HTML_PATH: Path = RAW_PATH / "angie_phase5_raw.html"
PROCESSED_CSV_PATH: Path = PROCESSED_PATH / "angie_phase5_processed.csv"
TOP_TOKENS_PNG_PATH: Path = PROCESSED_PATH / "angie_phase5_top_tokens.png"
WORDCLOUD_PNG_PATH: Path = PROCESSED_PATH / "angie_phase5_wordcloud.png"
SENTENCE_LENGTHS_PNG_PATH: Path = PROCESSED_PATH / "angie_phase5_sentence_lengths.png"
