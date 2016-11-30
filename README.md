# Unrolled Linked List

This repository contains information for lab 1 of BYU's CS498r: Problem Solving and Competitive Programming class.

Startup code is provided to turn your code into a package with 2 modules (UnrolledLinkedList and Tests). Please follow the exact naming conventions and file structure of this repository


## What is an Unrolled Linked List?

An [Unrolled Linked List](https://en.wikipedia.org/wiki/Unrolled_linked_list) is essentially a Linked List, where each node contains a list of elements up to a given max node capacity [more](https://brilliant.org/wiki/unrolled-linked-list/) 

![alt text](https://upload.wikimedia.org/wikipedia/commons/1/16/Unrolled_linked_lists_%281-8%29.PNG)

### Balancing

Here is an example of adding to the end of an Unrolled Linked List with a max node capacity of 4.[this link has a good explaination of insertion / deletion](https://blogs.msdn.microsoft.com/devdev/2005/08/22/unrolled-linked-lists/)

```
{}
{[1]}
{[1, 2]}
{[1, 2, 3]}
{[1, 2, 3, 4]}
{[1, 2], [3, 4, 5]}
{[1, 2], [3, 4, 5, 6]}
{[1, 2], [3, 4], [5, 6, 7]}
{[1, 2], [3, 4], [5, 6, 7, 8]}
```

If I were to remove the value 3, then 4:

```
{[1, 2], [4, 5, 6], [7, 8]}
{[1, 2], [5, 6], [7, 8]}
```

### Pros

* Linked Lists are O(n) access. Having nodes that hold muliple elements in a list / array lowers that cost
* This also helps to lower the amount of memory used in a traditional Linked List

## Lab 1 Specs

### Requirements

Implement an Unrolled Linked List according to the following requirements. 

Implement the following dunder methods:

* \_\_delitem\_\_ (self,index)
    * Remove the item at the given index.
    * If the index is negative, then you should remove starting from the back (i.e. deleting at -2 would delete the second-to-last element)
    * If the index is too large, raise an IndexError
* \_\_getitem\_\_ (self,index):
    * Returns the item in the given index.
    * If the index is negative, return with the index starting from the back (i.e. getting at -1 returns the last item)
    * If the index is too large, raise an IndexError
* \_\_setitem\_\_ (self,key,value):
    * sets the item at `key` to `value`
    * If the key is too large, raise an IndexError
* \_\_iter\_\_ (self):
    * Use the Python yield statement to make your list iterable. This will allow you to use it in a for-each loop
* \_\_str\_\_ (self)
    * Create a string representation of the list in the form {[x, x, x], [x, x], [x, x, x, x]}
where each set of [] indicates the list of values within a single node.
* \_\_len\_\_ (self)
    * returnsthetotal#ofdatainthelist,notthenumberofnodes
* \_\_reversed\_\_ (self)
    * reverse of iter
* \_\_contains\_\_ (self, obj)
    * Returns True if obj is in the data structure, otherwise False

Implement additional method:

* append(self,data)
    * Add the data to the end of the list
    * If a node has reached its max capacity, you must create a new node to put the data in

You are also responsible for writing your own test cases. We highly recommend taking advantage of [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development). We are expecting complete code coverage, if you can define your tests based on what you know about unrolled linked lists, your life will be much easier. 

Your test cases should be in a separate file. See below to learn more about the unittest package

Your class should be called UnrolledLinkedList, in the package lists

You must have a balanced Unrolled Linked List (see above)

### Grading

| Grading Rubric      |    |
| ------------------- | --:|
| Passes Unit Tests   | 70 |
| Code Quality        | 15 |
| Test Coverage       | 15 |
| Extra Credit (each) |  3 |

The penalty for each day late is 10%

#### Extra Credit

To get extra credit, you can implement any of the following dunder methods (3 points for each implementation):

* \_\_getslice\_\_
* \_\_setslice\_\_
* \_\_delslice\_\_

## Code Quality

[PEP 8](https://www.python.org/dev/peps/pep-0008/) is a standard for writing clean and pythonic code. Although not all Python developers choose to follow it as a style guide, it is well accepted in the Python community. Feel free to approach the code quality portion of this assignment as you wish. You are not required to use PEP 8, but it is a really good option

## unittest

unittest is a built-in testing framework for Python ([Python2](https://docs.python.org/2/library/unittest.html) or [Python3](https://docs.python.org/3/library/unittest.html)). You will need to use this for the testing portion of the lab

If I were to implement a test case for testing a Python list, I might start with something similar to the following...

```python
import unittest

class Test_List(unittest.TestCase):
    
    def test_empty(self):
        """Tests if a list is empty.
        """
        l = list()
        self.assertEqual(str(l), "[]")
        list.append(1)
        del list[0]
        self.assertEqual(str(l), "[]")

```

## Dunder Methods

Dunder stands for double underscores. Dunder methods are also refered to as magic methods, but don't use that term. They really aren't that magical

Classes can implement dunder functions as needed. They allow operators and certain built-in python functions to work on the class. For example: adding two lists using the __add__ dunder function:

```python
l1 = [1,2,3,4]
l2 = [5,6,7,8]

l = l1 + l2
print(l)
# [1, 2, 3, 4, 5, 6, 7, 8]
```

If I were to implement the \_\_getitem\_\_ dunder method for a Linked List, it might look something like this:

```python
    def __getitem__(self, index):
        """Allows you to get an item using the [] syntax
        """
        return self.getNodeAt(index)
```


## yield

The yield keyword essentially makes the object 'iterable'. It is a [generator](https://pythontips.com/2013/09/29/the-python-yield-keyword-explained/), meaning that the data is created on demand, rather than using additional memory to store the result. Check out the link for a much better description of generators. You will be expected to use it for functions that generate values on the fly (iterators). 


