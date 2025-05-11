from pathlib import Path

def render_metadata_block(index_code, file_name, file_type, description, source_class, notes):
    return f'''
    <div class="metadata-block border rounded p-4 my-4 shadow">
        <h3 class="text-xl font-semibold mb-1">{index_code} <span class="text-sm text-gray-400">({file_type})</span></h3>
        <p class="text-sm"><strong>File:</strong> {file_name}</p>
        <p class="text-sm"><strong>Title:</strong> {description}</p>
        <p class="text-sm"><strong>Source:</strong> <span class="font-semibold'>{source_class}</span></p>
        <p class="text-sm italic">{notes}</p>
    </div>
    '''

def render_block(directory):
    blocks = []
    for file in sorted(Path(directory).glob("*_META.txt")):
        with open(file, 'r', encoding='utf-8') as f:
            lines = [l.strip() for l in f if l.strip()]
            if len(lines) >= 6:
                blocks.append(render_metadata_block(*lines[:6]))
    if blocks:
        return "<h2 class='text-2xl font-semibold mt-10 mb-4'>📂 Module Metadata</h2>\n" + "\n".join(blocks)
    return ""