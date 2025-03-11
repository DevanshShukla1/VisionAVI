import cv2
import random
import numpy as np
#from ultralytics import YOLO

class scenario_temp:
    def __init__(self, input_source):
        """
        Initialize the scenario_temp class.
        :param input_source: Path to an image, video, or RTSP stream URL.
        """
        self.input_source = input_source
        #self.model = YOLO("yolov5nu.pt")

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
        Process frames based on the input type and perform predictions.
        """
        if self.input_type == "image":
            frame = cv2.imread(self.input_source)
            if frame is None:
                raise ValueError("Failed to load image.")
            prediction = self.dummy_predict(frame)
            print(f"Prediction: {prediction}")

        elif self.input_type in ["video", "rtsp"]:
            cap = cv2.VideoCapture(self.input_source)
            if not cap.isOpened():
                raise ValueError("Failed to open video source.")

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                prediction = self.dummy_predict(frame)
                print(f"Prediction: {prediction}")

            cap.release()

    def dummy_predict(self, frame):
        #predictions = []
        """
        Simulate YOLO model output by returning a single random prediction.
        :param frame: A single frame to process.
        :return: A single random prediction (x, y, w, h, class_id)
        """
        height, width, _ = frame.shape
        x = random.randint(0, width)
        y = random.randint(0, height)
        w = random.randint(10, width // 5)
        h = random.randint(10, height // 5)
        class_id = random.randint(0, 7)  # Assuming dataset (80 classes)

        prediction = (x, y, w, h, class_id)
        #predictions.append(prediction)
        return prediction

if __name__ == "__main__":
    input_path = "D:/Devansh/Computer vision course/Project/new1.mp4"
    scenario = scenario_temp(input_path)
    scenario.process_frames()



# #Other code

# import cv2
# import random
# import numpy as np
# from datetime import datetime, timedelta
# from typing import List, Dict

# class DummyDataGenerator:
#     """Generates realistic dummy data for testing database operations"""
    
#     @staticmethod
#     def generate_dummy_scene() -> Dict:
#         """Generate dummy scene metadata"""
#         return {
#             'timestamp': datetime.now() - timedelta(seconds=random.randint(0, 3600)),
#             'latitude': 40.7128 + random.uniform(-0.01, 0.01),  # New York area coordinates
#             'longitude': -74.0060 + random.uniform(-0.01, 0.01),
#             'resolution': f"{random.choice([1280, 1920, 3840])}x{random.choice([720, 1080, 2160])}",
#             'camera_id': f"cam_{random.randint(1, 10):03d}",
#             'media_path': f"/data/{datetime.now().strftime('%Y%m%d')}/scene_{random.randint(1000, 9999)}.jpg"
#         }

#     @staticmethod
#     def generate_dummy_detections(frame_shape: tuple) -> List[Dict]:
#         """Generate dummy object detections"""
#         classes = ['person', 'car', 'chair', 'door', 'table', 'tree', 'dog', 'stairs']
#         detections = []
        
#         for _ in range(random.randint(1, 5)):
#             height, width = frame_shape[:2]
#             x_min = random.randint(0, width-100)
#             y_min = random.randint(0, height-100)
#             x_max = x_min + random.randint(50, 200)
#             y_max = y_min + random.randint(50, 200)
            
#             detections.append({
#                 'class': random.choice(classes),
#                 'confidence': round(random.uniform(0.5, 0.99), 2),
#                 'bbox': [x_min, y_min, x_max, y_max]
#             })
#         return detections

#     @staticmethod
#     def generate_dummy_annotation(detections: List[Dict]) -> Dict:
#         """Generate dummy human annotation with potential corrections"""
#         return {
#             'label_type': random.choice(['manual', 'ground_truth']),
#             'class_label': random.choice([d['class'] for d in detections] + ['stairs']),
#             'x_min': random.uniform(0, 1),
#             'y_min': random.uniform(0, 1),
#             'x_max': random.uniform(0, 1),
#             'y_max': random.uniform(0, 1),
#             'annotated_by': f"annotator_{random.randint(1, 5)}",
#             'description': random.choice(["Clear path", "Obstacle present", "Text detected"])
#         }

#     @staticmethod
#     def generate_dummy_description(detections: List[Dict]) -> Dict:
#         """Generate dummy scene description based on detections"""
#         objects = ', '.join(set([d['class'] for d in detections]))
#         return {
#             'description': f"Scene contains: {objects}",
#             'confidence': round(random.uniform(0.7, 0.95), 2),
#             'model_version': f"v{random.randint(1, 3)}.{random.randint(0, 5)}"
#         }


# class scenario_temp:
#     def __init__(self, input_source, db_path="D://Devansh//Computer vision course//Main_project//Database_design//Database_design//schema.sql"):
#         """
#         Initialize the scenario_temp class with database integration
#         :param input_source: Path to an image, video, or RTSP stream URL
#         :param db_path: Path to SQLite database file
#         """
#         self.input_source = input_source
#         self.db = SceneDatabase(db_path)
#         self.data_gen = DummyDataGenerator()

#         # Determine input type
#         if input_source.lower().startswith("rtsp"):
#             self.input_type = "rtsp"
#         elif input_source.lower().endswith(".mp4"):
#             self.input_type = "video"
#         elif input_source.lower().endswith(('.jpg', '.jpeg', '.png')):
#             self.input_type = "image"
#         else:
#             raise ValueError("Unsupported input source type.")

#     def process_frames(self):
#         """Process frames and store dummy data in database"""
#         if self.input_type == "image":
#             frame = cv2.imread(self.input_source)
#             if frame is None:
#                 raise ValueError("Failed to load image.")
#             self._process_single_frame(frame)

#         elif self.input_type in ["video", "rtsp"]:
#             cap = cv2.VideoCapture(self.input_source)
#             if not cap.isOpened():
#                 raise ValueError("Failed to open video source.")

#             while cap.isOpened():
#                 ret, frame = cap.read()
#                 if not ret:
#                     break

#                 self._process_single_frame(frame)

#             cap.release()

#         self.db.close()

#     def _process_single_frame(self, frame):
#         """Process a single frame and store data in database"""
#         # Generate dummy data
#         scene_meta = self.data_gen.generate_dummy_scene()
#         detections = self.data_gen.generate_dummy_detections(frame.shape)
#         annotation = self.data_gen.generate_dummy_annotation(detections)
#         description = self.data_gen.generate_dummy_description(detections)

#         # Store in database
#         scene_id = self.db.add_scene(scene_meta)
#         self.db.add_detections(scene_id, detections)
#         self.db.add_annotation(scene_id, annotation)
#         self.db.add_scene_description(scene_id, **description)
        
#         # Random dataset assignment
#         if random.random() > 0.7:
#             self.db.assign_to_dataset([scene_id], random.choice(['train', 'val', 'test']))

#         print(f"Processed scene {scene_id} with {len(detections)} detections")

#     def dummy_predict(self, frame):
#         """Modified to return proper detection format"""
#         height, width = frame.shape[:2]
#         detections = self.data_gen.generate_dummy_detections(frame.shape)
#         return [(d['bbox'][0], d['bbox'][1], 
#                 d['bbox'][2]-d['bbox'][0],  # width
#                 d['bbox'][3]-d['bbox'][1],  # height
#                 d['class']) for d in detections]

# if __name__ == "__main__":
#     # Example usage
#     input_path = "C:/Users/sachi/Downloads/output_video (3).mp4"
    
#     # Initialize and process
#     scenario = scenario_temp(input_path)
#     scenario.process_frames()
    
#     # Verify database entries
#     db = SceneDatabase()
#     print("\nLast 5 scenes:")
#     for scene in db.get_all_scenes(limit=5):
#         print(f"Scene {scene['scene_id']} from {scene['camera_id']} at {scene['timestamp']}")
    
#     print("\nSample detections:")
#     for detection in db.get_detections_by_class('person', 0.5):
#         print(f"Detected {detection['class_label']} with confidence {detection['confidence']}")
    
#     db.close()