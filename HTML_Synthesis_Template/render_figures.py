from pathlib import Path

def render_block(directory):
    figs = []
    for svg_file in sorted(Path(directory).glob("*_FG*.svg")):
        rel_path = svg_file.as_posix()
        if "SSOT/" in rel_path:
            rel_path = rel_path.replace("SSOT/", "./")
        figs.append(f"<div class='mb-4'><img src='{rel_path}' alt='{svg_file.stem}' class='w-full max-w-lg mx-auto my-4'/></div>")
    return "\n".join(figs)