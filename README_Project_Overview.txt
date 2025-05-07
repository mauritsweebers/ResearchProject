# 🌍 Global Plant-Based Food System Research – Project Overview

## 📘 Purpose
This project investigates whether a nutritionally complete and ecologically sustainable global food system based entirely on plant-based diets is possible. Research is structured across multiple evidence-based Phases, each guided by protocols, institutional sources, and standardized workflows.

---

## 🧭 Project Structure

### 🔁 Phases
Research progresses through 9 structured phases:
- Phase 0: Current Food System Analysis ✅
- Phase 1: Nutritional Viability
- Phase 2: Agricultural Feasibility
- Phase 3: Environmental Impact
- Phase 4: Economic & Supply Chain Viability
- Phase 5: Cultural and Political Realities
- Phase 6: Transition Mechanisms
- Phase 7: Critique and Robustness Testing
- Phase 8: Synthesis and Scenario Modeling

Each Phase contains multiple Modules (e.g., M1, M2...) that handle discrete topics.

---

## 🗂️ File Structure (SSOT)

```
/ssot/
  └─ phaseX/
       └─ moduleY/
            ├─ data/        ← Raw CSV data files (DT)
            ├─ outputs/     ← Text outputs (TX), Figures (FG), Final syntheses
            ├─ logs/        ← Notes, QA results, actions
            └─ references/  ← Archived PDFs, source lists (optional)
```

**Key Conventions:**
- File names start with index codes: `P0.M1.DT01`, `P0.M2.TX01`, etc.
- Source quality is tracked using 🟢 (peer-reviewed), 🟡 (institutional), 🔴 (unverified).

---

## 🧑‍💻 Output Protocols

### ✅ HTML Report Protocol
Used to generate final synthesis reports with:
- Tailwind CSS for layout and styling
- Light/dark mode toggle button (top-right)
- Properly rendered `<p>`, `<ul>`, `<ol>`, `<table>`, `<img>` elements
- All text and visuals embedded in a responsive layout
- Reference list included as an appendix

📎 See: `HTML_Output_Protocol.txt`

---

## 🧪 Research Integrity Guidelines

- **Only peer-reviewed or institutional data is permitted in evidentiary arguments.**
- Framing content (Wikipedia, OWID) may be referenced for orientation but clearly marked.
- All outputs are stored and version-controlled in `ssot/`.
- Text, table, and figure outputs must follow naming and metadata conventions.

---

## 🔄 Phase Completion Workflow

Each phase is completed in these steps:
1. All modules finalized
2. Local sync check (upload current SSOT folder)
3. QA audit of all outputs
4. Correction & prompt cycle (if needed)
5. Render final HTML synthesis with dark/light mode
6. Archive, review, and submit for lock

---

## 📩 Getting Started as a New Contributor

1. Review the README and HTML protocol file
2. Explore `/ssot/phase0/` to understand how data and outputs are structured
3. Confirm you have access to all project folders
4. Join the correct Phase chat and await commands from project leadership

---

## 👨‍✈️ Governance

This project is led by a directive command structure. You are not expected to operate independently unless instructed. Output consistency, source rigor, and protocol adherence are strictly maintained.