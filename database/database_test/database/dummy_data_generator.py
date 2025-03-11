# database_test/dummy_data_generator.py
import os
from datetime import datetime, timedelta
from db_handlertest import SceneDatabase

def generate_dummy_data(db_path='test.db'):
    db = SceneDatabase(db_path)
    
    try:
        # Create 5 dummy scenes
        for i in range(1, 6):
            scene_meta = {
                'timestamp': (datetime.now() - timedelta(minutes=i)).isoformat(),
                'camera_id': f'cam_{i:03d}',
                'media_path': f'/data/scene_{i}.jpg',
                'resolution': '1920x1080',
                'latitude': 40.7128 + (i * 0.001),
                'longitude': -74.0060 + (i * 0.001)
            }
            scene_id = db.create_scene(scene_meta)
            
            # Add dummy detections
            detections = [{
                'class': 'person' if i % 2 == 0 else 'car',
                'confidence': 0.8 + (i * 0.02),
                'bbox': [100*i, 150*i, 200*i, 300*i]
            }]
            db.add_detections(scene_id, detections)
            
            print(f"Created scene {scene_id} with {len(detections)} detections")
            
        print("\nDummy data generation complete!")
        
    finally:
        db.close()

if __name__ == "__main__":
    generate_dummy_data()