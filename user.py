from PyInquirer import prompt
import csv

user_questions = [
    {
        "type": "input",
        "name": "name",
        "message": "New User - Name: ",
    }
]


def store_user(infos):
    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        for rows in reader:
            if infos["name"] == "".join(rows):
                return False
    with open('users.csv', 'a') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([infos["name"]])
    return True


def add_user():
    infos = prompt(user_questions)
    if store_user(infos):
        print("User Added !")
    else:
        print("This user already exist !")
    return True
