""" This file represents the entry point for the MCP server """

from mcp.server.fastmcp import FastMCP
from mcp.todolist_tools import *
from mcp.todoitems_tools import *


mcp = FastMCP("TodoApp")
