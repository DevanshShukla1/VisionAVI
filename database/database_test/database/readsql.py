import sqlite3

def read_table_data(db_path, table_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execute a query to retrieve all data from the specified table
    cursor.execute(f"SELECT * FROM {table_name}")

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Print the column names
    column_names = [description[0] for description in cursor.description]
    print(f"Column names: {column_names}")

    # Print each row
    for row in rows:
        print(row)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    db_path = 'test.db'  # Path to your SQLite database file
    table_name = 'annotations'  # Replace with your table name
    read_table_data(db_path, table_name)