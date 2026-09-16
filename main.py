import cv2
from src.utils.cli_parser import parse_args
from src.utils.config import validate_path, StereoConfig
from src.stereo_reconstruction.disparity import DisparityEstimator
from src.stereo_reconstruction.ply_exporter import export_ply
from src.motion_analytics.farneback import compute_dense_flow
from src.motion_analytics.visualizer import flow_to_hsv, MotionVideoWriter

def main():
    args = parse_args()
    
    if args.mode == "stereo":
        validate_path(args.left)
        validate_path(args.right)
        img_l, img_r = cv2.imread(args.left), cv2.imread(args.right)
        estimator = DisparityEstimator(StereoConfig())
        disp = estimator.compute(img_l, img_r)
        export_ply(disp, img_l, args.output)
        
    elif args.mode == "motion":
        validate_path(args.video)
        video_src = int(args.video) if args.video.isdigit() else args.video
        cap = cv2.VideoCapture(video_src)
        
        fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        out_path = args.output if args.output.endswith(('.mp4', '.avi')) else "motion_output.mp4"
        writer = MotionVideoWriter(out_path, fps, (width, height))
        
        ret, prev = cap.read()
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            flow = compute_dense_flow(prev, frame)
            vis = flow_to_hsv(flow)
            
            writer.write(vis)
            cv2.imshow("Dense Optical Flow", vis)
            
            delay = max(1, int(1000 / fps))
            if cv2.waitKey(delay) & 0xFF == 27:
                break
            prev = frame
            
        cap.release()
        writer.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()