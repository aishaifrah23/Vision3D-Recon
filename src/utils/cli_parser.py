import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Vision3D-Recon CLI")
    parser.add_argument("--mode", choices=["stereo", "motion"], required=True, help="Mode: stereo or motion")
    parser.add_argument("--left", type=str, help="Path to left stereo image")
    parser.add_argument("--right", type=str, help="Path to right stereo image")
    parser.add_argument("--video", type=str, help="Path to input video")
    parser.add_argument("--output", type=str, default="output.ply", help="Path for output files")
    return parser.parse_args()