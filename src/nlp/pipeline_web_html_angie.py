"""
src/nlp/pipeline_web_html_angie.py

Phase 4 custom pipeline entrypoint that preserves the case example.
Run from the project root with:

  uv run python -m nlp.pipeline_web_html_angie
"""

import logging

from datafun_toolkit.logger import get_logger, log_header, log_path

from nlp.config_angie import (
    DATA_PATH,
    HTTP_REQUEST_HEADERS,
    PAGE_URL,
    PROCESSED_CSV_PATH,
    PROCESSED_PATH,
    RAW_HTML_PATH,
    RAW_PATH,
    ROOT_PATH,
    SENTENCE_LENGTHS_PNG_PATH,
    TOP_TOKENS_PNG_PATH,
    WORDCLOUD_PNG_PATH,
)
from nlp.stage01_extract import run_extract
from nlp.stage02_validate_angie import run_validate
from nlp.stage03_transform_angie import run_transform
from nlp.stage04_analyze_angie import run_analyze
from nlp.stage05_load import run_load

LOG: logging.Logger = get_logger("CI", level="DEBUG")


def main() -> None:
    log_header(LOG, "Module 6: EVTAL PIPELINE - WEB DOCUMENTS (HTML) - ANGIE")
    LOG.info("START PIPELINE")

    RAW_PATH.mkdir(parents=True, exist_ok=True)
    PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

    log_path(LOG, "ROOT_PATH", ROOT_PATH)
    log_path(LOG, "DATA_PATH", DATA_PATH)
    log_path(LOG, "RAW_PATH", RAW_PATH)
    log_path(LOG, "PROCESSED_PATH", PROCESSED_PATH)

    html_content = run_extract(
        source_url=PAGE_URL,
        http_request_headers=HTTP_REQUEST_HEADERS,
        raw_html_path=RAW_HTML_PATH,
        LOG=LOG,
    )

    validated_soup = run_validate(
        html_content=html_content,
        LOG=LOG,
    )

    df = run_transform(
        soup=validated_soup,
        LOG=LOG,
    )

    run_analyze(
        df=df,
        LOG=LOG,
        top_tokens_path=TOP_TOKENS_PNG_PATH,
        wordcloud_path=WORDCLOUD_PNG_PATH,
        sentence_lengths_path=SENTENCE_LENGTHS_PNG_PATH,
    )

    run_load(
        df=df,
        processed_csv_path=PROCESSED_CSV_PATH,
        LOG=LOG,
    )

    LOG.info("========================")
    LOG.info("Pipeline executed successfully!")
    LOG.info("========================")


if __name__ == "__main__":
    main()
