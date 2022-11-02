from PyInquirer import prompt
import csv

expense_questions = [
    {
        "type": "input",
        "name": "amount",
        "message": "New Expense - Amount: ",
    },
    {
        "type": "input",
        "name": "label",
        "message": "New Expense - Label: ",
    },
    {
        "type": "input",
        "name": "spender",
        "message": "New Expense - Spender: ",
    },

]


def store_expenses(infos):
    if not infos["amount"].isnumeric():
        print("Error : The amount should be a number")
        return False
#   with open('user.csv', 'a')
    with open('expense_report.csv', 'a', newline='') as file:
        fieldnames = ['amount', 'label', 'spender']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(infos)
    return True


def new_expense(*args):
    infos = prompt(expense_questions)
    if store_expenses(infos):
        print("Expense Added !")
    return True
