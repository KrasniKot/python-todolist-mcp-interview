""" This file represents the entry point for the MCP server """

from mcp.server.fastmcp import FastMCP
from todolist_tools import *
from todoitems_tools import *


mcp = FastMCP("TodoApp")

######## TodoList tools
mcp.tool()(get_all_todolists)
mcp.tool()(get_todolist)
mcp.tool()(get_items_for_list)
mcp.tool()(create_todolist)
mcp.tool()(update_todolist)
mcp.tool()(delete_todolist)
######## 

######## TodoItem tools
mcp.tool()(get_all_todoitems)
mcp.tool()(get_todoitem)
mcp.tool()(create_todoitem)
mcp.tool()(update_todoitem)
mcp.tool()(delete_todoitem)
########
