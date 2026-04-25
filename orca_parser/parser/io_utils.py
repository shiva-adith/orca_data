import re
from pathlib import Path
from typing import Optional

from setuptools._distutils.command import install_lib


def read_text_file(path: Path) -> str:
    return path.read_text(errors="ignore")

def safe_to_float(value: Optional[str]) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value.replace("D", "E"))
    except Exception:
        return None

def safe_to_int(value: Optional[str]) -> Optional[int]:
    if value is None:
        return None
    try:
        return int(value)
    except Exception:
        return None

def first_match_float(text: str, pattern: str, flags: int=0) -> Optional[float]:
    match = re.search(pattern, text, flags)
    if not match:
        return None
    return safe_to_float(match.group(1))

def first_match_int(text: str, pattern: str, flags: int=0) -> Optional[int]:
    match = re.search(pattern, text, flags)
    if not match:
        return None
    # The first parenthesized subgroup.
    return safe_to_int(match.group(1))

def count_pattern(text: str, pattern: str, flags: int=0) -> int:
    return len(re.findall(pattern, text, flags))

def extract_text_block(text: str, start_pattern: str, end_pattern: str, flags: int=re.S) -> Optional[str]:
    start_match = re.search(start_pattern, text, flags)
    if not start_match:
        return None

    start_index = start_match.end()
    remainder = text[start_index:]

    end_match = re.search(end_pattern, remainder, flags)
    if not end_match:
        return remainder

    end_index = end_match.start()
    return remainder[:end_index]
