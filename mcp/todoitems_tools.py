""" This module contains the tools for todoitems """

import requests

from mcp.utils import BASE_URL


def get_all_todoitems():
    """ Fetches all existing todoitems

        >>> Returns all existing todo items
    """
    resp = requests.get(f"{BASE_URL}/todoitems/")
    resp.raise_for_status()
    return resp.json()


def get_todoitem(todoitem_id: int):
    """ Fetches a todoitem based on its id
        > todoitem_id .... id of the todoitem to be fetched

        >>> Returns the fetched todo item, if found
    """
    resp = requests.get(f"{BASE_URL}/todoitems/{todoitem_id}")
    resp.raise_for_status()
    return resp.json()


def create_todoitem(data: dict):
    """ Creates a todoitem
        > data .... data for the todoitem to be created, data must include:
                    'description' (str), 'status' (str, can be only in lowercase [not started, in progress or finished]) and 'list_id' (int)

        >>> Returns the created todoitem
    """
    resp = requests.post(f"{BASE_URL}/todoitems/", json=data)
    resp.raise_for_status()
    return resp.json()


def update_todoitem(todoitem_id: int, data: dict):
    """ Updates a todoitem based on its id
        > todoitem_id .... id of the item to be updated
        > data ........... data to update in the todoitem and
                           it might include: 'description' (str), 'status' (str, can be only in lowercase [not started, in progress or finished]) and 'list_id' (int)

        >>> Returns the updated todoitem
    """
    resp = requests.put(f"{BASE_URL}/todoitems/{todoitem_id}", json=data)
    resp.raise_for_status()
    return resp.json()


def delete_todoitem(todoitem_id: int):
    """ Deletes a todoitem based on its id
        > todoitem_id .... id of the item to be deleted

        >>> Returns True
    """
    resp = requests.delete(f"{BASE_URL}/todoitems/{todoitem_id}")
    resp.raise_for_status()
    return {"deleted": True}
