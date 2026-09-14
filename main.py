import sys
import os
from pathlib import Path

# Add project root directory to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import argparse
import cv2
from src.stereo_reconstruction.engine import Stereo3DEngine
from src.motion_analytics.flow_tracker import MotionTracker

def main():
    parser = argparse.ArgumentParser(description="Vision3D-Recon CLI Tool")
    parser.add_argument("--mode", choices=["stereo", "motion"], required=True, help="Execution mode")
    parser.add_argument("--left", type=str, help="Left stereo image path")
    parser.add_argument("--right", type=str, help="Right stereo image path")
    parser.add_argument("--video", type=str, help="Input video path for motion analysis")
    parser.add_argument("--output", type=str, required=True, help="Output destination file path")

    args = parser.parse_args()

    if args.mode == "stereo":
        if not args.left or not args.right:
            print("[ERROR] Both --left and --right flags are required for stereo mode.")
            return

        if not os.path.exists(args.left):
            print(f"[ERROR] File not found: {args.left}")
            return
            
        if not os.path.exists(args.right):
            print(f"[ERROR] File not found: {args.right}")
            return

        img_l = cv2.imread(args.left)
        img_r = cv2.imread(args.right)

        engine = Stereo3DEngine()
        disp = engine.compute_disparity(img_l, img_r)
        
        # Ensure target directory exists
        os.makedirs(os.path.dirname(args.output), exist_ok=True)
        engine.generate_point_cloud(img_l, disp, args.output)

    elif args.mode == "motion":
        if not args.video:
            print("[ERROR] --video flag is required for motion mode.")
            return

        if not os.path.exists(args.video):
            print(f"[ERROR] Video file not found: {args.video}")
            return

        tracker = MotionTracker()
        tracker.process_video(args.video, args.output)

if __name__ == "__main__":
    main()