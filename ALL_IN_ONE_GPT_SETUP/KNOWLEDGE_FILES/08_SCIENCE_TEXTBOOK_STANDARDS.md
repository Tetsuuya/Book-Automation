# 08 — SCIENCE TEXTBOOK STANDARDS (SCIENCE ONLY)

**Scope:** Apply this file ONLY when the subject is **Science** (Grades 3–10: Life, Physical, Earth and Space Science, Chemistry, Physics, Biology). For Science it **overrides** the paragraph-length and image-prompt rules in the Instructions and in files 01, 02, 05, and 06. Every other rule (10-section blueprint, verbatim compilation, answer-key balance, zero branding, Turn pacing) still applies. Mathematics follows file 07; all other subjects ignore this file.

**Why:** A science book teaches learners to observe, measure, and explain. When readers open a science book they expect:

- a **lesson opener**: a striking real-world picture of a phenomenon, a big question, and the key terms to watch for;
- a **quick hands-on activity before the reading** (explore first, explain after);
- **pictures of real things** (organisms, cells, landforms, apparatus) and **process diagrams** (cycles, food chains, input → output) on almost every page;
- **captions that ask a question** ("Which layer is hottest?");
- **data tables and graphs** with units, and formulas with units;
- a **full investigation** with safety rules, and a review that asks learners to read graphs and explain with evidence.

Lessons follow the **5E model** used in DepEd science teaching: Engage, Explore, Explain, Elaborate, Evaluate (mapped onto the 10-section blueprint in Section 5).

---

## 1. Page Balance (What Every Science Lesson Must Contain)

| Element | Per lesson | Rule |
| :--- | :--- | :--- |
| Explanation text | 1,600–2,100 words total | Short blocks of **50–90 words**, each followed by a diagram, table, formula, or example. Never more than **3 consecutive prose paragraphs**. |
| Key terms | 5–8 | Listed in Section 1, bolded where defined, all in the glossary. |
| Quick Activity | 1 | 5–10 minutes in Section 1 (Explore), no special materials. |
| AI image prompts | **3** | **1 phenomenon opener** (Ghibli scene, Section 1) + **2 labeled diagrams** with labels in the image (Section 4.2). |
| Code-drawn figures | **3–6** | Graphs, scales, **cycles, food chains, and flowcharts**, drawn exactly by the compiler (Section 4.1). |
| Key Concept boxes | 2–4 | Definitions, laws, and formulas with units (Section 3). |
| Investigation | **1** | Full lab or field activity with safety box and data table (Section 2). |
| Worked problems | 2–3 | Quantitative topics: boxed, with units in every step. Qualitative topics: 2 boxed **Data Analysis Examples** (read a graph or table, then explain). |
| Practice | **15–20** | Graded: Recall (5–6), Data and Calculation (6–8), Explain with CER (4–6). |
| Formative assessment | 15 items | Unchanged (10 MCQ + 5 open items); at least 3 items use a table or graph. |

Page target: about **8–10 Word pages per lesson**, within **45–75 counted pages** for the book (Cover, Preface, TOC, Synthesis, and Glossary are not counted). Never shrink type to fit (see the Instructions, Rule 3).

---

## 2. The Investigation (Section 8 of the Blueprint Becomes a Lab)

Every lesson has one investigation that learners can do safely with school or household materials. Use this structure:

```
::: note INVESTIGATION 4.2 — Which Material Keeps Water Warm Longest?
**Question:** Does the wrapping material change how fast hot water cools?

**Variables**

| Independent variable | Dependent variable | Controlled variables |
| :--- | :--- | :--- |
| Wrapping material | Temperature after 20 minutes (°C) | Starting temperature, water volume, container, room |

**Materials:** 3 identical cups, warm tap water (not boiling), cloth, foil, newspaper, thermometer, timer.

**Procedure**
1. ...
2. ...

**Data Table**

| Material | Start (°C) | After 10 min (°C) | After 20 min (°C) | Change (°C) |
| :--- | :---: | :---: | :---: | :---: |
| Cloth | | | | |

**Analysis:** 2–3 questions that use the data.
**Conclusion (CER):** Claim, Evidence from your table, Reasoning with the science idea.
:::
```

Put the safety rules in a Watch Out box **immediately before** the investigation:

```
::: watchout SAFETY FIRST
- Wear safety goggles. Use warm tap water only, never boiling water.
- Wipe spills at once. Wash hands after the activity.
:::
```

Safety rules: no flames above a candle or alcohol lamp under teacher control, no strong acids or bases, no electrical mains, no tasting, no unknown chemicals. Prefer vinegar, baking soda, salt, food coloring, batteries up to 9 V.

---

## 3. Formulas, Quantities, and Units

### 3.1 Formulas become real Word equations
Write formulas in TeX, as ChatGPT normally does; the compiler converts them into editable Word equations. Every formula sits inside `$…$` (inline) or `$$…$$` (own line). Never as plain text, never in code blocks.

```
::: concept KEY CONCEPT: Speed
$$ v = \frac{d}{t} $$

| Symbol | Quantity | SI unit |
| :---: | :--- | :--- |
| v | speed | metre per second (m/s) |
| d | distance | metre (m) |
| t | time | second (s) |
:::
```

Every formula box includes a **symbol–quantity–unit table**.

### 3.2 Worked problems keep units in every step
Use the Given–Find–Formula–Solution–Answer pattern inside an `::: example` box. Solution steps go in a `steps` block, aligned at `=`, with units on every line:

````
::: example Sample Problem 1 — A Jeepney's Average Speed
**Problem:** A jeepney travels 12 km in 0.5 h. Find its average speed.

**Given:** d = 12 km, t = 0.5 h   **Find:** v   **Formula:** $v = \frac{d}{t}$

```steps
v = 12 km ÷ 0.5 h | substitute
= 24 km/h | divide
```

**Answer:** The average speed is **24 km/h**.
:::
````

### 3.3 Notation rules

| Item | Write it as | Example |
| :--- | :--- | :--- |
| Chemical formulas | Unicode subscripts in normal text (not TeX) so element symbols stay upright | H₂O, CO₂, C₆H₁₂O₆ |
| Chemical equations | normal text with → and coefficients | 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂ |
| Ions and charges | Unicode superscripts | Na⁺, Cl⁻, Ca²⁺ |
| Scientific notation | TeX inside `$…$` | $3.0 \times 10^{8}$ m/s |
| Units | SI symbols, a space after the number | 25 °C, 9.8 m/s², 1.5 kg |
| Physical constants | accepted values, stated with units | g = 9.8 m/s² near Earth's surface |

---

## 4. Figures: Two Kinds

Science uses **both** kinds of figure. Choose by asking: *does the picture contain numbers, scales, data, or words with arrows?* If yes, draw it with code. If it is a picture of a real thing, use an AI prompt.

### 4.1 Exact figures, drawn by code (numbers, data, and word diagrams)
Graphs, scales, cycles, and flowcharts must be exact (AI garbles numbers and words), so they are written as `figure` blocks. The compiler draws them and numbers them automatically (Figure 4.2.1, …). Available types (keys as in file 07, Section 3.1, plus `flow` and `cycle` below):

| Science need | figure type | Example keys |
| :--- | :--- | :--- |
| Data over time (temperature, growth, cooling) | `line` | `labels: 0 min, 5 min, 10 min, 15 min` · `values: 60, 52, 46, 41` · `ylabel: Temperature (°C)` |
| Comparing groups (plant height by fertilizer, rainfall by month) | `bar` | `labels:` · `values:` · `ylabel:` with unit |
| Composition (gases in air, land use) | `pie` | `labels: Nitrogen, Oxygen, Argon and others` · `values: 78, 21, 1` |
| Thermometer, depth, altitude, ocean zones | `vnumberline` | `range: -10, 40, 10` · `zero: Freezing point of water` · `point:` |
| pH scale, number scales | `numberline` | `range: 0, 14, 1` · `point: 3, vinegar` · `point: 7, pure water` · `point: 12, soap` |
| Distance–time and motion graphs | `coordinate` | `range: 0, 10` · `segment: 0, 0, 4, 8` · `point: 4, 8, A` · `xlabel: Time (s)` · `ylabel: Distance (m)` |
| Food chains, energy transformations, input → process → output, step sequences | `flow` | `items: Sun → Rice plant → Rice field rat → Rice field snake → Philippine eagle` · `label: eaten by` (optional, printed on every arrow) · `direction: right` or `down` (default: right up to 4 items, down for 5 or more) |
| Water cycle, rock cycle, carbon cycle, life cycles | `cycle` | `items: Evaporation, Condensation, Precipitation, Collection` (in order, clockwise from the top) · `center: Water Cycle` |

Every graph has a title or caption, labeled axes **with units**, and values that match the data table beside it. In a `flow`, the arrow points the way energy or matter moves (in a food chain, from the eaten to the eater). Keep each item to 1–3 short words; the compiler wraps the text inside its box.

Examples:

````
```figure
type: flow
items: Carbon dioxide + Water → Photosynthesis (light, chlorophyll) → Glucose + Oxygen
caption: Photosynthesis turns carbon dioxide and water into food. What does the plant release?
```

```figure
type: cycle
items: Evaporation, Condensation, Precipitation, Collection
center: Water Cycle
caption: The water cycle. Which stage forms clouds?
```
````

### 4.2 AI pictures: 1 opener scene + 2 labeled diagrams
Each lesson has **3 AI image prompt boxes** (format from file 06):

1. **Phenomenon opener (Section 1), Studio Ghibli scene, no text:** the lesson's phenomenon happening in a Philippine setting (Mayon at dawn, a flooded rice paddy, a jeepney braking). It sits right below the lesson banner, like a chapter-opener picture.
2. **Two labeled diagrams (Sections 2, 3, or 6):** the real structure the lesson teaches, **with its labels drawn in the image**, like a real science book: parts of a plant cell, layers of the Earth, parts of a flower, a volcano cross-section, a microscope, a filtration setup, a spring scale.

**Every box starts from its INTENT.** Write the **Shows:** line first: the one idea the picture must make visible, taken from the text right before it and the task right after it. Then describe only what proves that idea, accurately. Anything that does not serve the intent stays out.

**Labeled diagram rules:**
- **Accurate first:** correct shapes, positions, proportions, and colors for the real thing at the learner's grade level. Name every part you want drawn, and where it is ("nucleus near the center, chloroplasts along the cell edge").
- **3–6 labels**, each 1–3 words, spelled exactly as in the lesson text and glossary. Put them in the prompt in quotes: `labels with thin leader lines pointing to each part: "Cell wall", "Cell membrane", "Nucleus", "Chloroplast", "Vacuole"`.
- **Style tag:** `clean labeled science textbook diagram, accurate proportions, soft colors, white background, clear sans-serif labels, no other text, no logos, no watermark. Wide 16:9 landscape image.`
- **Check line in the Replacement Note:** the author checks each label's spelling and that each leader line points to the right part. If one is wrong, regenerate, or cover it with a Word text box.
- **Any generator (Gemini, ChatGPT):** write the labels as a sentence ("Add only these labels in clear sans-serif text with thin leader lines: ..."), never as tool flags. If one label is misspelled or points wrong, ask the generator in the same chat to fix just that label.

**Still NOT AI (code `figure`, 4.1, or a table):** anything with numbers, scales, or measured values (graphs, thermometer readings, distance–time), cycles, food chains, flowcharts, circuits, ray and force diagrams, and the periodic table. AI misplaces numbers and arrow directions.

**For all three:**
- **Every caption asks one question** about the intent: "Figure 7.1.2 Parts of a plant cell. Which part makes food?" If you cannot write that question, the picture has no job: drop it.
- **Short prompt, 40–70 words,** in plain words; no jargon ("orthographic", "molecule-inspired clusters").
- **Context decides the style** (file 06, Part 3): a scene, story, or opener is Ghibli; a picture learners must recognize in real life (a rock sample, a real Philippine species) may be a real photo; a picture whose job is naming parts is a labeled diagram.
- **People** in lab or field-work scenes wear proper safety gear (goggles, gloves) and follow safe practice.

Example boxes:

```
> ### 🖼️ Figure: Mayon at Dawn
> **Shows:** A volcano is an opening where hot material from inside the Earth comes out.
> **AI Prompt:** Mayon Volcano at dawn with a thin plume of steam rising from its perfect cone, rice fields and a small village in the foreground, farmers looking up, soft golden light, Studio Ghibli-inspired warm watercolor illustration, no text, no logos, no watermark. Wide 16:9 landscape image.
> **Replacement Note:** Insert the image (Insert > Pictures). Caption: "Mayon steams at dawn. Where does the steam come from?"
```

```
> ### 🖼️ Figure: Parts of a Plant Cell
> **Shows:** A plant cell has a cell wall and chloroplasts, which an animal cell does not have.
> **AI Prompt:** A single plant cell cut open, rectangular with a thick green cell wall, a thin cell membrane just inside it, a large clear vacuole in the middle, a round nucleus beside it, small green chloroplasts along the edges, labels with thin leader lines pointing to each part: "Cell wall", "Cell membrane", "Vacuole", "Nucleus", "Chloroplast", clean labeled science textbook diagram, accurate proportions, soft colors, white background, clear sans-serif labels, no other text, no logos, no watermark. Wide 16:9 landscape image.
> **Replacement Note:** Insert the image. Check: all 5 labels spelled right, each line points to its part. Caption: "Parts of a plant cell. Which two parts are missing in an animal cell?"
```

---

## 5. Science Lesson Flow (Inside the 10-Section Blueprint)

| Blueprint section | 5E stage | What goes there |
| :--- | :--- | :--- |
| 1. Alignment & opener | **Engage, Explore** | Phenomenon opener image; the big question ("Why does Taal steam?"); learners write a first explanation; 5–8 **Key Terms**; the video box; a 5–10 minute **Quick Activity** with no special materials (e.g., breathe on a cold glass to see condensation). |
| 2, 3. Subtopics 1–2 | **Explain** | Short text → labeled diagram, graph, cycle, or flow → Key Concept box → Quick Check. |
| 4. Core anchor | **Explain** | Formula box and Sample Problems (quantitative), or Data Analysis Examples (qualitative). |
| 5. Reasoning | **Elaborate** | Watch Out box with **Wrong idea → Scientific idea** pairs (e.g., "Heavier objects fall faster" → "Without air resistance, all objects fall with the same acceleration"). |
| 6. Subtopic 3 | **Elaborate** | Application to Philippine contexts, technology, health, or the environment. |
| 7. Practice | **Evaluate** | Graded practice (`exercises` blocks for short items), including graph and table reading. |
| 8. Application | **Explore, Elaborate** | The full Investigation (Section 2 of this file), with SAFETY FIRST. |
| 9. Exit ticket | **Evaluate** | Revisit the opening phenomenon: learners rewrite their first explanation as a CER, then the summary box, then the boxed **FAITH CONNECTION** (file 01, Section 7A) built on the lesson's own science. |
| 10. Assessment | **Evaluate** | 15 items, at least 3 using a table or graph. |

---

## 6. Science Prose Style

- Explain cause → effect → evidence. Prefer "because" sentences over descriptive lists.
- Bold each new term once, where it is defined; every term goes in the glossary.
- Prefer a table or a figure over a paragraph when comparing.
- State values with units and, for constants, their accepted value.
- No fabricated studies, statistics, or dates; cite real sources (PAGASA, PHIVOLCS, DOST, NASA) when quoting data.

---

## 7. Science QA Checklist (add to the file 05 audit)

- [ ] Lesson opens with a phenomenon opener image, a big question, 5–8 key terms, and a Quick Activity; it closes by explaining the phenomenon with CER.
- [ ] Cycles, food chains, and flowcharts are code-drawn (`cycle`, `flow`), never AI.
- [ ] Every figure caption ends with a visual-check question.
- [ ] 1 safe investigation per lesson, with variables table, data table, and SAFETY FIRST box.
- [ ] Every formula is a Word equation inside a Key Concept box with a symbol–quantity–unit table.
- [ ] Units on every quantity and in every solution step.
- [ ] Chemical formulas use Unicode subscripts (H₂O), never TeX.
- [ ] Graphs and scales are code-drawn `figure` blocks with labeled axes and units.
- [ ] 3 AI prompts per lesson: 1 Ghibli opener (no text) + 2 accurate labeled diagrams (3–6 quoted labels, matching the glossary spelling); every box has a **Shows:** intent line and a label check.
- [ ] No AI images for graphs, scales, measured values, cycles, food chains, circuits, ray or force diagrams, or the periodic table.
- [ ] 15–20 graded practice items; at least 3 assessment items use a table or graph.
- [ ] Every scientific claim and value is accurate for the grade level.
- [ ] Every lesson has a FAITH CONNECTION box built on that lesson's own science; no verse is used as scientific proof.
