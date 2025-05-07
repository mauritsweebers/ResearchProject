
""" 
Full HTML rendering pipeline for Phase outputs
Includes:
- Text synthesis rendering with list logic
- Table previews using pandas
- Figure embedding by SSOT path
- Light/dark mode toggle and Tailwind styling
"""

import os
import re
import pandas as pd

def transform_txt_to_html_with_fixed_lists(txt):
    blocks = re.split(r'\n\s*\n', txt.strip())
    html_parts = []
    for block in blocks:
        lines = block.strip().splitlines()
        if not lines:
            continue
        if lines[0].startswith("## "):
            html_parts.append(f"<h3 class='text-lg font-semibold mt-6 mb-2'>{lines[0][3:].strip()}</h3>")
            lines = lines[1:]
        if all(line.strip().startswith("- ") or re.match(r'^\(Source:', line.strip()) for line in lines):
            html_parts.append("<ul class='list-disc list-inside pl-6 mb-4'>")
            for line in lines:
                if line.strip().startswith("- "):
                    html_parts.append(f"<li>{line.strip()[2:].strip()}</li>")
                else:
                    html_parts.append(f"<li class='text-sm italic'>{line.strip()}</li>")
            html_parts.append("</ul>")
        elif all(re.match(r"^\d+[.)]\s+", line.strip()) or re.match(r'^\(Source:', line.strip()) for line in lines):
            html_parts.append("<ol class='list-decimal list-inside pl-6 mb-4'>")
            for line in lines:
                if re.match(r"^\d+[.)]\s+", line.strip()):
                    content = re.sub(r"^\d+[.)]\s+", "", line.strip())
                    html_parts.append(f"<li>{content}</li>")
                else:
                    html_parts.append(f"<li class='text-sm italic'>{line.strip()}</li>")
            html_parts.append("</ol>")
        else:
            joined = "<br>".join(line.strip() for line in lines)
            html_parts.append(f"<p class='mb-4'>{joined}</p>")
    return "\n".join(html_parts)

def load_table_preview(file_path, max_rows=5):
    try:
        df = pd.read_csv(file_path)
        return df.head(max_rows)
    except Exception as e:
        return f"[Error loading table: {e}]"

def wrap_full_html(content_blocks, source_list, title="Phase Output"):
    body = f'''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
  <style>
    .theme-toggle {{
        position: fixed; top: 30px; right: 30px; z-index: 999;
    }}
    html.dark body {{
        background-color: #1a1a1a; color: #e0e0e0;
    }}
    html.dark h1, html.dark h2, html.dark h3, html.dark p, html.dark li {{
        color: #e0e0e0;
    }}
    html.dark table {{
        background-color: #2a2a2a; border-color: #444;
    }}
    html.dark th {{
        background-color: #333; color: #f0f0f0;
    }}
    html.dark td {{
        background-color: #2a2a2a; color: #e0e0e0;
    }}
  </style>
  <script>
    function toggleTheme() {{
        const html = document.documentElement;
        const isDark = html.classList.toggle('dark');
        document.getElementById('theme-toggle').textContent = isDark ? 'light mode' : 'dark mode';
    }}
  </script>
</head>
<body class="bg-white text-gray-900 font-sans transition-colors duration-300">
  <div class="max-w-screen-lg mx-auto px-4 py-8">
    <button id="theme-toggle" class="theme-toggle px-4 py-2 bg-gray-200 text-gray-800 rounded shadow" onclick="toggleTheme()">dark mode</button>
    <h1 class="text-4xl font-bold mb-4">{title}</h1>
    <p class="text-lg text-gray-700 mb-8">Synthesis output with full text, tables, dark/light theme, and sources.</p>
    {''.join(content_blocks)}
    <h2 class='text-2xl font-semibold mt-10 mb-4'>Appendix – Source References</h2>
    <ul class='list-disc list-inside pl-6 mb-8'>
      {''.join([f"<li><strong>{src['Source Name']}</strong> ({src['Type']}) – <a href='{src['Link or DOI']}' class='text-blue-600 underline'>{src['Link or DOI']}</a></li>" for src in source_list])}
    </ul>
  </div>
</body>
</html>'''
    return body
