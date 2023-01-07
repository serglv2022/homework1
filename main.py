import datetime
import time

CreationDate = datetime.datetime.today().strftime("%d-%m-%Y")
CreationTime = time.strftime("%H.%M.%S")

print("Date: ", CreationTime + " " + CreationDate, "\n")

print("before import salary", "\n")

import salary

print("Module salary was imported", "\n")

print("before import people", "\n")

import people

print("Module people was imported", "\n")

print("Begin if __name__ == '__main__'", "\n")
if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
print("Finish if __name__ == '__main__'")
