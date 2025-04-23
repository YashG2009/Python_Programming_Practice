# Program que-02.py
# Read data stored in a CSV file and convert it into a dictionary with total marks
# Display the dictionary data on the monitor

import csv
import os

def read_csv_to_dict(filename):
    data_dict = {}
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rollno = int(row['RollNo'])
            name = row['Name']
            marks = [int(row['Subject1']), int(row['Subject2']), int(row['Subject3'])]
            total = sum(marks)
            data_dict[rollno] = {
                'name': name,
                'marks': marks,
                'total': total
            }
    return data_dict

input_dir = "que-02-input"
csv_file = os.path.join(input_dir, "students.csv")
data = read_csv_to_dict(csv_file)
print("Data read from CSV and converted to dictionary:")
for rollno, details in data.items():
    print(f"RollNo: {rollno}, Name: {details['name']}, Marks: {details['marks']}, Total: {details['total']}")
