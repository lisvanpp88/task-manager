Task Manager App
This is a simple web application project for managing tasks (CRUD: Create, Read, Update, Delete). The application is built using FastAPI on the backend and JavaScript on the frontend to interact with the API.

Features Create Tasks: Add new tasks with a title and description.
Read Tasks: Display all available tasks in a list.
Update Tasks: Edit the title and description of an existing task.
Delete Tasks: Delete a task from the list.
Technologies Used Backend: FastAPI - a modern and fast web framework for building APIs with Python 3.7+ based on typing.
Frontend: HTML, CSS and JavaScript (with the Fetch API).
Database: SQLite (for simplicity, but can be changed to another database if needed).
Templates: Jinja2 for rendering the frontend from the server.
Prerequisites Make sure you have installed:

Python 3.7+
pip (gestor de paquetes de Python)

Endpoints
GET /: Home page displaying the list of tasks.
POST /create_task: Create a new task.
PUT /update_task/{task_id}: Update an existing task.
DELETE /delete_task/{task_id}: Delete a task.

