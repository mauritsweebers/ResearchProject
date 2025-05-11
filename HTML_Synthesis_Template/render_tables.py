import pandas as pd
from pathlib import Path

def render_table_from_csv(csv_path):
    df = pd.read_csv(csv_path)
    html = [f"<h3 class='text-lg font-semibold mt-6 mb-2'>{csv_path.stem}</h3>"]
    html.append("<div class='overflow-auto mb-6'><table class='min-w-full border-collapse text-sm'>")
    html.append("<thead><tr>" + "".join(f"<th class='bg-gray-100 border px-3 py-2'>{col}</th>" for col in df.columns) + "</tr></thead>")
    html.append("<tbody>")
    for _, row in df.iterrows():
        html.append("<tr>" + "".join(f"<td class='border px-3 py-2'>{val}</td>" for val in row) + "</tr>")
    html.append("</tbody></table></div>")
    return "\n".join(html)

def render_block(directory):
    out = []
    for file in sorted(Path(directory).glob("*_DT*.csv")):
        out.append(render_table_from_csv(file))
    return "\n".join(out)