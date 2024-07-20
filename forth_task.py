def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"

    return inner

def index_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Contact don't exist"

    return inner


def parse_input(user_input: str) -> list:
    """
    Parse console input

    Returns: 
        Parsed values of command and arguments
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args: list, contacts: dict) -> str:
    """
    Add contact to dictionary

    Returns:
        Console message of result
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args: list, contacts: dict) -> str:
    """
    Change contact in dictionary

    Returns:
        Console message of result
    """
    name, phone = args
    contacts[name] = phone
    return "Contact changed."

@index_error
@input_error
def show_phone(args: list, contacts: dict) -> str:
    """
    Show phone number of contact from dictionary

    Returns:
        Console message of result
    """
    name = args[0]
    return f"{contacts[name]}"
 
def show_all(contacts: dict) -> dict | str :
    """
    Show all contacts in dictionary

    Returns:
        Console message of result
    """
    if contacts == {}:
        return "Contacts list empty"
    else:
        return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
