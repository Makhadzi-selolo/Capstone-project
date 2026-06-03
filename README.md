# Task Manager

A simple command-line task management application built with Python that allows users to register, log in, and manage tasks efficiently.

## Features

- **User Authentication**: Secure login and registration system for users
- **Task Management**: Add, view, and track tasks assigned to team members
- **Task Tracking**: Monitor task completion status and due dates
- **User-Specific Views**: View all tasks or filter to see only your assigned tasks

## Getting Started

### Prerequisites

- Python 3.x
- Two text files in the project directory:
  - `user.txt` - Stores user credentials
  - `tasks.txt` - Stores task information

### Installation

1. Clone or download this repository
2. Ensure you have the required text files (`user.txt` and `tasks.txt`) in the same directory as `task_manager.py`
3. Run the application:
   ```bash
   python task_manager.py
   ```

### File Structure

- **user.txt**: Contains user credentials in the format:
  ```
  username, password
  ```
  Example:
  ```
  john_doe, password123
  jane_smith, secure_pass
  ```

- **tasks.txt**: Contains task information in the format:
  ```
  username, title, description, date_added, due_date, completed
  ```

## Usage

### Login
When you start the application, you'll be prompted to enter your username and password. You must have a valid account to proceed.

### Main Menu Options

| Option | Description |
|--------|-------------|
| `r` | Register a new user account |
| `a` | Add a new task |
| `va` | View all tasks in the system |
| `vm` | View only your assigned tasks |
| `e` | Exit the application |

### Workflow Examples

**Registering a New User:**
```
Select one of the following options: r
Enter new username: new_user
Enter new password: my_password
Confirm new password: my_password
New user added successfully!
```

**Adding a Task:**
```
Select one of the following options: a
Enter the username for the task: john_doe
Enter the task title: Complete Report
Enter the task description: Finish quarterly sales report
Enter the due date (e.g. 20 Jan 2025): 15 Feb 2025
Task added successfully!
```

**Viewing Tasks:**
- Use `va` to see all tasks assigned to all users
- Use `vm` to see only your assigned tasks

## Data Format

### Task Information
Tasks are stored with the following information:
- **Username**: Who the task is assigned to
- **Title**: The task title
- **Description**: Detailed task description
- **Date Added**: When the task was created (auto-generated)
- **Due Date**: When the task is due
- **Completed**: Status of the task (Yes/No)

## Troubleshooting

- **Login fails**: Ensure your username and password are correct and match what's in `user.txt`
- **Task not appearing**: Check that the `tasks.txt` file exists and has proper formatting
- **Malformed lines skipped**: The application will skip any lines in `tasks.txt` that don't have the correct number of fields

## Future Enhancements

Potential improvements for this project:
- Mark tasks as complete
- Edit or delete existing tasks
- Add task priority levels
- Implement password encryption for better security
- Add due date validation
- Create a database backend instead of text files
- Add task filtering by date or status

## License

This project is open source and available for educational purposes.

## Author

Created as a Capstone Project

---

**Note**: This is a simple implementation suitable for learning purposes. For production use, consider implementing proper database management, password encryption, and enhanced security features.
