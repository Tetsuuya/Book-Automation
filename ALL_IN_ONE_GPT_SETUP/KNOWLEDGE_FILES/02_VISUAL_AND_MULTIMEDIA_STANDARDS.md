# DEPED MATATAG VISUAL MEDIA & INTERACTIVE MULTIMEDIA STANDARDS

This document specifies the exact format and styling for all visual placeholders, AI generation prompts, and interactive YouTube video modules across ALL DepEd MATATAG subjects (Science, Math, English, Filipino, AP, MAPEH, TLE).

---

## 1. VISUAL CONCEPT ART & AI PROMPT SPECIFICATION

Whenever a `[VISUAL: ...]` tag is embedded into the textbook, it must be structured as a dedicated visual prompt callout frame:

### Formatting Rules:
- **Box Shading**: Soft Gray-Blue (`#F4F7FA`)
- **Border**: Navy Blue (`#1B365D`, 4.5pt / `sz="36"`) solid left border. Subtle light borders on top, right, and bottom (`#D0D7DE`).
- **Header**: `🖼️ [IMAGE PLACEHOLDER: Specific Subject Title]` in 10.5pt Bold Navy Blue (`#1B365D`).
- **Pedagogical Function**: 1–2 sentences explaining how this visual supports the learning competency.
- **Strict Zero-Branding Rule for Prompts**:
  * **NEVER** include publisher names, brand names, or government acronyms (`DepEd`, `MATATAG`, `CERE`) inside ANY AI image prompt.
  * AI image generators (Midjourney, DALL-E) try to render acronyms as distorted text, fake badges, or watermark artifacts.
  * Always describe pure visual elements (scene, lighting, subjects, uniforms without badges, historical context, colors).
  * Always append negative styling: `no text, no logos, no watermark, no branding --ar 16:9 --v 6.0` (or `--ar 8.5:11` for covers).
- **Teacher / Student Instruction**: *"Paunawa: Palitan ang kahong ito ng nabuong larawan sa Microsoft Word (Insert > Pictures)."*

---

## 2. INTERACTIVE YOUTUBE MULTIMEDIA MODULES (BULLETPROOF, REAL LINKS)

### ⚠️ ZERO-HALLUCINATION POLICY FOR YOUTUBE LINKS:
LLMs frequently hallucinate fake video IDs (e.g., `watch?v=abcdef12345` or random 11-letter codes) which result in frustrating **"404 Video Unavailable"** errors for teachers and students. To guarantee that every link ALWAYS works 100% of the time:

1. **NEVER FABRICATE RANDOM 11-CHARACTER VIDEO IDs**: Do not invent fake `watch?v=...` URLs.
2. **MANDATORY DUAL-LINKING SYSTEM**:
   - **Primary Direct Link (Search Query URL)**: Use official YouTube Search Query URLs. These NEVER expire, NEVER 404, and immediately open the active official video on YouTube mobile app and desktop!
     - Format: `https://www.youtube.com/results?search_query=[URL_ENCODED_TERMS]`
     - Example (Science): `https://www.youtube.com/results?search_query=DepEd+TV+Science+7+Cellular+Transport`
     - Example (Filipino): `https://www.youtube.com/results?search_query=Knowledge+Channel+Panitikan+Panahon+ng+Espanyol`
     - Example (Math): `https://www.youtube.com/results?search_query=Khan+Academy+Linear+Equations+Coordinate+Plane`
   - **Real Verified Video Link**: If your Web Search tool is active, search for the official video from trusted channels (*DepEd TV, Knowledge Channel, CrashCourse, Khan Academy, DOST-SEI, GMA Public Affairs*) and provide the verified URL.
3. **Explicit Search Keywords**: Always provide the exact plain-text query in quotes so students and teachers can also type it directly into the YouTube search bar.

### Required Module Layout & Styling:
- **Box Shading**: Soft Red (`#FFF5F5`)
- **Left Border**: Solid YouTube Red (`#CC0000`, 4.5pt / `sz="36"`)
- **Title**: `🎥 INTERAKTIBONG MULTIMEDIA: [MODULE TITLE]` (10.5pt Bold YouTube Red)
- **Verified Channels**: Must cite recognized channels (*DepEd TV Official, Knowledge Channel, CrashCourse, Khan Academy, DOST-SEI, GMA Public Affairs*).
- **Search & Watch URL**: Direct active search URL that is guaranteed to open active videos without 404.
- **Search Keywords**: Exact plain-text query in quotes.
- **QR Code Frame**: ``
- **Key Timestamps**: 2–3 specific timestamps with observational focus.
- **Socratic Viewing Questions (3 Items)**:
  1. *Recall / Direct Observation*: What specific evidence or phenomenon was shown?
  2. *Concept Connection*: How does this explain the principle in the lesson?
  3. *Real-World Critical Thinking*: What are the societal, ethical, or practical implications?

### YouTube Module Exemplar (Filipino-Medium):
```text
🎥 INTERAKTIBONG MULTIMEDIA: Paglalayag sa Panitikan ng Panahong Kolonyal
Opisyal na Channel: Knowledge Channel / DepEd TV Official
Search & Watch Link: https://www.youtube.com/results?search_query=Knowledge+Channel+Panitikan+sa+Panahong+Kastila
Search Keywords: "Knowledge Channel Panitikan sa Panahon ng Espanyol Pasyon Urbana at Feliza"

Mga Tampok na Bahagi (Timestamps):
• 02:10 - 05:30: Pagsusuri sa pagdating ng imprenta at Doctrina Christiana sa Maynila noong 1593.
• 07:15 - 11:40: Pasyon at Senakulo bilang multimodal na pagpapahayag ng pananampalataya.

Mga Gabay na Tanong sa Panonood:
1. Batay sa video, anong teknikal na pamamaraan ang ginamit ng mga manlilimbag sa unang aklat?
2. Paano ipinakita sa dokumentaryo ang paggamit ng Pasyon sa pagpapahayag ng damdaming bayan?
3. Bakit naging napakalakas ng biswal at pasalitang anyo ng panitikan sa panahong iyon?
```

### YouTube Module Exemplar (English-Medium / Science):
```text
🎥 INTERACTIVE MULTIMEDIA: Cellular Transport in Living Organisms
Official Channel: CrashCourse / DOST-SEI / Khan Academy
Search & Watch Link: https://www.youtube.com/results?search_query=CrashCourse+Biology+InDaClub+Cell+Membranes+Transport
Search Keywords: "CrashCourse Biology Cell Membranes and Transport Diffusion Osmosis"

Key Timestamps to Observe:
• 01:45 - 04:15: Phospholipid bilayer fluid mosaic structure and selective permeability.
• 05:20 - 08:35: Passive vs. active transport mechanisms across membrane gradients.

Socratic Viewing Questions:
1. What molecular properties determine whether a particle can diffuse directly through the lipid bilayer?
2. How does the documentary illustrate the role of ATP energy in active transport pumps?
3. Relate cellular osmotic regulation to how plant root systems absorb water from hypertonic or hypotonic soil.
```

---

## 3. SUBJECT-SPECIFIC COVER & VISUAL PROMPT EXEMPLARS

### Cover Art Exemplar 1: Filipino-Medium (Grade 7 Filipino)
```text
[PROMPT SA PAGBUO NG LARAWAN SA PABALAT / FRONT COVER AI IMAGE PROMPT]
PAMAGAT NG AKLAT: Gabay Pampagkatuto sa Filipino 7
BAITANG AT YUNIT: Filipino Baitang 7 • Yunit III: "Ako at ang Aking Pagkatao, Tanglaw ng Katatagan"
PAKSA: Panitikan sa Panahon ng Espanya • Tekstong Pampahayagan • Wika at Multimodal

PROMPT: A prestigious, high-end educational textbook cover layout. At the top of the cover, a sleek deep navy blue graphic banner featuring clean, crisp, perfectly rendered typography. The primary headline in bold white capital letters reads: "GABAY PAMPAGKATUTO SA FILIPINO 7". Below it, a secondary title in elegant warm gold letters reads: "YUNIT III: AKO AT ANG AKING PAGKATAO, TANGLAW NG KATATAGAN". Beneath in subtle light silver text: "Panitikan sa Panahon ng Espanya • Tekstong Pampahayagan • Wika at Multimodal". In the lower two-thirds illustration, two Filipino Grade 7 students (a 13-year-old boy and girl in neat modern school uniforms) studying together at a wooden table under warm golden morning light with an open book and study materials. In the background, a historic Spanish-colonial stone church belfry and majestic Philippine mountains under a luminous sunrise. Clean textbook graphic design, perfectly centered professional typography, ultra-high resolution, no gibberish text, no watermarks, no logos --ar 8.5:11 --v 6.0
```

### Cover Art Exemplar 2: English-Medium (Grade 8 Science)
```text
[FRONT COVER AI IMAGE PROMPT / COVER ART SPECIFICATION]
BOOK TITLE: Learning Guide in Science 8
GRADE & UNIT: Science Grade 8 • Unit II: "Force, Motion, and Energy Transformations"
SCOPE: Newtonian Mechanics • Work and Power • Energy Flow in Living Ecosystems

PROMPT: A prestigious, high-end educational textbook cover layout. At the top of the cover, a sleek deep navy blue graphic banner featuring clean, crisp, perfectly rendered typography. The primary headline in bold white capital letters reads: "SCIENCE 8: LEARNING GUIDE". Below it, a secondary title in elegant warm gold letters reads: "UNIT II: FORCE, MOTION, AND ENERGY". Beneath in subtle light silver text: "Newtonian Mechanics • Work and Power • Energy Transformations". In the lower two-thirds illustration, two Filipino junior high school students (a 14-year-old boy and girl wearing protective laboratory goggles and modern school uniforms) actively conducting a physics mechanics experiment with dynamic tracks and photogate timers in a modern, well-lit school laboratory. In the background, illuminated chalkboard blueprints of physics vector vectors and dynamic energy conversion models. Clean textbook graphic design, perfectly centered professional typography, ultra-high resolution, no gibberish text, no watermarks, no logos --ar 8.5:11 --v 6.0
```

### Science (Cellular & Laboratory):
```text
🖼️ [IMAGE PLACEHOLDER: High-Resolution 3D Cross-Section of Plant Cell Organelles]
Layunin: Demonstrates the structural relationship between rigid cellulose cell wall, large central vacuole, and emerald chloroplasts during photosynthesis.
AI Prompt: A highly detailed, photorealistic 3D anatomical cross-section diagram of a eukaryotic plant cell (Allium cepa) on an ultra-clean scientific laboratory background. Clear distinct visualization of the cell wall, central vacuole, bright emerald green chloroplasts, and translucent nucleus. Vibrant color-coded educational palette, studio lighting, volumetric glow, high scientific accuracy, 8k resolution, documentary science textbook quality, no text, no logos, no watermark --ar 16:9 --v 6.0
```

### Mathematics (Vector & 3D Geometry):
```text
🖼️ [IMAGE PLACEHOLDER: 2D Cartesian Coordinate Plane with Linear Functions]
Layunin: Visualizes linear slope intercept equations and coordinate intersection points.
AI Prompt: A clean, high-precision mathematical diagram of a 2D Cartesian coordinate plane on subtle blueprint grid paper. Crisp, dark navy x-axis and y-axis clearly labeled from -10 to +10. A bold royal blue linear function line intersecting the y-axis with distinct labeled coordinate points (0,2) and (3,8). Minimalist, high contrast, clean vector style, textbook mathematical illustration, no text, no logos, no watermark --ar 16:9 --style raw
```

### English (Afro-Asian / World Literature):
```text
🖼️ [IMAGE PLACEHOLDER: Dramatic Staging of Classical Theatrical Dialogue]
Objective: Visualizes stage blocking, dramatic staging, and character conflict in oral communication.
AI Prompt: An evocative, high-detail editorial illustration of a classical dramatic theater performance. Two actors in period costume performing an intense dialogue on a wooden stage with dramatic spotlighting and rich atmospheric haze. Expressive character gestures, historical costume accuracy, cinematic depth of field, warm theatrical lighting, fine arts textbook illustration style, no text, no logos, no watermark --ar 16:9 --v 6.0
```

### Araling Panlipunan (Philippine & Asian History):
```text
🖼️ [IMAGE PLACEHOLDER: Archival Reconstructed Scene of the Manila Galleon Trade]
Layunin: Reconstructs historic maritime trade, global commodity exchange, and cultural encounters.
AI Prompt: A meticulously detailed historical painting depicting a 17th-century Spanish-Manila galleon docked in Manila Bay during loading. Port workers, merchants, and mariners handling crates of silk, porcelain, and spices under a warm tropical sun. Authentic period naval architecture, historical accuracy, rich sepia and ocean blue tones, museum quality historical illustration, no text, no logos, no watermark --ar 16:9 --v 6.0
```

### MAPEH (Music, Arts, PE, Health):
```text
🖼️ [IMAGE PLACEHOLDER: Mindanaoan Kulintang Gong Ensemble]
Layunin: Preserves indigenous cultural organology and traditional performance crafts.
AI Prompt: A culturally authentic, highly detailed still-life illustration of a complete traditional Mindanaoan Kulintang ensemble set. Ornate, intricately hand-carved okir wooden frame (antangan) holding a row of eight bossed bronze gongs with glowing metallic sheen. Beside it, agung gongs and dabakan drum. Warm dramatic lighting, museum quality, cultural dignity, no text, no logos, no watermark --ar 16:9 --v 6.0
```

### TLE / TVL (Technical & Industrial):
```text
🖼️ [IMAGE PLACEHOLDER: Mortise and Tenon Woodworking Joint Blueprint]
Layunin: Exploded technical drafting for furniture and structural joinery.
AI Prompt: A crisp technical drafting illustration showing exploded and assembled views of a classic Mortise and Tenon wood joint. Clear millimeter dimension lines, wood grain textures (Narra wood), clean isometric lines, blueprint aesthetic, engineering drawing style, no text, no logos, no watermark --ar 16:9 --style raw
```
