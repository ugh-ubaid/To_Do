# To-Do List / Task Manager

## Tech Stack
- Python (Flask)
- MySQL
- HTML/CSS

## Description
A web-based task manager to help users track their daily tasks. Features include adding, updating, deleting, marking tasks as completed, and filtering by status.

## Features
- Add new tasks
- Update/edit tasks
- Delete tasks
- Mark tasks as Pending/Completed
- Optional: User authentication

## Database
### Table: tasks
| Column       | Type         |
|-------------|-------------|
| id          | INT PK      |
| user_id     | INT FK      |
| title       | VARCHAR     |
| description | TEXT        |
| due_date    | DATE        |
| status      | ENUM        |
| created_at  | TIMESTAMP   |

### Table: users (optional)
| Column      | Type         |
|------------|-------------|
| id         | INT PK      |
| username   | VARCHAR     |
| email      | VARCHAR     |
| password   | VARCHAR     |

## How to Run
1. Clone the repo
```bash
git clone <https://github.com/ugh-ubaid/To_Do>
cd To_DO
