import cv2
import numpy as np

class MotionTracker:
    def process_video(self, video_path, output_path):
        cap = cv2.VideoCapture(video_path)
        ret, first_frame = cap.read()
        if not ret:
            print("[ERROR] Could not read video file.")
            return

        prev_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
        hsv = np.zeros_like(first_frame)
        hsv[..., 1] = 255

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, 30.0, (first_frame.shape[1], first_frame.shape[0]))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
            
            mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
            hsv[..., 0] = ang * 180 / np.pi / 2
            hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
            bgr_flow = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
            
            out.write(bgr_flow)
            prev_gray = gray

        cap.release()
        out.release()
        print(f"[SUCCESS] Motion analysis video saved to: {output_path}")