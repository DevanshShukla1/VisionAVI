# import sys
# import os
# from datetime import datetime

# # Add the parent directory to the sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# from database_test.database.db_handlertest import SceneDatabase

# def main():
#     # Initialize database
#     db = SceneDatabase('test.db')
    
#     try:
#         # --- CREATE ---
#         print("Creating new scene...")
#         new_scene_id = db.create_scene({
#             'timestamp': datetime.now().isoformat(),
#             'camera_id': 'test_cam_001',
#             'media_path': '/test/scene_001.jpg',
#             'resolution': '1920x1080'
#         })
#         print(f"Created scene ID: {new_scene_id}")

#         # --- READ ---
#         print("\nReading scene...")
#         scene = db.get_scene(new_scene_id)
#         print(f"Scene details: {scene}")

#         # --- UPDATE ---
#         print("\nUpdating scene...")
#         db.update_scene(new_scene_id, {
#             'resolution': '1280x720',
#             'latitude': 40.7135
#         })
#         updated_scene = db.get_scene(new_scene_id)
#         print(f"Updated resolution: {updated_scene['resolution']}")

#         # --- DELETE ---
#         print("\nDeleting scene...")
#         db.delete_scene(new_scene_id)
#         deleted_scene = db.get_scene(new_scene_id)
#         print(f"Scene after deletion: {deleted_scene}")

#     finally:
#         db.close()

# if __name__ == "__main__":
#     main()


# database_test/example_crudtest.py
from datetime import datetime
from db_handlertest import SceneDatabase

def main():
    db = SceneDatabase('test.db')
    
    try:
        # --- CREATE & SHOW DATA ---
        scene_id = db.create_scene({
            'timestamp': datetime.now().isoformat(),
            'camera_id': 'persistence_test',
            'media_path': '/test/persistent_scene.jpg',
            'resolution': '3840x2160'
        })
        
        print("Created persistent scene. Run database_inspector.py to view it.")
        
    finally:
        db.close()

if __name__ == "__main__":
    main()