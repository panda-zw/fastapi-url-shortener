# FastAPI URL Shortener

This repository contains the backend code for a URL Shortener application built with FastAPI. The application allows users to shorten long URLs, manage shortened URLs, and retrieve the original URLs. It uses MongoDB for storing URL mappings and provides a RESTful API for interaction.

## Features

- **URL Shortening**: Generate short URLs for long URLs.
- **URL Retrieval**: Redirect to the original URL from a short URL.
- **Duplicate Handling**: Ensure the same URL is not shortened multiple times.
- **Timestamping**: Store the creation date of each shortened URL.
- **Storage**: MongoDB integration for storing URL mappings.
- **Environment Configuration**: Use `.env` files for configuration.

## Getting Started

### Prerequisites

- Python 3.8+
- MongoDB instance
- `pip` (Python package installer)
- `python-dotenv` for environment variable management

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/fastapi-url-shortener.git
   cd fastapi-url-shortener
    ```
   
2. **Create and activate a virtual environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies**:
   ```sh
    pip install -r requirements.txt
    ```
   
4. **Create a `.env` file and add your MongoDB connection string**:
   ```sh
   DB_URL=mongodb://localhost:27017
   ```
   
5. **Run the FastAPI application**:
   ```sh
    uvicorn main:app --reload
    ```
   
## Usage
Once the FastAPI application is running, you can access the API documentation at `http://
localhost:8000/docs`. Use this interface to test the API endpoints and see the available routes

## API Endpoints

**POST /shorten**: Shorten a long URL.
- #### Request
   ```json
   {
      "original_url": "https://example.com"
   }
   ```
- #### Response
   ```json
   {
      "original_url": "https://example.com",
      "short_url": "http://localhost:8000/abc123",
      "created_at": "2021-08-01T12:00:00"
   }
   ```
**GET /{short_url}**: Retrieve the original URL from a short URL.
- #### Response
   - Redirects to the original URL.
   - If the short URL is not found, returns a 404 Not Found error.
  
## Project Structure
- `main.py`: Entry point of the application, sets up FastAPI and routes.
- `routes/url.py`: Contains the URL shortening and retrieval endpoints.
- `models/url.py`: Defines the URL data model.
- `.env`: Environment variables configuration file.
- `requirements.txt`: List of dependencies.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with any improvements or bug fixes.

## License
Distributed under the MIT License. See `LICENSE` for more information.


