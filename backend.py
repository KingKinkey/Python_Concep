import csv
import os

class BackEndManager:
    def __init__(self):
        self.data_file = ""

class AddValueToCSV:
    def __init__(self, file_name):
        if not os.path.exists(file_name):
            raise ValueError(f"File {file_name} does not exist.")
        self.file_name = file_name

    def add_value(self, value):
        with open(self.file_name, 'a') as file:
            writer = csv.writer(file)
            writer.writerow([value])


class ComplexValue:
    def __init__(self, name, age, id, file_name):
        self.name = name
        self.age = age
        self.id = id
        self.file_name = file_name
        with open(file_name, 'a') as my_file:
            my_file.write(f"{name}, {age}, {id}\n")


def display_record(file_name):
    with open(file_name, "r") as file:
        contents = file.read()
        print(contents)


class CreateCSV:
    def __init__(self, filename):
        self.filename = filename

    def create_file(self):
        if not self.filename.endswith('.csv'):
            raise ValueError("File name must end with '.csv'")
        with open(self.filename, 'w', newline='') as file:
            pass
