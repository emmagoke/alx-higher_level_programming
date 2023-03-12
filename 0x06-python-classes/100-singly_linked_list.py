#!/usr/bin/python3
"""
This module contains two classes.
Node: For creating a linked list node
Linked List: For creating a linked list
"""


class Node():
    """
    This is the  Node class

    Args:
        data (int): The data in the Node
        next_node (Node): The reference to the next node
    """
    def __init__(self, data):
        """
        Thiss method creates an instance of the class Node
        """
        self.data = data
        self.next_node = None

    @property
    def data(self):
        """
        Returns: The data in the Node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        This method sets the data in the Node.
        Args:
             value (int): The value must be an Integer.
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        This method returns the next_node of the Node instance.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        This method sets the value of the next_node of the Node instance.
        Args:
            value (Node): The value must be an instance of Node or None.
        """
        if (not isinstance(value, Node)) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList():
    """
    This is a SinglyLinkedList Class
    """

    def __init__(self):
        """
        This moethod creates an instance of the class SinglyLinkedList
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        This method nserts a new Node into the correct sorted position in
        the list (increasing order)
        Args:
            value (int)
        """
        new = Node(value)
        if self.__head is None or self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """
        This method print the Singly Linked List when the print()
        function is called on the linked list.
        e.g:
        sll = SinglyLinkedList()
        sll.sorted_insert(2)
        sll.sorted_insert(5)
        print(sll)
        >> 2
        >> 5
        """
        temp = self.__head
        out = ""
        if temp is None:
            return out
        while temp.next_node is not None:
            out += str(temp.data)
            out += "\n"
            temp = temp.next_node
        out += str(temp.data)
        return out
