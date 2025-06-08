# python-todolist-mcp-interview
This repository contains a `REST API` for managing Todo items with `MCP` integration for `Claude Desktop.`

## Project Overview
This project comprises two main components: an `API` server and an `MCP Python SDK` server. Together, they facilitate communication with an `MCP Agent`—for example, `Claude Desktop`—enabling it to interact seamlessly with the various endpoints defined by the `API`. These endpoints are presented as `tools` accessible to the `MCP Client`, which in turn allows the client to carry out full CRUD (Create, Read, Update, Delete) operations on todo-lists and their associated items. This setup provides a structured and efficient way for external agents to manage and manipulate todo-list data through clearly defined interfaces.

## Repository Structure

This repository is organised into the following main directories:

- `./api`: Hosts the `FastAPI` server responsible for managing todo-list data, connected to a `SQLite` database for persistent storage.
- `./mcp`: Contains the `MCP` Python SDK server, which acts as an intermediary by exposing tools for managing both todo-lists and todo-items. It interacts with the `FastAPI` server via HTTP requests to perform these operations.

## Setup Instructions

- [x] Recommended OS: `Windows 10` or `Windows 11`. This project was tested on a `Windows 10` virtual machine.
- [x] Install `Python 3.12.3` from the official website: [python.org](https://www.python.org/downloads/)
- [x] Confirm the correct version of `Python` is installed by opening your `Terminal` (Linux) or `PowerShell` (Windows) and running `python --version`
- [x] Confirm that `pip` is installed by running `pip --version`
    - If `pip` is not installed, install it first before proceeding.
- [x] Ensure `Claude Desktop` is installed and functioning properly.

### Steps

1. Clone the repository: `git clone https://github.com/KrasniKot/python-todolist-mcp-interview`
2. Navigate to the root directory: `cd python-todolist-mcp-interview/`
3. You will find a `requirements.txt` file which lists all the required `Python` modules for proper setup.
4. Install the dependencies: `pip install -r requirements.txt`
5. Once installation is complete, start the `FastAPI` server using: `uvicorn api.main:app`. This will make the endpoints available locally.
6. Open other `Terminal` or `PowerShell` window and install the `MCP` server in `Claude Desktop` by running: `mcp install ./todo_mcp/server.py`
7. Restart `Claude Desktop`. In some cases, you may need to terminate all running `Claude Desktop` processes for changes to take effect.
8. You are all set! You can now ask `Claude Desktop` to use the available tools.

## Usage Examples

The usage of this project is rather straight forward.

1. Open `Claude Desktop`
2. Prompt it to perform an action. Eg "List all the current todolists" or "Create a new todo list"

### Actions That Can Be Performed

#### TodoLists

| Method | Description                   | Route                                            | MCP Function           |
|--------|-------------------------------|--------------------------------------------------|------------------------|
| POST   | Create TodoList               | http://localhost:8000/todolists/                 | create_todolist        |
| GET    | Get all TodoLists             | http://localhost:8000/todolists/                 | get_all_todolists      |
| GET    | Get one TodoList              | http://localhost:8000/todolists/{todolist_id}    | get_todolist           |
| GET    | Get TodoItems from TodoList   | http://localhost:8000/todolists/{list_id}/items  | get_items_for_list     |
| PUT    | Update TodoList               | http://localhost:8000/todolists/{todolist_id}    | update_todolist        |
| DELETE | Delete TodoList               | http://localhost:8000/todolists/{todolist_id}    | delete_todolist        |

#### TodoList Structure
| Field | Type     | Constraints                | Description                            |
|-------|----------|----------------------------|----------------------------------------|
| id    | Integer  | Primary key, Indexed       | Unique identifier for the TodoList     |
| name  | String   | Unique, Not null           | Name/title of the TodoList             |
| items | List     | Relationship (1-to-many)   | List of related TodoItems              |


#### TodoItems

| Method | Description         | Route                                           | MCP Function         |
|--------|---------------------|-------------------------------------------------|----------------------|
| POST   | Create TodoItem     | http://localhost:8000/todoitems/                | create_todoitem      |
| GET    | Get all TodoItems   | http://localhost:8000/todoitems/                | get_all_todoitems    |
| GET    | Get one TodoItem    | http://localhost:8000/todoitems/{todoitem_id}   | get_todoitem         |
| PUT    | Update TodoItem     | http://localhost:8000/todoitems/{todoitem_id}   | update_todoitem      |
| DELETE | Delete TodoItem     | http://localhost:8000/todoitems/{todoitem_id}   | delete_todoitem      |

#### TodoItem Structure
| Field       | Type      | Constraints                 | Description                                                  |
|-------------|-----------|-----------------------------|--------------------------------------------------------------|
| id          | Integer   | Primary key, Indexed        | Unique identifier for the TodoItem                           |
| list_id     | Integer   | Foreign key (todo_lists.id) | ID of the associated TodoList (not null)                     |
| description | String    | Not null                    | Description of the task                                      |
| status      | Enum      | Default: not started        | Current status (`not started`, `in progress`, or `finished`) |
| todo_list   | Object    | Relationship (many-to-1)    | Associated `TodoList` object                                 |


## Development Notes

If you went through the code, you probably found some details regarding the code style.

- [x] Use `> param_name ....` description inside docstrings to describe function parameters.
- [x] Use `>>> Returns ...` in docstrings to indicate return values, inline and concise.
- [x] Many functions as one-liners unless they require more logic.
- [x] Parameters and comments in docstrings are visually aligned for better readability.
- [x] Variables aligned for better readability.
- [x] Use `########` (eight `#` characters) as a title separator to mark new sections in the code for clarity.

