# PhaseBuilderHtml.py — injects phase overview from Research_Phases_Template.csv

import os
import datetime
import importlib.util
from pathlib import Path
import pandas as pd

def load_renderer(name):
    path = RENDERER_DIR / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def get_phase_overview_html(phase_id):
    csv_path = Path("./SSOT/setup/Research_Phases_Template.csv")
    df = pd.read_csv(csv_path, sep=";")
    df["Phase"] = df["Phase"].str.lower()
    df.set_index("Phase", inplace=True)
    if phase_id not in df.index:
        return ""
    row = df.loc[phase_id]
    #phase_name = phase_id.row['Title'].strip()
    phase_name = f"{phase_id} {df.loc[phase_id, 'Title'].strip()}"

    html = ['<h2 class="text-2xl font-semibold mt-10 mb-4">🧭 Phase Overview</h2>']
    html.append(f"<div class='metadata-block border rounded p-4 my-4 shadow'>")
    html.append(f"<p class='mb-4'><strong>Title:</strong> {row['Title'].strip()}</p>")
    html.append(f"<p class='mb-4'><strong>Objectives:</strong> {row['Objectives'].strip()}</p>")
    html.append(f"<p class='mb-4'><strong>Inputs:</strong> {row['Inputs'].strip()}</p>")
    html.append(f"<p class='mb-4'><strong>Outputs:</strong> {row['Outputs'].strip()}</p>")
    html.append(f"</div>")
    #return "\n".join(html)
    return "\n".join(html), phase_name

def build_phase(phase_id):
    phase_dir = SSOT_BASE / phase_id
    output_file = f"{phase_id}_output.html"

    render_summary = load_renderer("render_summary")
    render_metadata = load_renderer("render_metadata")
    render_narrative = load_renderer("render_narrative")
    render_figures = load_renderer("render_figures")
    render_tables = load_renderer("render_tables")
    render_sources = load_renderer("render_sources_table")

    html_blocks = []

     # Inject overview and get the title
    overview_html, phase_name = get_phase_overview_html(phase_id)
    html_blocks.append(overview_html)

    # Inject overview and summary
    #html_blocks.append(get_phase_overview_html(phase_id))

    html_blocks.append(render_summary.render_block(phase_dir))

    for mod_dir in sorted((phase_dir).glob("module*")):
        module_num = mod_dir.name.replace("module", "")
        html_blocks.append(f"<h2 class='text-2xl font-semibold mt-10 mb-4'>Module {module_num}</h2>")

        outputs = mod_dir / "outputs"
        if outputs.exists():
            html_blocks.append(render_metadata.render_block(outputs))
            html_blocks.append(render_narrative.render_block(outputs))
            html_blocks.append(render_tables.render_block(outputs))
            html_blocks.append(render_figures.render_block(outputs))

        data = mod_dir / "data"
        if data.exists():
            html_blocks.append(render_tables.render_block(data))
            html_blocks.append(render_figures.render_block(data))

    html_blocks.append("<h2 class='text-2xl font-semibold mt-10 mb-4'>Appendix – Source References</h2>")
    html_blocks.append(render_sources.render_block(SSOT_BASE / "Master_Index_Register.csv"))

    theme = THEME_FILE.read_text(encoding="utf-8")
    rendered_html = theme.replace("{title}", phase_name).replace("{content}", "\n".join(html_blocks))

    out_path = OUTPUT_DIR / output_file
    out_path.write_text(rendered_html, encoding="utf-8")
    print(f"✅ Output: {out_path.resolve()}")

# ==== Entry point ====
import argparse

parser = argparse.ArgumentParser(description="Build phaseX HTML synthesis using SSOT")
parser.add_argument("--phase", required=True, help="Phase ID (e.g. phase0, phase1)")
args = parser.parse_args()

PHASE = args.phase.lower()
RENDERER_DIR = Path("./HTML_Synthesis_Template")
SSOT_BASE = Path("./SSOT")
OUTPUT_DIR = Path("./docs")
THEME_FILE = RENDERER_DIR / "theme.html"
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

build_phase(PHASE)