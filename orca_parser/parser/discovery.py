from pathlib import Path
from typing import Optional

def discover_files(root_dir: Path, optional_glob: Optional[str] = None) -> dict:
    out_files = []
    xyz_files = []
    trj_files = []

    for path in root_dir.rglob("*"):
        if not path.is_file():
            continue

        name = path.name

        if optional_glob is not None:
            # placeholder
            if optional_glob not in name:
                continue

        if name.endswith(".trj.xyz"):
            trj_files.append(path)
        elif name.endswith(".xyz"):
            xyz_files.append(path)
        elif name.endswith(".out"):
            out_files.append(path)

    return {
        "out_files": sorted(out_files),
        "xyz_files": sorted(xyz_files),
        "trj_files": sorted(trj_files)
    }