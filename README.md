# Assignment: Task Manager API

## Instructions

### Overview

You are tasked with building a Task Manager API using FastAPI. The API should allow users to manage tasks with features similar to the provided codebase. Follow the instructions below to implement the required functionality.

### Steps

1. **Setup the Project**:
   - Create a new FastAPI project.
   - Set up the project structure similar to the provided codebase.

2. **Database Configuration**:
   - Use SQLModel to define database models.
   - Create a `Task` model with the following fields:
     - `id`: Primary key (integer).
     - `title`: String (2-100 characters).
     - `description`: String (optional, max 1000 characters).
     - `completed`: Boolean (default: False).
     - `priority`: Integer (1-5).

3. **API Endpoints**:
   - Implement the following endpoints:
     - `POST /tasks`: Create a new task.
     - `GET /tasks`: Retrieve all tasks with optional filters (e.g., `completed`, `priority`).
     - `GET /tasks/{task_id}`: Retrieve a task by its ID.
     - `PATCH /tasks/{task_id}`: Update a task.
     - `DELETE /tasks/{task_id}`: Delete a task.

4. **Validation**:
   - Add validation for input data (e.g., `title` length, `priority` range).

5. **Middleware**:
   - Add CORS middleware to allow requests from any origin.

6. **Testing**:
   - Test all endpoints using a tool like Postman or FastAPI's interactive docs.

7. **Documentation**:
   - Ensure all endpoints are well-documented using FastAPI's automatic documentation.

### Bonus

- Add pagination to the `GET /tasks` endpoint.
- Implement a `PUT /tasks/{task_id}` endpoint to replace a task entirely.
- Add user authentication to secure the API.

### Submission

Submit your project as a GitHub repository link. Ensure the repository includes:

- The complete codebase.
- A `README.md` file with setup instructions.
- Example requests and responses for each endpoint.
