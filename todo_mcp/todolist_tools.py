""" This module contains the tools for the todolist routes """


import requests

from utils import BASE_URL


def get_all_todolists():
    """ Fetches all the todolists

        >>> Returns all the todolists present in the database
    """
    resp = requests.get(f"{BASE_URL}/todolists/")
    resp.raise_for_status()
    return resp.json()


def get_todolist(todolist_id: int):
    """ Fetches a single todo list, based on its ID
        > todolist_id .... id of the todolist to be fetched

        >>> Returns the todolist information, if found
    """
    resp = requests.get(f"{BASE_URL}/todolists/{todolist_id}")
    resp.raise_for_status()
    return resp.json()


def get_items_for_list(list_id: int):
    """ Fetches the items of a todo list, based on the todolist ID
        > todolist_id .... id of the todolist to be fetched

        >>> Returns the todolist items, if found
    """
    resp = requests.get(f"{BASE_URL}/todolists/{list_id}/items")
    resp.raise_for_status()
    return resp.json()


def create_todolist(name: str):
    """ Creates a todo list
        > name .... todolist name

        >>> Returns the created todolist
    """
    resp = requests.post(f"{BASE_URL}/todolists/", json={"name": name})
    resp.raise_for_status()
    return resp.json()


def update_todolist(todolist_id: int, name: str):
    """" Updates a todo list
        > todolist_id .... id of the todolist to be updated
        > name ........... new name for the todolist

        >>> Returns the updated todolist
    """
    resp = requests.put(f"{BASE_URL}/todolists/{todolist_id}", json={"name": name})
    resp.raise_for_status()
    return resp.json()


def delete_todolist(todolist_id: int):
    """ Deletes a todolist based on its id
        > todolist_id .... id of the todolist to be deleted

        >>> Returns True
    """
    resp = requests.delete(f"{BASE_URL}/todolists/{todolist_id}")
    resp.raise_for_status()
    return {"deleted": True}
