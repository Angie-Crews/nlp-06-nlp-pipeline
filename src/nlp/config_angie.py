"""
src/nlp/config_angie.py - Phase 4 Configuration

Custom configuration copied from the case example.
This version writes outputs to angie_* files so the example outputs remain intact.
"""

from pathlib import Path

# ============================================================
# API CONFIGURATION
# ============================================================

PAGE_URL: str = "https://arxiv.org/abs/2602.20021"

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

RAW_HTML_PATH: Path = RAW_PATH / "angie_raw.html"
PROCESSED_CSV_PATH: Path = PROCESSED_PATH / "angie_processed.csv"
