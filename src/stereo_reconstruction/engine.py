import cv2
import numpy as np

class Stereo3DEngine:
    def __init__(self, focal_length=700.0, baseline=0.1):
        self.f = focal_length
        self.b = baseline

    def compute_disparity(self, img_left, img_right):
        gray_l = cv2.cvtColor(img_left, cv2.COLOR_BGR2GRAY)
        gray_r = cv2.cvtColor(img_right, cv2.COLOR_BGR2GRAY)
        
        stereo = cv2.StereoSGBM_create(
            minDisparity=0,
            numDisparities=64,
            blockSize=11,
            P1=8 * 3 * 11**2,
            P2=32 * 3 * 11**2,
            disp12MaxDiff=1,
            uniquenessRatio=10,
            speckleWindowSize=100,
            speckleRange=32
        )
        disparity = stereo.compute(gray_l, gray_r).astype(np.float32) / 16.0
        return disparity

    def generate_point_cloud(self, img_left, disparity, output_path):
        h, w = disparity.shape
        cx, cy = w / 2.0, h / 2.0
        
        Q = np.float32([
            [1, 0, 0, -cx],
            [0, -1, 0, cy],
            [0, 0, 0, self.f],
            [0, 0, -1/self.b, 0]
        ])
        
        points_3D = cv2.reprojectImageTo3D(disparity, Q)
        colors = cv2.cvtColor(img_left, cv2.COLOR_BGR2RGB)
        
        mask = disparity > disparity.min()
        out_points = points_3D[mask]
        out_colors = colors[mask]

        with open(output_path, 'w') as f:
            f.write("ply\nformat ascii 1.0\n")
            f.write(f"element vertex {len(out_points)}\n")
            f.write("property float x\nproperty float y\nproperty float z\n")
            f.write("property uchar red\nproperty uchar green\nproperty uchar blue\n")
            f.write("end_header\n")
            for pt, clr in zip(out_points, out_colors):
                f.write(f"{pt[0]:.4f} {pt[1]:.4f} {pt[2]:.4f} {clr[0]} {clr[1]} {clr[2]}\n")

        print(f"[SUCCESS] Point cloud saved to: {output_path}")