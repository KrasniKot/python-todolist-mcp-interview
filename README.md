# python-todolist-mcp-interview
This repository contains a `REST API` for managing Todo items with `MCP` integration for `Claude Desktop.`

## Project Overview
This project comprises two main components: an `API` server and an `MCP Python SDK` server. Together, they facilitate communication with an `MCP Agent`—for example, `Claude Desktop`—enabling it to interact seamlessly with the various endpoints defined by the `API`. These endpoints are presented as `tools` accessible to the `MCP Client`, which in turn allows the client to carry out full CRUD (Create, Read, Update, Delete) operations on todo-lists and their associated items. This setup provides a structured and efficient way for external agents to manage and manipulate todo-list data through clearly defined interfaces.

## Repository Structure

This repository is organised into the following main directories:

- [x] `./api`: Hosts the `FastAPI` server responsible for managing todo-list data, connected to a `SQLite` database for persistent storage.
- [x] `./mcp`: Contains the `MCP` Python SDK server, which acts as an intermediary by exposing tools for managing both todo-lists and todo-items. It interacts with the `FastAPI` server via HTTP requests to perform these operations.

## Setup Instructions: How to set up the whole project environment, install dependencies, etc.

## Running the project: How to start/run the full system, including any prerequisite steps.

## Usage examples: Basic examples of how to use or test.

## Development notes: Info on the folder structure (routes, schemas, crud), coding conventions.
