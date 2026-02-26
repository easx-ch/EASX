import yaml
from pathlib import Path
import shutil

base_path = Path("docs")
if not base_path.exists():
    print(f"ERROR: Folder {base_path} does not exist")
    exit(1)

def process_order(folder: Path):
    nav = []
    order_file = folder / ".order"

    if order_file.exists():
        with order_file.open() as f:
            lines = [line.strip() for line in f if line.strip()]

        for i, line in enumerate(lines):
            file_path = folder / f"{line}.md" if not line.endswith(".md") else folder / line
            if not file_path.exists() or file_path.name.lower() == "404.md":
                continue
            title = Path(line).stem.replace("-", " ")
            rel_path = file_path.relative_to(base_path).as_posix()

            # First file becomes index.md too
            if folder == base_path and i == 0:
                shutil.copy(file_path, base_path / "index.md")
                nav.append({title: "index.md"})
            else:
                nav.append({title: rel_path})

    # Recursively process subfolders
    for subfolder in sorted(folder.iterdir()):
        if subfolder.is_dir():
            sub_nav = process_order(subfolder)
            if sub_nav:
                nav.append({subfolder.name.replace("-", " "): sub_nav})

    return nav

nav = process_order(base_path)

with open("mkdocs.base.yml") as f:
    config = yaml.safe_load(f)

config["docs_dir"] = str(base_path)
config["nav"] = nav

with open("mkdocs.yml", "w") as f:
    yaml.dump(config, f, sort_keys=False)

print("Nav generated successfully")