import pandas as pd

def render_block(csv_path):
    df = pd.read_csv(csv_path)
    html = ["<div class='overflow-auto mb-8'><table class='min-w-full border text-sm'>"]
    html.append("<thead><tr>" + "".join(f"<th class='bg-gray-100 border px-3 py-2'>{col}</th>" for col in df.columns) + "</tr></thead>")
    html.append("<tbody>")
    for _, row in df.iterrows():
        html.append("<tr>" + "".join(f"<td class='border px-3 py-2'>{row[col]}</td>" for col in df.columns) + "</tr>")
    html.append("</tbody></table></div>")
    return "\n".join(html)