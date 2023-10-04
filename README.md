# Semantic Search Project

## Overview
The Semantic Search Project is designed to implement a semantic search feature that retrieves documents based on text content using TF-IDF and cosine similarity. This README provides detailed documentation for the project, including its structure, functionality, and how to use it effectively.

## Table of Contents
1. [Project Structure](#project-structure)
2. [Usage](#usage)
3. [Configuration](#configuration)
4. [Dependencies](#dependencies)
5. [Running the `json_beauty.py` Script](#running-the-json_beautypy-script)
6. [Results](#results)
7. [License](#license)
8. [Acknowledgments](#acknowledgments)

## Project Structure
The project is organized into the following directories and files:

- `app/` - Contains the Python code for the application.
  - `main.py` - The main Flask application for handling REST API requests.
  - `search.py` - The module responsible for performing semantic search.
  - `elasticsearch.yml` - Configuration for Elasticsearch (if used).
  - `Dockerfile` - Dockerfile for building the application image.
- `patent_jsons/` - Directory for storing JSON documents. You can place your JSON files here.
- `docker-compose.yml` - Configuration for Docker Compose, including services for Elasticsearch and the application.
- `requirements.txt` - A list of Python dependencies required for the project.
- `json_beauty.py` - A script to load JSON files, format them, and store them in the desired location.
- `README.md` - This documentation file.

## Usage
To use the Semantic Search Project:

1. Clone this repository to your local machine:

```git clone https://github.com/yourusername/Semantic-Search-Project.git```


2. Add your JSON documents to the `patent_jsons/` directory.

3. Build and run the project using Docker Compose:

```docker-compose up --build```


4. Access the REST API endpoint for semantic search:
- Open your web browser or use a tool like `curl` to make GET requests to `http://localhost:5000/search?query=your_query_here`.
- Replace `your_query_here` with your search query.

## Configuration
You can customize the project's behavior by modifying the following configuration files:

- `app/elasticsearch.yml` - If you choose to use Elasticsearch for indexing and searching documents, configure it in this file.

## Dependencies
The project relies on the following Python dependencies, which are listed in `requirements.txt`:

- Flask - A micro web framework for handling API requests.
- scikit-learn - A machine learning library for TF-IDF vectorization and cosine similarity calculations.
- Elasticsearch (optional) - If you choose to use Elasticsearch.

Install these dependencies using pip:
```pip install -r requirements.txt```


## Running the `json_beauty.py` Script
The `json_beauty.py` script is designed to load all of the JSON files in the source directory, format them, and store them in the desired location for the Semantic Search Project. To run the script:

1. Open your terminal or command prompt.

2. Navigate to the project directory:

```python json_beauty.py```

The script will beautify and reformat all JSON files in the `patent_jsons/` directory and store the formatted JSON files in the same directory.

## Results
![alt text](https://raw.githubusercontent.com/sumitdnath/Semantic-Search-Project/main/Screenshot.png)


The screenshot above shows an example of the project's results after performing a semantic search.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- List any acknowledgments, references, or contributors here.

Feel free to update and expand this README file to provide more detailed documentation for your specific use case and project requirements.

