import pickle

def main():

    user_name_email_dict = get_names_starting()

    display_menu(user_name_email_dict)

def get_names_starting():

    # Name and email directory
    user_name_email_dict = {}

    # Add name and email to Database
    print("\nPlease enter the name and the email that you want to add down below:")

    another = "Y"
    while another.upper() == "Y":

        # Store the name and the email
        name = input("\nEnter your name: ")
        email = input("Enter your email: ")

        # Store to dict
        user_name_email_dict[name] = email

        another = input("Enter 'y' to add another name and email, else, enter anything else to stop: ")

    return user_name_email_dict

def display_menu(user_name_email_dict):

    # Menu Constants
    ADD_NAME_AND_EMAIL = 1
    LOOKUP_EMAIL = 2
    CHANGE_EMAIL = 3
    DELETE_EMAIL = 4

    # Display the prompt
    print("\nPlease tell us what you want to do:")
    print("1) Add name and email")
    print("2) Look-up email")
    print("3) Change email")
    print("4) Delete email")

    # Get the user input
    user_input_number = int(input("\nPlease enter your choice: "))

    # Get the choices set out.
    if user_input_number == 1:
        add_name_and_email_function(user_name_email_dict)

    elif user_input_number == 2:
        look_up_email_function(user_name_email_dict)

    elif user_input_number == 3:
        change_email_function(user_name_email_dict)

    elif user_input_number == 4:
        delete_email_function(user_name_email_dict)

def add_name_and_email_function(user_name_email_dict):

    # Add name and email to Database
    print("\nPlease enter the name and the email that you want to add down below:")

    another = "Y"
    while another.upper() == "Y":

        # Store the name and the email
        name = input("\nEnter your name: ")
        email = input("Enter your email: ")

        # Store to dict
        user_name_email_dict[name] = email

        another = input("Enter 'y' to add another name and email, else, enter anything else to stop: ")

    print(f"add_name_and_emmail_function {user_name_email_dict}")

    # Control statement to go back to menu
    print("\nWould you like to go to menu?")

    user_input_menu_choice = input("Enter Y, otherwise, anything else to terminate the program: ")

    if user_input_menu_choice.upper() == "Y":
        display_menu(user_name_email_dict)
    else:
        print("Ending program")

def look_up_email_function(user_name_email_dict):

    print(f"Look_up_email_function: {user_name_email_dict}")

    look_up_key = input("\nEnter your name to get the email from the database: ")

    if look_up_key in user_name_email_dict.keys():
        print(f"Email: {user_name_email_dict[look_up_key]}")

    while look_up_key not in user_name_email_dict.keys():

        look_up_key = input("\nSorry that name is not in our database please enter another name: ")

        if look_up_key in user_name_email_dict.keys():
            print(f"Email: {user_name_email_dict[look_up_key]}")

    # Control statement to go back to menu
    print("\nWould you like to go to menu?")

    user_input_menu_choice = input("Enter Y otherwise anything else to terminate the program: ")

    if user_input_menu_choice.upper() == "Y":
        display_menu(user_name_email_dict)
    else:
        print("Ending program")

def change_email_function(user_name_email_dict):

    print(f"change_email_function: {user_name_email_dict}")

    user_inputs_name = input("Enter your name: ")

    if user_inputs_name in user_name_email_dict.keys():

        new_email = input("Enter your new email address here: ")

        user_name_email_dict[user_inputs_name] = new_email

    while user_inputs_name not in user_name_email_dict:

        user_inputs_name = input("Sorry that name is not in our database please enter another one: ")

        if user_inputs_name in user_name_email_dict.keys():

            new_email = input("Enter your new email address here: ")

            user_name_email_dict[user_inputs_name] = new_email

            break

    # Control statement to go back to menu
    print("\nWould you like to go to menu?")

    user_input_menu_choice = input("Enter Y otherwise anything else to terminate the program: ")

    if user_input_menu_choice.upper() == "Y":
        display_menu(user_name_email_dict)
    else:
        print("Ending program")

def delete_email_function(user_name_email_dict):

    print(f"delete_email_function: {user_name_email_dict}")

    delete_name_input = input("Enter your name: ")

    while delete_name_input not in user_name_email_dict.keys():

        delete_name_input = input("That name was not there please type in a different name: ")

        if delete_name_input in user_name_email_dict.keys():

            del user_name_email_dict[delete_name_input]

            print("That email has been deleted from the database")

            print(f"\nNew Database: {user_name_email_dict}")

    if delete_name_input in user_name_email_dict.keys():

        del user_name_email_dict[delete_name_input]

        print("That email has been deleted from the database")

        print(f"\nNew Database: {user_name_email_dict}")

    # Control statement to go back to menu
    print("\nWould you like to go to menu?")

    user_input_menu_choice = input("Enter Y otherwise anything else to terminate the program: ")

    if user_input_menu_choice.upper() == "Y":
        display_menu(user_name_email_dict)
    else:
        print("Ending program")

main()