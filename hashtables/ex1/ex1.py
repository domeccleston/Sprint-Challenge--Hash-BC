#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)

    for i in range(len(weights)):
        j = hash_table_retrieve(ht, limit - weights[i])
        if j is not None:
            if i > j:
                return (i, j)
            return (j, i)
        else:
            hash_table_insert(ht, weights[i], i)
            


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
