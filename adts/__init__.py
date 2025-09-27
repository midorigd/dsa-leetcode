import ctypes

# creates low-level arrays
def make_array(size):
    return (size * ctypes.py_object)()


# my implementations
from .ArrayList import ArrayList
from .ArrayStack import ArrayStack

# implementations from class, will update with mine soon
from .ArrayQueue import ArrayQueue
from .ArrayDeque import ArrayDeque
from .SinglyLinkedList import SinglyLinkedList
from .DoublyLinkedList import DoublyLinkedList
from .LinkedBinaryTree import LinkedBinaryTree
from .BinarySearchTreeMap import BinarySearchTreeMap
from .UnsortedArrayMap import UnsortedArrayMap
from .ChainingHashTableMap import ChainingHashTableMap
from .ArrayHeap import ArrayHeap
