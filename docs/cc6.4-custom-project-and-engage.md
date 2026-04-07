# cc6.4 Custom Project & Engage

This document summarizes the Phase 4 custom project work completed for the NLP pipeline project.

## 1. Goal of the Modification
- Created a custom version of the example pipeline while keeping the original `_case` files unchanged.
- Extended the project with a meaningful technical modification rather than a simple configuration tweak.
- Focused the modification on sentence-level analysis so the project produces new metrics and a new visualization.

## 2. Custom Project Files
- Copied the example pipeline files into custom `angie` versions under `src/nlp/`.
- Added a custom pipeline entrypoint:
  - `uv run python -m nlp.pipeline_web_html_angie`
- Preserved the original example pipeline and outputs for comparison.

## 3. Technical Modification Made
- Added new derived features in the Transform stage:
  - `sentence_count`
  - `avg_sentence_length_words`
  - `sentence_lengths`
- Added a new visualization in the Analyze stage:
  - `data/processed/angie_sentence_lengths.png`
- Kept outputs separate from the example by writing to custom `angie_*` files.

## 4. Outputs Produced
- Verified creation of custom artifacts:
  - `data/raw/angie_raw.html`
  - `data/processed/angie_processed.csv`
  - `data/processed/angie_top_tokens.png`
  - `data/processed/angie_wordcloud.png`
  - `data/processed/angie_sentence_lengths.png`

## 5. What Was Observed
- The custom pipeline ran successfully after the modification.
- The processed CSV now includes sentence-level columns in addition to the original token-based metrics.
- The sentence-length histogram shows that the abstract varies noticeably in sentence length, ranging from short sentences to much denser ones.
- This adds a second perspective to the analysis beyond token frequency and the word cloud.

## 6. Why This Matters
- The modification demonstrates ownership of the project by changing what the pipeline computes and produces.
- The new features make the analysis more interpretable by showing how information is distributed across sentences.
- The separate `angie` pipeline preserves the working example while documenting an original extension of the project.

## 7. Engagement With the Results
- Reviewed the new CSV output to confirm the added columns were populated correctly.
- Interpreted the histogram to understand the structure of the abstract, not just its vocabulary.
- Used the results to explain how the abstract mixes short summary statements with longer, information-dense sentences.

---

This page provides a concise record of the custom Phase 4 project work and the evidence that the modified pipeline runs successfully.
