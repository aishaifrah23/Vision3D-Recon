# Vision3D-Recon

A modular Opencv toolkit designed for 3D stereo reconstruction and dense optical flow motion tracking. It allows users to turn image pairs into 3D point clouds and calculate real-time motion vectors from video files or live camera streams through a command-line interface.

## Features

* **3D Point Cloud Generation:** Uses OpenCVs algorithm to compute depth maps and then reprojects pixels into 3D space. The resulting filtered point clouds are saved in the.ply` format.

* **Dense Optical Flow:** Tracks motion one frame at a time using the Farneback algorithm. It maps velocity and direction directly into the HSV color space making motion visually clear.

* **Flexible Video/Camera Inputs:** Accepts both saved MP4 or AVI videos and live camera feeds. These inputs can be processed with command-line flags.

* **Modular Architecture:** Keeps CLI handling, parameter configuration algorithm logic and output writers clearly separated for maintenance and extension.

## Repository Structure

```

Vision3D-Recon/

├── main.py # Main script that runs stereo and motion modes via CLI

├── README.md # Instructions for setup and running the tool

├── statement.md # Overview of the project and the problem it solves

├── requirements.txt # List of required packages and dependencies

├── sample.mp4 # Sample input video

└── src/

├── __init__.py

├── utils/

│ ├── __init__.py

│ ├── cli_parser.py # Handles argument parsing for the command line

│ └── config.py # Manages stereo. Checks file paths

├── stereo_reconstruction/

│ ├── __init__.py

│ ├── disparity.py # Creates disparity maps using

│ └── ply_exporter.py # Converts pixels to 3D and saves them as PLY files

└── motion_analytics/

├── __init__.py

├── farneback.py # Calculates optical flow using the Farneback method

└── visualizer.py # Displays motion in HSV. Writes results, to MP4

```
## Setup

Needs Python 3.8+, OpenCV (opencv-python), NumPy.

```bash
1) Clone the repository:
git clone [https://github.com/aishaifrah23/Vision3D-Recon.git](https://github.com/aishaifrah23/Vision3D-Recon.git)
cd Vision3D-Recon
2) Create and activate a virtual environment:
python -m venv venv
.\venv\Scripts\activate   # Windows PowerShell
python3 -m venv venv
source venv/bin/activate # macOS / Linux
pip install -r requirements.txt
```

## Usage
All commands run through main.py

**Stereo reconstruction** — takes a left/right pair, outputs a point cloud:

```bash
python main.py --mode stereo --left data/raw_stereo/left.png --right data/raw_stereo/right.png --output data/output/cloud.ply
```

**Motion analytics** — takes a video, outputs a flow visualization:

```bash
python main.py --mode motion --video sample.mp4 --output motion_output.mp4
```
**Motion Tracking Mode (Webcam)**
Runs motion estimation on a live camera stream using camera index 0
```bash
python main.py --mode motion --video 0
```

### CLI flags

| Flag | Required for | What it is |
|---|---|---|
| `--mode` | both | `stereo` or `motion` |
| `--left` | stereo | left frame path |
| `--right` | stereo | right frame path |
| `--video` | motion | source video path |
| `--output` | both | where the result gets written (`.ply` or `.mp4`) |

## Viewing the output

`.ply` files open fine in MeshLab or CloudCompare — `File → Import Mesh`, then toggle
vertex coloring to see the texture mapped onto the surface.

## Dependencies

- opencv-python
- numpy

## License

MIT
