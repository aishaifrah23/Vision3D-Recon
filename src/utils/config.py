import os
from dataclasses import dataclass

@dataclass
class StereoConfig:
    min_disparity: int = 0
    num_disparities: int = 16 * 5
    block_size: int = 15
    p1: int = 8 * 3 * 15**2
    p2: int = 32 * 3 * 15**2

def validate_path(path_str: str) -> str:
    if not path_str:
        raise FileNotFoundError("No input path provided.")
    # Allow numeric camera index strings like "0"
    if path_str.isdigit():
        return path_str
    if not os.path.exists(path_str):
        raise FileNotFoundError(f"Input path not found: {path_str}")
    return path_str