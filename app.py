import json
from enum import Enum

# Load contacts from JSON file
def load_contacts():
    with open('contacts.json', 'r') as file:
        return json.load(file)

# Save contacts to JSON file
def save_contacts():
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

# Initialize contacts
contacts = load_contacts()

# Enum for actions
class Actions(Enum):
    ADD = 1
    DELETE = 2
    PRINT = 3
    UPDATE = 4
    EXIT = 5

# Menu function to display options and get user selection
def menu():
    for action in Actions:
        print(f'{action.value} - {action.name}')
    return Actions(int(input("please select one: ")))

# Function to add a new contact
def add():
    contacts.append({'fName': input("Your name? "), 'email': input("Your email? ")})
    save_contacts()

# Function to print all contacts
def print_contacts():
    for index, contact in enumerate(contacts):
        print(f"({index}) fName: {contact['fName']} , email: {contact['email']}")

# Function to update an existing contact
def upd_contact():
    victim = find_contact()
    contacts[victim] = {'fName': input("New name? "), 'email': input("New email? ")}
    save_contacts()

# Function to delete a contact
def del_contact():
    victim = find_contact()
    print(f'{contacts[victim]} is kaput')
    contacts.pop(victim)
    save_contacts()

# Function to find a contact by index
def find_contact():
    print_contacts()
    victim = int(input("Please select a victim - number: "))
    return victim

# Main program loop
if __name__ == "__main__":
    while True:
        user_selection = menu()
        if user_selection == Actions.EXIT:
            exit()
        elif user_selection == Actions.ADD:
            add()
        elif user_selection == Actions.PRINT:
            print_contacts()
        elif user_selection == Actions.DELETE:
            del_contact()
        elif user_selection == Actions.UPDATE:
            upd_contact()
