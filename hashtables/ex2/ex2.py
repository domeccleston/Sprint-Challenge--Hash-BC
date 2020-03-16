#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)

    # initialize key to NONE and iterate through tickets, updating new key as previous value

    key = "NONE"
    
    for i in range(length):
        current_ticket = hash_table_retrieve(hashtable, key)
        key = current_ticket
        route[i] = current_ticket

    # remove the final NONE
    route.pop()
    return route
    