import re
import sys
from pathlib import Path
from typing import Optional

sys.path.append("../orca_parser")
from orca_parser.config import HARTREE_TO_KJMOL
from text_patterns import GENERAL_PATTERNS
from io_utils import first_match_float, extract_text_block

def infer_complex_name(file_path: Path) -> str:
    for part in reversed(file_path.parts[:-1]):
        lowered = part.lower()
        if lowered.startswith(("comp", "complex", "cluster")):
            return part
    return file_path.stem