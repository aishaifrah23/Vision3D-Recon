import cv2
import numpy as np

def export_ply(disparity: np.ndarray, img: np.ndarray, output_path: str, Q: np.ndarray = None):
    if Q is None:
        h, w = disparity.shape
        Q = np.float32([[1, 0, 0, -0.5*w], [0, -1, 0, 0.5*h], [0, 0, 0, -0.8*w], [0, 0, 1/0.8, 0]])
    
    points = cv2.reprojectImageTo3D(disparity, Q)
    colors = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    mask = disparity > disparity.min()
    out_points = points[mask]
    out_colors = colors[mask]
    
    verts = np.hstack([out_points, out_colors])
    header = f"ply\nformat ascii 1.0\nelement vertex {len(verts)}\nproperty float x\nproperty float y\nproperty float z\nproperty uchar red\nproperty uchar green\nproperty uchar blue\nend_header\n"
    
    with open(output_path, 'w') as f:
        f.write(header)
        np.savetxt(f, verts, fmt="%f %f %f %d %d %d")