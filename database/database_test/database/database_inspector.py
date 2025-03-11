import sqlite3

def inspect_database(db_path='test.db'):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Retrieve and print data from the scenes table
    print("=== Scenes ===")
    cursor.execute("SELECT * FROM scenes")
    scenes = cursor.fetchall()
    for scene in scenes:
        print(scene)

    # Retrieve and print data from the detections table
    print("\n=== Detections ===")
    cursor.execute("SELECT * FROM detections")
    detections = cursor.fetchall()
    for detection in detections:
        print(detection)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    inspect_database()