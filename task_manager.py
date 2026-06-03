# ===== Importing external modules ===========
from datetime import datetime

# ===== Login Section =====

# Read users from user.txt and store in dictionary
users = {}
with open("user.txt", "r") as f:
    for line in f:
        username, password = line.strip().split(", ")
        users[username] = password

# Ask user to log in
logged_in_user = ""
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful!\n")
        logged_in_user = username
        break
    else:
        print("Incorrect username or password. Try again.\n")

# ===== Main Menu =====
while True:
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    # ===== Register a User =====
    if menu == 'r':
        new_user = input("Enter new username: ")
        new_pass = input("Enter new password: ")
        confirm_pass = input("Confirm new password: ")

        if new_pass == confirm_pass:
            with open("user.txt", "a") as f:
                f.write(f"{new_user}, {new_pass}\n")
            print("New user added successfully!\n")
        else:
            print("Passwords do not match. Try again.\n")

    # ===== Add a Task =====
    elif menu == 'a':
        task_user = input("Enter the username for the task: ")
        title = input("Enter the task title: ")
        description = input("Enter the task description: ")
        due_date = input("Enter the due date (e.g. 20 Jan 2025): ")
        current_date = datetime.now().strftime("%d %b %Y")

        with open("tasks.txt", "a") as f:
            f.write(f"{task_user}, {title}, {description}, {current_date}, {due_date}, No\n")

        print("Task added successfully!\n")

    # ===== View All Tasks =====
    elif menu == 'va':
        print("\n========== ALL TASKS ==========\n")
        with open("tasks.txt", "r") as f:
            for line in f:
                data = line.strip().split(", ")
                if len(data) < 6:
                    continue  # skip malformed lines

                print(f"Task:        {data[1]}")
                print(f"Assigned to: {data[0]}")
                print(f"Date added:  {data[3]}")
                print(f"Due date:    {data[4]}")
                print(f"Completed:   {data[5]}")
                print(f"Description: {data[2]}")
                print("------------------------------------")
        print()

    # ===== View My Tasks =====
    elif menu == 'vm':
        print("\n========== MY TASKS ==========\n")
        with open("tasks.txt", "r") as f:
            for line in f:
                data = line.strip().split(", ")
                if len(data) < 6:
                    continue

                if data[0] == logged_in_user:
                    print(f"Task:        {data[1]}")
                    print(f"Assigned to: {data[0]}")
                    print(f"Date added:  {data[3]}")
                    print(f"Due date:    {data[4]}")
                    print(f"Completed:   {data[5]}")
                    print(f"Description: {data[2]}")
                    print("------------------------------------")
        print()

    # ===== Exit =====
    elif menu == 'e':
        print("Goodbye!!!")
        exit()

    else:
        print("You have entered an invalid input. Please try again\n")