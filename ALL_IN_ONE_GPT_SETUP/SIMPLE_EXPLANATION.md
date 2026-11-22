# Simple Guide: DepEd MATATAG All-in-One GPT Setup & Knowledge Files

This document provides a clear, specific breakdown in basic English of what the instructions and each knowledge file contain, and what their exact purpose is.

---

## 🎯 Big Picture: What is this folder for?

This folder contains everything needed to set up a single **Custom ChatGPT** that generates publication-grade, 45-to-75 page quarterly textbooks for the Philippine **DepEd MATATAG Curriculum** (Grades 1 to 10) across all subjects, and compiles them directly into formatted Microsoft Word (`.docx`) files.

---

## 📜 1. The Main Instruction File (`INSTRUCTIONS_FOR_CHATGPT.txt`)

This is the master prompt pasted into ChatGPT's **Instructions** box. It acts as the "brain" and rulebook.

### Specifically What It Contains:
1. **The 10 Non-Negotiable Core Rules:**
   * **1. Publication Prose:** Written in 100% formal academic language with zero rough draft tags (banning tags like "Visual Prompt").
   * **2. Verbatim Law (No Summarizing):** Transfer 100% of all generated chat text word-for-word into the Word document. Never condense or omit items.
   * **3. 45–75 Counted Pages Target:** 
     * Only counts from Lesson 1 to Answer Keys (Cover, Preface, TOC, Synthesis, and Glossary are uncounted).
     * Word budget: 18,000–24,000 words total (4,000–4,500 words/lesson for 3-lesson units; 2,200–2,600 words/lesson for 5–7 lesson STEM quarters).
     * Typography is locked: 10.5 pt font, 1.15 line spacing, 0.8-inch margins (never shrink fonts to fit).
   * **4. Continuous Flow:** Natural flow without internal page breaks. Breaks are only allowed between major structural milestones.
   * **5. Zero Branding:** No "DepEd", "MATATAG", or commercial logos in prompts, headers, or footers.
   * **6. Prompts Only (No Fake AI Images):** Output text prompt boxes for the author to generate later. Exactly 3 image boxes per lesson + 1 cover prompt.
   * **7. Blue Header Banners:** Solid Navy (`#1B365D`) banners for H1 headers, soft blue (`#EBF3FA`) with navy left borders for H2 subtopics.
   * **8. Structured Table Keys:** All quiz answers must be in clean table grids with balanced A–D answers (~25% each; max 2 consecutive same letters).
   * **9. Factual Integrity & DOK:** Zero fake dates, fake laws, or fake science. Matches cognitive depth to Grade Level (DOK 1–4).
   * **10. STEM Standards:** Real math equations in `$…$` or `$$…$$`, formula definition cards, and 5-step worked examples.

2. **The Turn-by-Turn Delivery Protocol:**
   * **Turn 0 (Handshake):** ChatGPT asks for the Subject, Grade, Quarter, and Lesson Range.
   * **Turn 1 (Front Matter):** Generates Page 1 Cover, Page 2 Preface (350+ words), and Page 3 Table of Contents.
   * **Lesson Turns:** Generates **one lesson per turn** following a strict 10-section blueprint.
   * **Back Matter Turn:** Generates the 50-point unit assessment, culminating performance task (4x4 rubric), unit synthesis, glossary, structured answer tables, and QA stamp.
   * **Compilation Turn:** Runs the Python compiler (`docx_builder.py`) to produce the final `.docx` book.

3. **The 10-Section Lesson Blueprint:**
   * **Sec 1:** H1 Banner, Competency Codes, 3 Essential Questions, Boxed YouTube Module, and 150–250 word Background.
   * **Sec 2:** Subtopic 1 (Theory), Image Box 1, Concept Matrix (3 cols), Quick Check (3 items).
   * **Sec 3:** Subtopic 2 (Proofs/Mechanisms), Image Box 2, Comparative Matrix, Quick Check (3 items).
   * **Sec 4:** Core Anchor (Literary text for Filipino/Values OR Formula card & two 5-step examples for STEM).
   * **Sec 5:** Inquiry & Analysis (Socratic Seminar OR Math Reasoning & Misconceptions).
   * **Sec 6:** Subtopic 3 (Applied Mastery), Image Box 3, Procedural Matrix, Quick Check (3 items).
   * **Sec 7:** Guided Practice (Task X.1 drill & Task X.2 matrix).
   * **Sec 8:** Contextual Application (Practical real-world task).
   * **Sec 9:** 3-2-1 Exit Ticket, Lesson Summary Box, and Boxed "Faith Connection" reflection.
   * **Sec 10:** Formative Assessment (15 items: 10 Multiple-Choice + 5 Open-Ended/Calculation items).

---

## 📚 2. The Knowledge Files (Inside `KNOWLEDGE_FILES/`)

These 9 files are uploaded to ChatGPT's **Knowledge** base to provide detailed standards for every part of the book:

### 1. `00_REFERENCE_TEXTBOOK_BENCHMARK.docx`
* **Purpose:** The visual model and gold-standard Word file.
* **Specifically Contains:**
  * Sample solid Navy Blue (`#1B365D`) table banners and soft blue section blocks.
  * Exact table styling: 4x4 analytic rubrics, concept matrices, and answer key grids.
  * Visual styling for callout containers (image prompts, YouTube boxes, formula cards).
  * Proof of continuous text flow without awkward blank spaces.

### 2. `01_PEDAGOGICAL_FRAMEWORK_AND_EXEMPLAR.md`
* **Purpose:** The teaching methodology, structure, and pacing guide.
* **Specifically Contains:**
  * **The 70/30 Instructional Formula:** 70% deep reading and explanation, 30% exercises, drills, and rubrics.
  * **Page and Word Budgets:** Exact formulas for 3-lesson units (Filipino/Values) vs 5–7 lesson quarters (Math/Science).
  * **The 3-Page Front Matter Architecture:** Rules for Cover, 350+ word Preface, and clean Table of Contents.
  * **The Detailed 10-Section Lesson Blueprint:** Full instructions for each section of a lesson.
  * **The Faith Connection Standard:** Guidelines for moral and spiritual reflections tied to the lesson topic.

### 3. `02_VISUAL_AND_MULTIMEDIA_STANDARDS.md`
* **Purpose:** Formatting standards for image placeholders and video modules.
* **Specifically Contains:**
  * **Mandatory "Prompts-Only" Rule:** Forbids generating fake images; requires text prompt boxes with Title, Purpose, Prompt, and Replacement Note.
  * **Image Quota:** Exactly 1 cover prompt + 3 image prompts per lesson.
  * **Style Matrix:** When to use **Studio Ghibli watercolor** (covers, stories, history) vs **Realistic Educational Photography** (TLE tools, PE exercises, science lab safety).
  * **Interactive YouTube Module Spec:** Single-cell red-bordered container, official channel name, 3 viewing questions, and zero fake timestamps or AI disclaimers.
  * **Curated Video Bank:** A table of verified, working YouTube URLs for Values Ed, Filipino, and Science.

### 4. `03_DOCX_BUILDER_SCRIPT.py` (or `docx_builder.py`)
* **Purpose:** The Python compilation engine that ChatGPT runs via Code Interpreter.
* **Specifically Contains:**
  * **XML Styling Functions:** Custom code for colored shading, left-stripe borders, dashed borders, and cell padding.
  * **Math Equation Converter:** Converts LaTeX TeX formulas (`$…$` and `$$…$$`) into real native Word math equations (OMML).
  * **Pacing Gating (`append_lesson`):** Estimates page count and warns/rejects lessons if they exceed their page budget.
  * **Typography Checker (`finalize_book`):** Verifies that body text is 10.5 pt with 1.15 line spacing and 0.8-inch margins.

### 5. `04_FRONT_MATTER_AND_ANSWER_KEYS_STANDARDS.md`
* **Purpose:** Standards for Page 1 (Front Cover), Page 3 (TOC), and the Back Matter Answer Keys.
* **Specifically Contains:**
  * **Page 1 Cover Blueprint:** 3-tier navy title banner in quotes (Tier 1: Book Title, Tier 2: Unit Title, Tier 3: Scope Sub-text) tailored for Values, Filipino, Science, Math, and AP.
  * **Page 3 Table of Contents Blueprint:** Strict ban on table grids/pipes (`|...|`); uses a clean hierarchical indented typographic list.
  * **Structured Answer Key Layouts:** Strict ban on paragraph answer blobs; provides table templates for Multiple-Choice grids and 2-column calculation explanations with balanced A–D answers.

### 6. `05_QUALITY_ASSURANCE_AND_CURRICULUM_AUDIT.md`
* **Purpose:** The quality inspector and fact-checking audit.
* **Specifically Contains:**
  * **Zero-Hallucination Fact Verification:** Real Philippine historical dates (Tejeros Convention, Independence Day), real Republic Acts (RA 10533, RA 11476), authentic literary texts, and strict poetic syllable counts (Tanaga: 7-7-7-7).
  * **Grade-Level Calibration Matrix:** Bloom / DOK levels (1 to 4) and Lexile reading difficulty bands from Grade 7 to Grade 10.
  * **Gender-Fair & Inclusive Language:** Rules following DepEd Order No. 32, s. 2017 and IPED cultural inclusion.
  * **The 100-Point DepEd MATATAG QA Audit Scorecard:** 5 pillars evaluated prior to publishing.

### 7. `06_AI_IMAGE_PROMPT_STANDARDS_AND_EXEMPLARS.md`
* **Purpose:** Guide for writing concrete physical image prompts for image generators (Gemini, Midjourney, ChatGPT).
* **Specifically Contains:**
  * **The "Wall of Shame":** Examples of banned lazy prompts (e.g., abstract concepts, mental actions, generic students).
  * **The 5 Physical Cinematographic Pillars:** Prompts must describe Subject, Action, Setting, Props, and Lighting/Camera.
  * **The National Hero Integrity Rule:** Forbids generating AI faces of heroes (Rizal, Bonifacio); uses historical desks, manuscripts, quills, flags, and artifacts instead.
  * **Subject-Specific Prompt Exemplars:** Ready-to-use prompt examples across Filipino, Science, Math, History, and Values Ed.

### 8. `07_MATHEMATICS_TEXTBOOK_STANDARDS.md` (Math Only)
* **Purpose:** Specialized standards that override general writing rules specifically for Mathematics textbooks.
* **Specifically Contains:**
  * **Page Balance:** Reduces reading to short 40-to-70 word explanation chunks (no long prose blocks).
  * **Formula Markup:** All formulas centered on display lines with `$$…$$`, aligned step-by-step solutions at `=`, and real math symbols (`×, ÷, ±, √, π`).
  * **Required Elements:** 10–15 code-drawn figures (number lines, coordinate graphs, geometric angles), 2–4 Key Concept boxes, 4 boxed worked examples, and 20–24 graded exercises.

### 9. `08_SCIENCE_TEXTBOOK_STANDARDS.md` (Science Only)
* **Purpose:** Specialized standards that override general writing rules specifically for Science textbooks.
* **Specifically Contains:**
  * **The 5E Model:** Maps lessons to Engage, Explore, Explain, Elaborate, and Evaluate.
  * **Lesson Balance:** 1,600–2,100 words with short 50–90 word paragraphs.
  * **Hands-on Investigation (Lab):** A complete safe experiment per lesson with question, variables table (independent, dependent, controlled), materials, procedure, data table, and safety box (`::: watchout`).
  * **Visual & Formula Elements:** 1 phenomenon opener image, 2 labeled scientific diagrams, 3–6 code-drawn cycles/flowcharts, and formulas with explicit symbol-quantity-unit tables.

---

## 📁 3. Supporting Files in the Folder

* **`README_SETUP_GUIDE.md`**: Step-by-step 2-minute walkthrough showing where to copy the instructions and how to upload the files in the ChatGPT GPT Builder interface.
* **`SAMPLE_COVER_OUTPUT.jpg` & `SAMPLE_FULL_TITLE_COVER.jpg`**: Visual cover reference examples showing the 3-tier title banner and illustration styling.

---

## ⚡ Quick Reference Table

| File Name | Primary Scope | Specifically What It Contains |
| :--- | :--- | :--- |
| **`INSTRUCTIONS_FOR_CHATGPT.txt`** | Master Instructions | The 10 Core Rules, 10-section lesson blueprint, turn-by-turn pacing, and auto-compilation commands. |
| **`00_REFERENCE_TEXTBOOK_BENCHMARK.docx`** | Layout Sample | Finished Word document showing navy banners, rubrics, table grids, and callouts. |
| **`01_PEDAGOGICAL_FRAMEWORK_AND_EXEMPLAR.md`** | Lesson Recipe | 70/30 teaching ratio, page budgets, 10-section blueprint, and Faith Connection box. |
| **`02_VISUAL_AND_MULTIMEDIA_STANDARDS.md`** | Media Standards | Image prompt box layout, image quotas (3 per lesson), Ghibli vs Photo rules, and verified YouTube links. |
| **`03_DOCX_BUILDER_SCRIPT.py`** | Python Compiler | Code Interpreter engine that converts text into Word format, styles tables, and converts math to real equations. |
| **`04_FRONT_MATTER_AND_ANSWER_KEYS_STANDARDS.md`** | Cover & Back Matter | 3-tier cover banner, typographic TOC without table pipes, and structured MCQ answer grids. |
| **`05_QUALITY_ASSURANCE_AND_CURRICULUM_AUDIT.md`** | Quality Audit | Fact verification (real dates/laws), grade-level Lexile/DOK matrix, and 100-point QA audit scorecard. |
| **`06_AI_IMAGE_PROMPT_STANDARDS_AND_EXEMPLARS.md`** | Visual Prompts | 5-pillar physical scene rule, banned lazy prompts, national hero integrity rule, and subject prompt exemplars. |
| **`07_MATHEMATICS_TEXTBOOK_STANDARDS.md`** | Math Only | Short text chunks, real TeX math formulas, 10–15 code-drawn figures, and 4 step-by-step worked examples. |
| **`08_SCIENCE_TEXTBOOK_STANDARDS.md`** | Science Only | 5E model, phenomenon opener, hands-on lab investigation with safety box, and data tables with units. |
| **`README_SETUP_GUIDE.md`** | Setup Manual | Step-by-step setup guide for creating the Custom GPT in ChatGPT. |
