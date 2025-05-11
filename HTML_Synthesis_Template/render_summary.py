from pathlib import Path
import re

def render_block(directory):
    blocks = []
    summary_path = directory / f"{directory.name.capitalize()}_Summary.txt"

    if not summary_path.exists():
        return ""

    with open(summary_path, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
        buffer = []
        mode = None  # 'ul', 'ol', or 'p'

        def flush_buffer():
            nonlocal buffer, mode
            if not buffer:
                return
            if mode == 'ul':
                items = "".join(f"<li>{line[2:].strip()}</li>" for line in buffer)
                blocks.append(f"<ul class='list-disc list-inside mb-4'>{items}</ul>")
            elif mode == 'ol':
                items = []
                for line in buffer:
                    clean = re.sub(r"^\d+\.\s+", "", line).strip()
                    items.append(f"<li>{clean}</li>")
                blocks.append(f"<ol class='list-decimal list-inside mb-4'>{''.join(items)}</ol>")
            else:
                blocks.append(f"<p class='mb-4'>{'<br>'.join(buffer)}</p>")
            buffer = []
            mode = None

        for line in lines:
            line = line.strip()
            if not line:
                flush_buffer()
                continue
            if re.match(r"^##\s", line):
                flush_buffer()
                blocks.append(f"<h3 class='text-xl font-semibold mt-6 mb-2'>{line[3:].strip()}</h3>")
            elif line.startswith("- "):
                if mode not in ('ul', None):
                    flush_buffer()
                mode = 'ul'
                buffer.append(line)
            elif re.match(r"^\d+\.\s", line):
                if mode not in ('ol', None):
                    flush_buffer()
                mode = 'ol'
                buffer.append(line)
            else:
                if mode not in (None, 'p'):
                    flush_buffer()
                mode = 'p'
                buffer.append(line)

        flush_buffer()
    return "\n".join(blocks)
