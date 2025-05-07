
""" 
Reusable HTML rendering logic for Phase synthesis outputs 
Includes:
- Paragraph and list parsing
- Dark/light mode toggle
- Table rendering
- Figure embedding
- Source list inclusion
"""

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

        # Bullet list with optional source line
        if all(line.strip().startswith("- ") or re.match(r'^\(Source:', line.strip()) for line in lines):
            html_parts.append("<ul class='list-disc list-inside pl-6 mb-4'>")
            for line in lines:
                if line.strip().startswith("- "):
                    html_parts.append(f"<li>{line.strip()[2:].strip()}</li>")
                else:
                    html_parts.append(f"<li class='text-sm italic'>{line.strip()}</li>")
            html_parts.append("</ul>")
        # Numbered list with optional source line
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
