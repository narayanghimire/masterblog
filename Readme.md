# Flask Blog Application

This is a simple Flask-based blog application that supports adding, deleting, and updating blog posts. The blog posts are stored in a JSON file.

## Features

- Display blog posts
- Add new blog posts
- Update existing blog posts
- Delete blog posts

## Project Structure

- `app/`: Contains the application code.
  - `controller/`: Flask route handlers.
  - `model/`: Data models.
  - `service/`: Services for managing blog posts.
  - `impl/`: Implementation of services.
- `static/`: Contains static files like CSS and JSON data.
- `templates/`: Contains HTML templates for rendering views.
- `requirements.txt`: List of dependencies.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/narayanghimire/masterblog.git
cd masterblog
 ```

2 **Install Dependencies**

 ```bash
  pip install -r requirements.txt
 ```
## Usage
1. **Run the Application**

    ```bash
    python3 main.py
    ```