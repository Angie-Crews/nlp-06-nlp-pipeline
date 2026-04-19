# NLP Portfolio Presentation

This portfolio summarizes my work across the Web Mining and Applied NLP sequence, with concrete evidence from my repositories and outputs.

## 1. NLP Techniques Implemented

I implemented and combined multiple NLP techniques in a repeatable pipeline:

- Tokenization and text normalization using spaCy in [src/nlp/stage03_transform_angie.py](../src/nlp/stage03_transform_angie.py).
- Text cleaning (lowercasing, punctuation removal, whitespace normalization, stopword removal) in [src/nlp/stage03_transform_angie.py](../src/nlp/stage03_transform_angie.py).
- Frequency analysis and ranking using Counter in [src/nlp/stage04_analyze_angie.py](../src/nlp/stage04_analyze_angie.py).
- N-gram related exploration in earlier course projects (see representative projects below).
- Web scraping/content extraction from HTML using requests and BeautifulSoup in [src/nlp/stage01_extract.py](../src/nlp/stage01_extract.py) and [src/nlp/stage03_transform_angie.py](../src/nlp/stage03_transform_angie.py).
- API-based text data handling (JSON parsing and analysis) in my module 4 API text project: <https://github.com/Angie-Crews/nlp-04-api-text-data>.

Evidence:

- Processed output file: [data/processed/angie_phase5_processed.csv](../data/processed/angie_phase5_processed.csv).
- Visual outputs: [data/processed/angie_phase5_top_tokens.png](../data/processed/angie_phase5_top_tokens.png), [data/processed/angie_phase5_wordcloud.png](../data/processed/angie_phase5_wordcloud.png), [data/processed/angie_phase5_sentence_lengths.png](../data/processed/angie_phase5_sentence_lengths.png).

## 2. Systems and Data Sources

I worked with multiple source types and structures:

- HTML web documents from arXiv abstracts (module 5 and module 6).
- JSON/API text data (module 4 project).
- Plain text fields extracted into tabular records for downstream analysis.

Current module 6 source analyzed:

- URL configured in [src/nlp/config_angie.py](../src/nlp/config_angie.py): <https://arxiv.org/abs/1706.03762>.

How I handled messy or variable input:

- Validation checks for required HTML elements (title, authors, abstract, subjects, dateline) in [src/nlp/stage02_validate_angie.py](../src/nlp/stage02_validate_angie.py).
- Defensive extraction with fallbacks such as unknown values in [src/nlp/stage03_transform_angie.py](../src/nlp/stage03_transform_angie.py).
- Canonical link parsing and robust handling when metadata is missing.

## 3. Pipeline Structure (EVTL)

I implemented and ran a structured EVTL pipeline:

- Extract: Retrieve HTML from a configured source URL and persist raw HTML in [src/nlp/stage01_extract.py](../src/nlp/stage01_extract.py).
- Validate: Parse and verify required structure before transformation in [src/nlp/stage02_validate_angie.py](../src/nlp/stage02_validate_angie.py).
- Transform: Clean text, tokenize, and engineer features in [src/nlp/stage03_transform_angie.py](../src/nlp/stage03_transform_angie.py).
- Analyze: Compute token frequencies and generate visuals in [src/nlp/stage04_analyze_angie.py](../src/nlp/stage04_analyze_angie.py).
- Load: Write final tabular output to CSV in [src/nlp/stage05_load.py](../src/nlp/stage05_load.py).

Pipeline orchestration and successful execution are shown in [src/nlp/pipeline_web_html_angie.py](../src/nlp/pipeline_web_html_angie.py) and documented in [README.md](../README.md).

## 4. Signals and Analysis Methods

I computed signals that quantify both vocabulary and writing structure:

- Word frequency via top token counts.
- Lexical diversity via type-token ratio.
- Sentence-level structure via sentence_count, avg_sentence_length_words, and sentence_lengths.
- Author and metadata signals (author_count, arxiv_id, subjects, submitted date).

Methods and outputs:

- Frequency ranking and top-N plotting in [src/nlp/stage04_analyze_angie.py](../src/nlp/stage04_analyze_angie.py).
- Engineered features in [src/nlp/stage03_transform_angie.py](../src/nlp/stage03_transform_angie.py).
- Stored signals in [data/processed/angie_phase5_processed.csv](../data/processed/angie_phase5_processed.csv).

## 5. Insights

My analysis of Attention Is All You Need revealed several useful patterns:

- Raw abstract words: 166
- Cleaned tokens: 99
- Unique tokens: 79
- Type-token ratio: 0.798
- Sentence count: 7
- Average sentence length: 24.14 words

Sentence length distribution showed one especially long sentence (43 words), indicating dense technical packaging of ideas. Token-level signals emphasized terms related to attention, translation, models, BLEU, and training. Combining token and sentence metrics made the results more meaningful than frequency alone.

Evidence source: [docs/p6-custom-project-and-engage.md](p6-custom-project-and-engage.md) and [data/processed/angie_phase5_processed.csv](../data/processed/angie_phase5_processed.csv).

## 6. Representative Work

1. Module 6 NLP Pipeline (EVTL + custom sentence features)

   Link: <https://github.com/Angie-Crews/nlp-06-nlp-pipeline>

   This project is representative because it shows end-to-end engineering of an EVTL workflow, from web extraction through analysis and loading. It also includes my technical customization (sentence-level features and histogram), not just starter code execution.

2. Module 5 Web Documents

   Link: <https://github.com/Angie-Crews/nlp-05-web-documents>

   This project demonstrates my baseline HTML extraction and transformation workflow and serves as the foundation for module 6 enhancements. It shows how I built reliability before adding deeper NLP features.

3. Module 4 API Text Data

   Link: <https://github.com/Angie-Crews/nlp-04-api-text-data>

   This project is representative because it demonstrates my ability to work with API/JSON data sources, normalize text fields, and analyze outputs from non-HTML systems. It complements the HTML pipeline work by showing broader data-source fluency.

## 7. Skills

I can:

- Build repeatable Python data pipelines with clear stages and outputs.
- Extract and validate text data from HTML and API/JSON sources.
- Clean and normalize messy, inconsistent text data for analysis.
- Engineer NLP-derived features and compare lexical/structural signals.
- Produce analysis artifacts (CSV, charts, word clouds) and interpret findings.
- Communicate technical work professionally in Markdown documentation with evidence and links.

## Portfolio Links

- Module 6 repository: <https://github.com/Angie-Crews/nlp-06-nlp-pipeline>
- Module 6 hosted docs (portfolio page): <https://angie-crews.github.io/nlp-06-nlp-pipeline/nlp-portfolio/>
