# Vision3D-Recon

Stereo 3D reconstruction + dense optical flow tracking, wrapped in a single CLI.

I built this to play around with classic stereo vision techniques — no deep learning,
just OpenCV's block matching and Farneback flow, done properly. Give it a calibrated
stereo pair and it'll spit out a colored point cloud. Give it a video and it'll track
pixel motion frame to frame and render that as a flow visualization.

## What it does

- **Stereo depth**: StereoSGBM computes a disparity map from left/right image pairs,
  which gets reprojected into 3D (X, Y, Z) points and exported as an ASCII `.ply`.
- **Motion tracking**: Farneback dense optical flow over a video, exported as an
  annotated MP4 showing per-pixel velocity.

Two pipelines, one entry point (`main.py`), picked via `--mode`.

## Project layout
```
Vision3D-Recon/
├── data/
│   ├── raw_stereo/                  # input stereo images and sample videos
│   └── output/                      # generated .ply and .mp4 files land here
├── src/
│   ├── stereo_reconstruction/
│   │   ├── __init__.py
│   │   └── engine.py                # disparity computation + point cloud export
│   └── motion_analytics/
│       ├── __init__.py
│       └── flow_tracker.py          # optical flow processing
├── main.py                          # CLI entry point
├── requirements.txt
├── statement.md
├── .gitignore
└── README.md
```

## Setup

Needs Python 3.8+.

```bash
git clone https://github.com/YOUR_USERNAME/Vision3D-Recon.git
cd Vision3D-Recon
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows PowerShell
pip install -r requirements.txt
```

## Usage

**Stereo reconstruction** — takes a left/right pair, outputs a point cloud:

```bash
python main.py --mode stereo --left data/raw_stereo/left.png --right data/raw_stereo/right.png --output data/output/cloud.ply
```

**Motion analytics** — takes a video, outputs a flow visualization:

```bash
python main.py --mode motion --video data/raw_stereo/sample_motion.mp4 --output data/output/motion_flow.mp4
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
