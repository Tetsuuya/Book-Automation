# 07 — MATHEMATICS TEXTBOOK STANDARDS (MATH ONLY)

**Scope:** Apply this file ONLY when the subject is **Mathematics**. For Mathematics it **overrides** the paragraph-length, word-budget, and image-prompt rules in the Instructions and in files 01, 02, 05, and 06. Every other rule (10-section blueprint, verbatim compilation, answer-key balance, zero branding, Turn pacing) still applies. Science, English, Filipino, AP, Values Ed, MAPEH, and TLE ignore this file.

**Why:** A math book is read with a pencil. Learners should see numbers, figures, formulas, and worked steps on every page, with short sentences connecting them. Long academic paragraphs make a math book read like a social-studies book.

---

## 1. Page Balance (What Every Math Lesson Must Contain)

| Element | Per lesson | Rule |
| :--- | :--- | :--- |
| Explanation text | 1,400–1,900 words total | Short blocks of **40–70 words**, each followed immediately by a formula, figure, or example. Never more than **2 consecutive prose paragraphs**. |
| Code-drawn figures | **10–15** | Small, exact, numbered, captioned (Section 3). |
| Key Concept / Rule boxes | 2–4 | Definitions, rules, and properties (Section 2). |
| Worked examples | **4** | Each in an `::: example` box with steps aligned at `=`, and at least 2 of the 4 with a figure. |
| Practice exercises | **20–24** | Graded: Basic (10–12), Intermediate (6–8), Challenge / Word Problems (4). |
| Formative assessment | 15 items | Unchanged (10 MCQ + 5 open items). |

Page target: about **8–9 Word pages per lesson**, so a 6- or 7-lesson quarter lands within **45–75 counted pages** (Cover, Preface, TOC, Synthesis, and Glossary are not counted). The figures and exercises add pages, so the prose is shorter to compensate. Never shrink type to fit (see the Instructions, Rule 3).

---

## 2. How Formulas Must Appear

### 2.1 Display formulas: on their own line, centered
Write every important formula or equation on its **own line** between `$$` markers. The compiler typesets it as real Word math (Cambria Math, centered, larger). **Math must never reach Word as plain text.**

**TeX is welcome.** Write formulas the way ChatGPT normally does; the compiler converts all of it into real, editable Word equations (stacked fractions, roots, exponents, subscripts):

| You write (TeX) | Where |
| :--- | :--- |
| `$$ \frac{f}{n} \times 360^\circ $$` or a `\[ … \]` block | display formula, centered on its own line |
| `$x^{2}$` or `\( -4 + 9 = 5 \)` | inline formula inside a sentence |
| `\begin{aligned} … &= … && \text{reason} \\ … \end{aligned}` inside `$$` | aligned solution steps (same as a `steps` block) |
| `\frac \dfrac \sqrt \times \div \cdot \pm \le \ge \neq \approx \pi \circ \text{} \left( \right)` | all converted |

Rules: put every formula inside `$…$`, `$$…$$`, `\(…\)`, or `\[…\]`. Never put formulas inside code blocks, never as images. Money uses ₱ (a plain `$5` stays text).

```
$$ \text{Sector angle} = \frac{f}{n} \times 360^\circ $$
$$ (−a) + (−b) = −(a + b) $$
```

The simpler Unicode notation below also works inside `$$ … $$`:

| Write | Word shows |
| :--- | :--- |
| `frac(3, 4)` | a stacked fraction with a bar (3 over 4) |
| `x^(n+1)` or `x²` | a superscript |
| `abs(−5)` or vertical bars around −5 | absolute-value bars ∣−5∣ |
| `×  ÷  −  ±  ≤  ≥  ≠  √  π  °` | the real symbols |

Inline math inside sentences stays short (for example, −4 + (−7)). Anything longer than about 12 characters, or anything learners must remember, goes on a display line.

### 2.2 Key Concept boxes
Rules, definitions, and properties go in a boxed Key Concept, with a display formula and the meaning of every letter:

```
::: concept KEY CONCEPT: Adding Integers with the Same Sign
Add the absolute values. Keep the common sign.
$$ (−a) + (−b) = −(a + b) $$
where a and b are whole numbers.
:::
```

### 2.3 Solution steps aligned at the equals sign
Inside worked examples, write the solution as a `steps` block: one step per line, the **reason after a `|`**. Continuation lines begin with `=`. The compiler aligns every `=` in one column.

````
```steps
−4 + (−7) = −(4 + 7) | same signs: add the absolute values, keep −
= −11 | simplify
```
````

### 2.4 Worked example boxes
Every worked example is one boxed block. It may contain text, a figure, a steps block, and the final answer:

````
::: example Worked Example 2 — Net Change in Savings
**Problem:** A learner saves ₱150, then spends ₱230. Find the net change.

**Given:** +150 and −230   **Find:** the net change in pesos

```figure
type: numberline
range: -100, 200, 50
hop: 0, 150, +150
hop: 150, -80, −230
point: -80, −80
caption: Starting at 0, move 150 right, then 230 left.
```

```steps
150 + (−230) = −(230 − 150) | different signs: subtract, keep the sign of the larger absolute value
= −80 | simplify
```

**Answer:** The net change is **−₱80**, a decrease of ₱80.
:::
````

The 5-step pattern (Problem, Given, Find, Formula/Rule, Step Solution, Final Answer) still applies; the steps block is the "Step Solution".

---

## 3. Figures Are Drawn by Code, Not by AI

AI image generators miscount objects, space ticks unevenly, and garble numbers. A wrong number line is worse than none. Therefore, in Mathematics:

- **Lesson figures are written as `figure` blocks.** The compiler draws them exactly (matplotlib) and numbers them automatically (Figure 3.3.1, 3.3.2, …) with the caption below.
- **Only the cover uses an AI image prompt** (Ghibli style, per file 06). Lessons contain **zero** `🖼️` AI prompt boxes, unless no figure type below fits (then use one technical-diagram prompt box from file 06).
- Every number in a figure must match the text and the example next to it.
- Place each figure **right after** the sentence or example it supports.

### 3.1 Figure types and keys

One `key: value` per line. Keys marked "repeatable" may appear several times. Use plain hyphens for negative numbers in values (the figure prints true minus signs).

| type | Use for | Keys |
| :--- | :--- | :--- |
| `numberline` | integers, ordering, opposites, addition/subtraction hops | `range: min, max[, step]` · `point: value[, label]` (repeatable) · `hop: start, end[, label]` (repeatable) · `distance: a, b[, label]` (bracket for absolute value) · `caption:` |
| `vnumberline` | temperature, elevation, sea level, floors | same keys as `numberline`, drawn vertically · `zero:` label for 0 (e.g., Sea level) |
| `counters` | zero pairs, integer addition/subtraction models | `positive: n` · `negative: n` · `pairs: yes` (circles each zero pair) · `remove: n, positive` or `remove: n, negative` (crosses out counters for subtraction) · `caption:` |
| `groups` | multiplication as equal groups | `groups: n` · `each: k` (negative k draws red counters) · `caption:` |
| `bar` | bar graphs | `labels:` · `values:` · `xlabel:` · `ylabel:` · `title:` · `caption:` |
| `line` | line graphs over time | same keys as `bar` |
| `pie` | pie graphs | `labels:` · `values:` · `angles: yes` (prints each sector's degrees) · `caption:` |
| `stemleaf` | stem-and-leaf plots | `data:` · `key:` (e.g., 1 / 2 means 12 minutes) · `caption:` |
| `coordinate` | coordinate plane | `range: min, max` · `point: x, y[, label]` (repeatable) · `segment: x1, y1, x2, y2` (repeatable) · `xlabel:` · `ylabel:` · `caption:` |
| `polygon` | shapes with labeled sides and angles | `vertices: A(0,0), B(4,0), C(4,3)` · `side: AB, 4 cm` (repeatable) · `right: B` (right-angle mark) · `caption:` |

Example (zero pairs):

````
```figure
type: counters
positive: 5
negative: 3
pairs: yes
caption: Three zero pairs cancel, leaving +2.
```
````

### 3.2 Expected figures per Grade 7–10 topic

| Topic | Figures learners expect |
| :--- | :--- |
| Statistics | frequency table + bar, pie (with angles), line graph, stem-and-leaf plot |
| Integers | number line for every comparison or operation; counters for zero pairs; thermometer/elevation scales |
| Integer operations | counters and number-line hops for + and −; equal groups for ×; inverse checks for ÷ |
| Algebra | tables of values with a coordinate graph; balance or tile models (AI prompt box if no type fits) |
| Geometry and measurement | polygons with labeled sides, right-angle marks, coordinate figures |

---

## 4. Practice Sets Look Like a Math Book

Use an `exercises` block. Write one item per line with **no numbers**; the compiler numbers them and sets them in columns.

````
```exercises cols=3 start=1
(+8) + (+13)
(−9) + (−6)
(+17) + (−24)
```
````

- **Basic:** `cols=3`, short computations.
- **Intermediate:** `cols=2`, multi-step or "find the missing number".
- **Challenge / Word Problems:** normal numbered list (`1.`), one problem per line, with units.
- Continue numbering across levels with `start=` (Basic 1–12, Intermediate 13–18, Challenge 19–22).
- Every exercise has an answer in the Back Matter key.

---

## 5. Math Prose Style

- Write like a math book, not an essay: **definition → formula → figure → example → check**.
- Bold each new term once, where it is defined.
- Prefer a table or figure over a paragraph when comparing cases.
- Watch Out boxes show **Wrong → Right** pairs with one-line reasons.
- No history, motivation, or values paragraphs inside subtopics; keep context to the Background (Section 1) and the Contextual Application (Section 8).

---

## 6. Math QA Checklist (add to the file 05 audit)

- [ ] Every rule, property, and key equation is on a `$$` display line or inside a `concept` box.
- [ ] 4 worked examples per lesson, each boxed, each with an aligned `steps` block.
- [ ] 10–15 code-drawn figures per lesson; no AI prompt boxes inside lessons.
- [ ] Every number in every figure matches the text beside it.
- [ ] 20–24 graded exercises per lesson, all answered in the key.
- [ ] No prose run longer than 2 paragraphs; no paragraph over 70 words inside subtopics.
- [ ] No formula left as plain text: every formula sits inside `$…$`, `$$…$$`, `\(…\)`, or `\[…\]` (TeX allowed) so it compiles into a real Word equation.
