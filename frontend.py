import sys
import backend

class FrontEndUI:
    def __init__(self, backend):
        self.backend = backend

    def show_ui(self):
        message = "\n"
        message += "Welcome to stock tracker for Generic Company PTY LTD \n"
        message += "1. To Add one value to a record \n"
        message += "2. To Display records \n"
        message += "3. To create a new file \n"
        message += "4. To add a record with three values \n"
        message += "5. To exit \n"
        message += "Whats your option "
        sys.stdout.write(message)
        user_input = int(sys.stdin.readline())
        question = "what do you want to add? \n"

        while user_input != 5:
            if user_input == 1:
                question_name_of_csv_file = "Enter the name of the existing CSV file: "
                sys.stdout.write(question_name_of_csv_file)
                file_name = input()
                question_one_value_add = "Enter the value to add to the CSV file: "
                sys.stdout.write(question_one_value_add)
                value = input()
                add_value_to_csv = backend.AddValueToCSV(file_name)
                add_value_to_csv.add_value(value)
                sys.stdout.write(message)
                user_input = int(sys.stdin.readline())

            elif user_input == 2:
                print("what file do you want display : try 'test_case.txt")
                file2 = str(sys.stdin.readline().strip())
                backend.display_record(file2)
                sys.stdout.write(message)
                user_input = int(sys.stdin.readline())

            elif user_input == 3:
                print("Enter the name of the .csv file to create, make sure to add the '.csv' at the end to avoid a error message: ")
                filename = sys.stdin.readline().strip()
                try:
                    csv_file = backend.CreateCSV(filename)
                    csv_file.create_file()
                    print("File created successfully.\n")
                    print(message)
                    user_input = int(sys.stdin.readline())
                except Exception as e:
                    print(str(e) + '\n')

            elif user_input == 4:
                print(question)
                name = input("Enter the item name: ")
                age = (input("Enter the shelf life of " + name + ": "))
                id = float(input("Enter the SKU number of " + name + ": "))
                file = input("Enter the filename, must end in .csv: ")
                obj = backend.ComplexValue(name, age, id, file)
                print(message)
                user_input = int(sys.stdin.readline())
