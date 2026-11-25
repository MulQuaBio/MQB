---
orphan: true
---

# AI-assisted programming · figure credits

The CodeRefinery images and their adaptations below are from *Responsible Use of
Generative AI in Assisted Coding*, version 2026-11-13, pinned at
[`d1a0a704`](https://github.com/coderefinery/coding-with-ai/tree/d1a0a7049d890f5ebeb9ee6ee713a40d810a2572).
Copyright (c) CodeRefinery. The adapted materials are available under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). See the
[full text](CC-BY-4.0.txt) and [CodeRefinery's attribution instructions](https://coderefinery.github.io/coding-with-ai/reusing/).

| MQB file | Source and changes |
| --- | --- |
| `llm.png`, `intro_chatbot.png`, `full_control.png` | CodeRefinery illustrations reproduced as supplied. |
| `tokens.webp` | New MQB illustration of the idea in `llm_blocks.png`, which CodeRefinery credits to [Simo Tuomisto](https://github.com/simo-tuomisto/understanding-ai-landscape-lecture). Copyright (c) 2026 Simo Tuomisto. See the [Tuomisto MIT notice](Simo-Tuomisto-MIT.txt). |
| `editor.webp`, `included-context.webp` | `intro_ide-integ.png` and `hidden_context.png`, redrawn respectively. Reworded the labels and distinguished optional from explicitly supplied context. |
| `agent-loop.webp`, `agent-review.webp` | Adapted `intro_agentic.png`, `agentic.png` and the example attached to the `open_code.png` illustration. Show the bounded review loop and the practice file, protected inputs and independent check. |
| `delegation.webp` | Combined `scenarios.png` and `scenarios_summary.png` into the three actions a learner reviews. |
| `risk.webp` | `risk-domains.png` redrawn with shorter labels. The surrounding text carries examples of the overlapping domains. |
| `context-window.webp` | Replaced the `llm_context_windows_2026.png` comparison table with a conceptual diagram of what can make up a request. |
| `notebook_components.png` | Reproduced as supplied. From [CodeRefinery's Jupyter lesson](https://coderefinery.github.io/jupyter/interface/), [CC BY 4.0](https://github.com/coderefinery/jupyter/blob/main/LICENSE). |
| `notebook-cells.webp` | Adapted the notebook explanation accompanying `JupyterInterface.png` from [CodeRefinery's Jupyter lesson](https://coderefinery.github.io/jupyter/interface/), CC BY 4.0. Uses an illustrative pollinator notebook cell and a hand-checked output. |

## Image generation record

MQB's redraws used the built-in ChatGPT ImageGen tool. Reference images came
from the pinned source. The scientific meanings, captions and accessible text
were reviewed separately.

### tokens

Source files supplied to ImageGen: none, text prompt only.

> Scientific educational diagram for a quantitative biology lecture, landscape. Create a sharp, spare diagram in the spirit of a simple typeset university lecture graphic, dark navy ink, deep teal and warm ochre accents on an off-white background, generous margins. Three steps from left to right, with identical chips visually repeated as the sequence grows. First 'Input tokens' then 'Predict one token' then 'Append and repeat'. Exactly these labels, letter-perfect, one label per step. Use abstract geometric token chips without text, with one ochre chip in the last panel appended AFTER the teal chips. Clear arrows in a single consistent reading direction. No title, no branding, no decorative extra text. Large labels legible on a projector.

### editor

Source files supplied to ImageGen: `img/intro_ide-integ.png`.

> Show exactly two labelled boxes: ‘Code editor’ and ‘AI service’. An arrow from the editor to the service is labelled ‘Request and context’. An arrow back is labelled ‘Suggested code’. Show the learner inspecting the suggested line inside the editor with a small magnifying-glass icon. Keep the arrows visually distinct and give them clear arrowheads. Scientific educational diagram for an MQB university lecture or textbook, landscape. Use a restrained two-dimensional diagram on almost-white paper, navy type, deep teal and muted ochre accents, clear lines, spacious margins and large readable sentence-case labels. No extra text, branding, logos, product screenshots or title. Keep the figure sparse. Use the reference for its teaching concept; make the new structure and exact wording below.

### included-context

Source files supplied to ImageGen: `img/hidden_context.png`.

> Show three clearly distinguished cards labelled ‘Selected code’, ‘Active file’, and ‘Other project files’. A solid line from the first and two dashed lines from the latter cards converge into a single card labelled ‘Request to the service’. No line crosses a label. The dashed lines represent context that depends on tools or settings. Only the four supplied labels. Scientific educational diagram for an MQB university lecture or textbook, landscape. Use a restrained two-dimensional diagram on almost-white paper, navy type, deep teal and muted ochre accents, clear lines, spacious margins and large readable sentence-case labels. No extra text, branding, logos, product screenshots or title. Keep the figure sparse. Use the reference for its teaching concept; make the new structure and exact wording below.

### agent-loop

Source files supplied to ImageGen: `img/intro_agentic.png`.

> Show exactly four stages from left to right in a row: ‘Review the plan’ → ‘Edit one file’ → ‘Inspect the diff’ → ‘Run an independent check’. Four icon cards connected by three rightward arrows. Human review is indicated by an eye icon on stages 1 and 3. There are no loopback arrows or subtitles. Scientific educational diagram for an MQB university lecture or textbook, landscape. Use a restrained two-dimensional diagram on almost-white paper, navy type, deep teal and muted ochre accents, clear lines, spacious margins and large readable sentence-case labels. No extra text, branding, logos, product screenshots or title. Keep the figure sparse. Use the reference for its teaching concept; make the new structure and exact wording below.

### agent-review

Source files supplied to ImageGen: `img/agentic.png`, `img/open_code.png`.

> Draw a schematic, not a software screenshot. Three separate panels labelled ‘Allowed edit’, ‘Protected inputs’, and ‘Independent check’. Allowed edit is a single code page with a plus line. Protected inputs are a small table and a lock, visually separated. Independent check is a checklist with a magnifier; no claim that it passed. Use only the three specified labels. Scientific educational diagram for an MQB university lecture or textbook, landscape. Use a restrained two-dimensional diagram on almost-white paper, navy type, deep teal and muted ochre accents, clear lines, spacious margins and large readable sentence-case labels. No extra text, branding, logos, product screenshots or title. Keep the figure sparse. Use the reference for its teaching concept; make the new structure and exact wording below.

### delegation

Source files supplied to ImageGen: `img/scenarios.png`, `img/scenarios_summary.png`.

> Create three equal columns labelled exactly ‘Chat’, ‘Editor assistance’, ‘Agent’. Beneath each draw a simple icon and use exactly one line below the icon respectively ‘Read the reply’, ‘Inspect the suggestion’, ‘Review the diff and actions’. A chat bubble, a code line with magnifier, and connected file-and-command symbols. No arrows comparing speed or risk and no ranking symbols. Scientific educational diagram for an MQB university lecture or textbook, landscape. Use a restrained two-dimensional diagram on almost-white paper, navy type, deep teal and muted ochre accents, clear lines, spacious margins and large readable sentence-case labels. No extra text, branding, logos, product screenshots or title. Keep the figure sparse. Use the reference for its teaching concept; make the new structure and exact wording below.

### risk

Source files supplied to ImageGen: `img/risk-domains.png`.

> Create a Venn diagram with three visibly overlapping circles using transparent light teal, warm yellow and slate blue. Use only these three large labels ‘Research integrity’, ‘Confidentiality’, ‘Security’, placed inside their own circle outside the central intersection. Put a small simple check mark, lock and shield beside the corresponding labels. Do not put words, marks or data in the overlap. Scientific educational diagram for an MQB university lecture or textbook, landscape. Use a restrained two-dimensional diagram on almost-white paper, navy type, deep teal and muted ochre accents, clear lines, spacious margins and large readable sentence-case labels. No extra text, branding, logos, product screenshots or title. Keep the figure sparse. Use the reference for its teaching concept; make the new structure and exact wording below.

### context-window

Source files supplied to ImageGen: `llm_context_windows_2026.png`.

> Redraw the teaching idea as four consecutive labelled sections inside one outlined wide container. Labels from left to right are ‘Instructions’, ‘Files’, ‘Conversation’, ‘Tool results’. Use a visible empty margin to imply room can run out, but no numbers, sizes, model names, product logos or scale. Add a single small heading above the container reading ‘Context available for this request’. Scientific educational diagram for an MQB university lecture or textbook, landscape. Use a restrained two-dimensional diagram on almost-white paper, navy type, deep teal and muted ochre accents, clear lines, spacious margins and large readable sentence-case labels. No extra text, branding, logos, product screenshots or title. Keep the figure sparse. Use the reference for its teaching concept; make the new structure and exact wording below.

### notebook-cells

Source files supplied to ImageGen: `img/JupyterInterface.png`.

> Draw a generic conceptual notebook page, with exactly three stacked blocks. Label first ‘Markdown cell’ with short example ‘Which watches contribute time?’. Label next ‘Code cell’ with exact expression ‘3 / 15’. Label last ‘Output’ with exact value ‘0.2’. Next to each label use a subtle icon. Make this an explanatory diagram with no menus or trademark. Scientific educational diagram for an MQB university lecture or textbook, landscape. Use a restrained two-dimensional diagram on almost-white paper, navy type, deep teal and muted ochre accents, clear lines, spacious margins and large readable sentence-case labels. No extra text, branding, logos, product screenshots or title. Keep the figure sparse. Use the reference for its teaching concept; make the new structure and exact wording below.
