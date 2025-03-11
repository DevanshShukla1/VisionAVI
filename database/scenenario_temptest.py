import cv2
import random
from datetime import datetime, timedelta

class ScenarioTemp:
    def __init__(self, input_source):
        """
        Initialize the ScenarioTemp class.
        :param input_source: Path to an image, video, or RTSP stream URL.
        """
        self.input_source = input_source

        # Determine input type
        if input_source.lower().startswith("rtsp"):
            self.input_type = "rtsp"
        elif input_source.lower().endswith(".mp4"):
            self.input_type = "video"
        elif input_source.lower().endswith(('.jpg', '.jpeg', '.png')):
            self.input_type = "image"
        else:
            raise ValueError("Unsupported input source type.")

    def process_frames(self):
        """
        Process frames based on the input type.
        For each frame, generate dummy scene metadata, predictions, and scene description.
        """
        if self.input_type == "image":
            frame = cv2.imread(self.input_source)
            if frame is None:
                raise ValueError("Failed to load image.")
            self._process_single_frame(frame)

        elif self.input_type in ["video", "rtsp"]:
            cap = cv2.VideoCapture(self.input_source)
            if not cap.isOpened():
                raise ValueError("Failed to open video source.")

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                self._process_single_frame(frame)
            cap.release()

    def _process_single_frame(self, frame):
        """
        Process a single frame: generate and print dummy scene data, predictions, and scene description.
        """
        # 1. Capture & Metadata Extraction
        scene_data = self.generate_dummy_scene_data()
        print("Capture & Metadata Extraction:")
        print(f"  A wearable camera captures a frame at {scene_data['timestamp']} with a resolution of {scene_data['resolution']} from {scene_data['camera_id']}.")
        print(f"  Media Path: {scene_data['media_path']}")
        print(f"  Location: Latitude {scene_data['latitude']}, Longitude {scene_data['longitude']}\n")

        # 2. Object Detection with YOLO
        detections = self.dummy_predict(frame)
        print("Object Detection with YOLO:")
        for d in detections:
            print(f"  Detected {d['class']} with confidence {d['confidence']} and bounding box {d['bbox']}")
        print()

        # 3. Scene Description Generation
        description_data = self.generate_dummy_scene_description(detections)
        print("Scene Description Generation:")
        print(f"  {description_data['description']}")
        print(f"  Confidence: {description_data['confidence']}, Model Version: {description_data['model_version']}\n")

    def dummy_predict(self, frame):
        """
        Simulate YOLO model output by returning two fixed predictions.
        :param frame: A single frame to process.
        :return: A list of predictions with keys 'class', 'confidence', and 'bbox'
        """
        detection1 = {"class": "person", "confidence": 0.95, "bbox": [100, 150, 300, 450]}
        detection2 = {"class": "car", "confidence": 0.88, "bbox": [400, 200, 600, 500]}
        return [detection1, detection2]

    def generate_dummy_scene_data(self):
        """
        Generate dummy scene metadata that mimics the columns in the scenes table.
        Returns a dictionary with keys:
          - timestamp, latitude, longitude, resolution, camera_id, media_path, processed
        """
        # Use fixed values as per the example
        return {
            "timestamp": "2024-03-07T12:34:56",
            "latitude": 40.7128,
            "longitude": -74.0060,
            "resolution": "1920x1080",
            "camera_id": "CAM_001",
            "media_path": "/data/scenes/scene_001.jpg",
            "processed": 0
        }

    def generate_dummy_scene_description(self, detections):
        """
        Generate dummy scene description based on detections.
        Returns a dictionary with keys:
          - description, confidence, model_version
        """
        # For demonstration, we assume a fixed description based on the example
        return {
            "description": "A person is near a parked car.",
            "confidence": 0.90,
            "model_version": "v1.0"
        }

if __name__ == "__main__":
    # Example usage: change the input path to an existing video or image file on your system.
    input_path = "D:/Devansh/Computer vision course/Project/new1.mp4"
    scenario = ScenarioTemp(input_path)
    scenario.process_frames()
