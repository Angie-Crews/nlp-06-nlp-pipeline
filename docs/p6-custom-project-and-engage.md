# P6 Custom Project & Engage -- Phases 4 & 5

This document summarizes the custom project work completed for Phases 4 and 5 of the NLP pipeline project.

## Summary Table: Evolution and Application of Skills

| Aspect                | Original Pipeline (Example)                                                                 | Technical Modification (Phase 4)                                                                                 | Application to New Problem (Phase 5)                                                                 |
|-----------------------|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| **Input**             | arXiv abstract (original example paper)                                                    | No change to input for Phase 4                                                                                   | New arXiv abstract: *Attention Is All You Need*                                                     |
| **Pipeline Structure**| Extraction, validation, transformation, analysis, load (EVTAL)                             | Same structure, but with custom `angie` pipeline files                                                           | Reused custom `angie` pipeline for new paper                                                        |
| **Key Features**      | Tokenization, word frequency, word cloud                                                   | Added sentence-level metrics: `sentence_count`, `avg_sentence_length_words`, `sentence_lengths`                  | Same sentence-level metrics applied to new paper                                                    |
| **Visualizations**    | Top tokens bar chart, word cloud                                                          | Added histogram of sentence lengths                                                                              | All three visualizations for new paper                                                              |
| **Outputs**           | `*_processed.csv`, `*_top_tokens.png`, `*_wordcloud.png`                                  | Added `angie_sentence_lengths.png` and new columns in CSV                                                        | New outputs: `angie_phase5_*` files for all artifacts                                              |
| **Technical Skills**  | Basic pipeline usage, pandas, matplotlib                                                   | Custom pipeline creation, feature engineering, new visualization, config management                              | Workflow reuse, config adaptation, analysis of new domain                                           |
| **Insights**          | Token analysis of original abstract                                                        | Discovered sentence structure patterns, richer document analysis                                                  | Compared structure/content of two different abstracts, validated pipeline generalizability           |

This table summarizes how the project evolved from the original example, through technical modification, to successful application on a new problem.
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

This section provides a concise record of the custom Phase 4 project work and the evidence that the modified pipeline ran successfully.

## Phase 5

## 1. New Problem Chosen
- Applied the custom `angie` pipeline to a different arXiv paper instead of the original Phase 4 paper.
- New source paper:
  - *Attention Is All You Need*
  - `https://arxiv.org/abs/1706.03762`
- This satisfied the Phase 5 suggestion to apply the same workflow to a new arXiv abstract page.

## 2. Files Used for the Custom Application
- Reused the custom `angie` pipeline created in Phase 4.
- Continued using:
  - `src/nlp/config_angie.py`
  - `src/nlp/stage02_validate_angie.py`
  - `src/nlp/stage03_transform_angie.py`
  - `src/nlp/stage04_analyze_angie.py`
  - `src/nlp/pipeline_web_html_angie.py`
- Updated the custom config so Phase 5 writes to separate `angie_phase5_*` outputs.

## 3. Did You Use Pandas or Polars?
- Used `pandas`.

## 4. Why Did You Make That Choice?
- I chose `pandas` because the starter project already used it.
- This kept the custom work consistent with the original pipeline.
- It allowed me to focus on applying the workflow to a new problem instead of rewriting the data-processing logic.

## 5. Describe Your Custom Application
- I changed the input text by targeting a different arXiv paper.
- The pipeline extracted, validated, transformed, analyzed, and loaded data for the new abstract using the same EVTAL process.
- The code changes centered on updating the custom configuration and writing separate Phase 5 artifacts so earlier custom outputs were preserved.
- The sentence-level metrics from Phase 4 were retained, so the new paper could be analyzed with both token-level and sentence-level features.

## 6. What Is Interesting About Your Custom Application?
- It shows that the same pipeline can analyze a very different paper without changing the overall architecture.
- The new paper is a foundational NLP paper, so the output naturally emphasizes terms like `attention`, `translation`, `BLEU`, `transformer`, and `training`.
- This makes the custom application more meaningful because the output aligns strongly with the topic of the selected paper.

## 7. What Did You Observe?
- The custom pipeline ran successfully on the new paper.
- New Phase 5 artifacts were created:
  - `data/raw/angie_phase5_raw.html`
  - `data/processed/angie_phase5_processed.csv`
  - `data/processed/angie_phase5_top_tokens.png`
  - `data/processed/angie_phase5_wordcloud.png`
  - `data/processed/angie_phase5_sentence_lengths.png`
- The processed CSV reported:
  - raw abstract words: `166`
  - cleaned tokens: `99`
  - unique tokens: `79`
  - type-token ratio: `0.798`
  - author count: `8`
  - sentence count: `7`
  - average sentence length: `24.14`
  - sentence lengths: `19, 14, 20, 25, 23, 43, 25`

## 8. What Insights Did You Gain?
- I learned that this abstract is dense and technical, with multiple medium-length sentences and one especially long sentence carrying a large amount of detail.
- Token analysis highlights the paper's central ideas: models, attention, translation, BLEU scores, and training performance.
- Sentence-length analysis adds a structural perspective that token counts alone do not provide.
- This reinforced that NLP analysis can be strengthened by combining vocabulary-based metrics with document-structure features.

## 9. Brief Summary of Results
- The custom Angie pipeline successfully applied the EVTAL workflow to a new arXiv paper.
- The results produced a clean CSV and three visual outputs for Phase 5.
- Together, the token chart, word cloud, and sentence-length histogram provided a clearer picture of both the content and structure of the abstract.

---

This page now provides a concise record of the custom project work completed for both Phase 4 and Phase 5.
