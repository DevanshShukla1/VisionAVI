# database_test/path_checker.py
import os

schema_path = r'D:\Devansh\Computer vision course\Main_project\Database_design\Database_design\database_test\database\schematest.sql'

def verify_path():
    print(f"Absolute path: {os.path.abspath(schema_path)}")
    print(f"File exists: {os.path.exists(schema_path)}")
    print(f"Readable: {os.access(schema_path, os.R_OK)}")

if __name__ == "__main__":
    verify_path()