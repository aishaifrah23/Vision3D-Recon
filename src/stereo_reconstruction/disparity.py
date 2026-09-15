import cv2
import numpy as np
from src.utils.config import StereoConfig

class DisparityEstimator:
    def __init__(self, config: StereoConfig = StereoConfig()):
        self.matcher = cv2.StereoSGBM_create(
            minDisparity=config.min_disparity,
            numDisparities=config.num_disparities,
            blockSize=config.block_size,
            P1=config.p1,
            P2=config.p2
        )

    def compute(self, img_left: np.ndarray, img_right: np.ndarray) -> np.ndarray:
        gray_l = cv2.cvtColor(img_left, cv2.COLOR_BGR2GRAY)
        gray_r = cv2.cvtColor(img_right, cv2.COLOR_BGR2GRAY)
        return self.matcher.compute(gray_l, gray_r).astype(np.float32) / 16.0