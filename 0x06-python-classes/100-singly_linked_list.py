#!/usr/bin/python3
"""defines a node and SinglyLinkedList class"""


class Node:
    """represents a node in a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a Node

        Args:
            data: the data to be stored in the node
            next_node: the next node in the list

        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gets the data from a node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """sets the data in a Node

        Args:
            value: the value to set it to

        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets the next node in a list"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """sets the next node in a list"""

        if not (isinstance(value, Node) or value is None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        """defines the print representation of this object"""
        tmp = self.__head
        string = ""
        while tmp is not None:
            string += "{}\n".format(tmp.data)
            tmp = tmp.next_node

        return (string[0:-1])

    def sorted_insert(self, value):
        tmp = self.__head
        new = Node(value)
        prev = None

        if (tmp is None):
            self.__head = new
            return

        while tmp is not None:
            if (tmp.data > value):
                if (prev is not None):
                    prev.next_node = new
                else:
                    self.__head = new
                new.next_node = tmp

                return

            prev = tmp
            tmp = tmp.next_node

        prev.next_node = new
