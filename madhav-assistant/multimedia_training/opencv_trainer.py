"""
OpenCV Trainer Module for Madhav Assistant

This module uses OpenCV for image/video processing and training data generation.
"""

import cv2
import os

class OpenCVTrainer:
    def __init__(self):
        pass

    def extract_frames(self, video_file: str, output_dir: str, frame_rate: int = 1) -> bool:
        """
        Extract frames from video at specified frame rate (frames per second).
        Saves frames as images in output_dir.
        """
        try:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            cap = cv2.VideoCapture(video_file)
            fps = cap.get(cv2.CAP_PROP_FPS)
            frame_interval = int(fps / frame_rate) if fps > 0 else 1
            count = 0
            saved_count = 0

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                if count % frame_interval == 0:
                    frame_path = os.path.join(output_dir, f"frame_{saved_count:05d}.jpg")
                    cv2.imwrite(frame_path, frame)
                    saved_count += 1
                count += 1

            cap.release()
            return True
        except Exception as e:
            print(f"OpenCV error: {e}")
            return False

# Example usage:
# trainer = OpenCVTrainer()
# success = trainer.extract_frames("input_video.mp4", "output_frames", frame_rate=1)
# if success:
#     print("Frames extracted successfully.")
# else:
#     print("Failed to extract frames.")
