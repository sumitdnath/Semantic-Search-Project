# Semantic Search Project

## Overview
This project implements a semantic search feature that retrieves documents based on text content using TF-IDF and cosine similarity. It allows you to search for relevant documents within a collection of JSON files.

## Project Structure
The project is structured as follows:

- `app/` - Contains the Python code for the application.
  - `main.py` - The main Flask application for handling REST API requests.
  - `search.py` - The module responsible for performing semantic search.
  - `elasticsearch.yml` - Configuration for Elasticsearch (if used).
  - `Dockerfile` - Dockerfile for building the application image.
- `patent_jsons/` - Directory for storing JSON documents. You can place your JSON files here.
- `docker-compose.yml` - Configuration for Docker Compose, including services for Elasticsearch and the application.
- `requirements.txt` - A list of Python dependencies required for the project.
- `README.md` - This documentation file.

## Usage
To use this project:

1. Clone this repository to your local machine:
