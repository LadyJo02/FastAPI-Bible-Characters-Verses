# FastAPI Bible Characters and Verses

This project is a simple FastAPI application that provides endpoints for retrieving and storing information about Bible characters and verses. It was created as part of a cloud computing activity.

## Features

* Store character names and messages.
* Store Bible verses and their references.
* Retrieve data by name or verse text.

## Usage

1. Clone the repository.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   ```bash
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the application:
   ```bash
   uvicorn chars:app --reload
   ```
6. Use Postman to interact with the API endpoints.

## Endpoints

* `GET /characters`: Retrieve all characters.
* `GET /characters/{name}`: Retrieve a specific character by name.
* `POST /characters/{name}`: Add or update a character.
* `GET /bible_verses`: Retrieve all Bible verses.
* `GET /bible_verses/{verse}`: Retrieve a specific verse by text.
* `POST /bible_verses/{verse}`: Add or update a Bible verse.

## Contributors

* Joanna Reyda D. Santos DS3A
```
