# P6 Custom Project & Engage -- Phases 4 & 5

This document summarizes the Phase 4 custom project work completed for the NLP pipeline project.
## Phase 4

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

## 5. Verification of Success
- The custom pipeline ran successfully after the modification.
- The processed CSV includes the new sentence-level columns.
- The new histogram image was created along with the other custom `angie_*` outputs.

## 6. Why Did You Choose This?
- I chose this modification because it makes a stronger impression than changing a simple setting.
- Adding sentence-level metrics changes what the pipeline computes, not just how it is configured.
- The new histogram also makes the project more engaging because it adds a fresh visual interpretation of the abstract.
- I wanted the modification to be meaningful while still being small enough to test and explain clearly.

## 7. What Did You Observe?
- The pipeline still ran successfully after the change.
- The processed CSV now includes `sentence_count`, `avg_sentence_length_words`, and `sentence_lengths`.
- The abstract contains 9 sentences with an average sentence length of 20.67 words.
- Sentence lengths range from 9 words to 38 words, showing that the writing is uneven in sentence size.
- The histogram adds a second perspective beyond token frequency and the word cloud.

## 8. What Insights Did You Gain?
- I learned that the abstract is information-dense and uses a mix of short and long sentences rather than a uniform writing pattern.
- The longest sentences carry much of the technical detail, while the shorter ones help summarize or transition ideas.
- Token analysis shows what words are emphasized, but sentence-length analysis shows how the ideas are structured.
- This reinforced the idea that useful NLP analysis can come from both vocabulary features and document-structure features.

---

This page provides a concise record of the custom Phase 4 project work and the evidence that the modified pipeline runs successfully.
