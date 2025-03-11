# Create
new_scene_id = db.create_scene({
    'timestamp': datetime.now().isoformat(),
    'camera_id': 'cam_002',
    'media_path': '/data/scenes/scene_002.jpg'
})

# Read
scene = db.get_scene(new_scene_id)
all_scenes = db.get_all_scenes(limit=10)

# Update
db.update_scene(new_scene_id, {
    'resolution': '1280x720',
    'latitude': 40.7135
})

# Delete
db.delete_scene(new_scene_id)  # Automatically deletes related data

# Detection operations
detections = db.get_scene_detections(scene_id=5)
if detections:
    first_detection = detections[0]
    db.update_detection(first_detection['detection_id'], {'confidence': 0.95})
    db.delete_detection(first_detection['detection_id'])