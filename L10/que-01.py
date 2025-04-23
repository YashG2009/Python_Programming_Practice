# Program que-01.py
# Create a CSV file that can be directly opened in MS-Excel

import csv
import os

def create_csv(filename):
    # Sample data: rollno, name, marks in 3 subjects
    data = [
        ['RollNo', 'Name', 'Subject1', 'Subject2', 'Subject3'],
        [1, 'Alice', 85, 90, 88],
        [2, 'Bob', 78, 82, 80],
        [3, 'Charlie', 92, 88, 95]
    ]
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f"CSV file '{filename}' created successfully.")

output_dir = "que-01-output"
os.makedirs(output_dir, exist_ok=True)
csv_file = os.path.join(output_dir, "students.csv")
create_csv(csv_file)
