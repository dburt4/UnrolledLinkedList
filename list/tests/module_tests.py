''' You will need the following import if using python2 '''
# from __future__ import absolute_import

from ..unrolled_linked_list.module import UnrolledLinkedList
import unittest


class UnrolledLinkedList_Test(unittest.TestCase):
    """This is an example of a Testing class. You are welcome to make multiple
    classes to organize your code if you would like to, but it is in no way
    required or expected. You'll want to replace this comment with your own.
    """
    def test_default_node_capacity(self):
        """Test that the default node capacity is being set, and is set to 16
        """
        l = UnrolledLinkedList()
        self.assertEqual(l.max_node_capacity, 16)

    def test_append(self):
        l = UnrolledLinkedList(4)
        l.append(1)
        self.assertEquals(str(l),"{[1]}")
        l.append(2)
        self.assertEquals(str(l), "{[1, 2]}")
        l.append(3)
        self.assertEquals(str(l), "{[1, 2, 3]}")
        l.append(4)
        self.assertEquals(str(l), "{[1, 2, 3, 4]}")
        l.append(5)
        self.assertEquals(str(l), "{[1, 2], [3, 4, 5]}")
        l.append(6)
        l.append(7)
        l.append(8)
        self.assertEquals(str(l), "{[1, 2], [3, 4], [5, 6, 7, 8]}")

        l2 = UnrolledLinkedList(2)
        l2.append(1)
        self.assertEquals(str(l2), "{[1]}")
        l2.append(2)
        self.assertEquals(str(l2), "{[1, 2]}")

        l3 = UnrolledLinkedList(1)
        l3.append(1)
        l3.append(2)
        self.assertEquals(str(l3), "{[1], [2]}")

        try:
            l0 = UnrolledLinkedList(0)
        except ValueError as err:
            self.assertEquals(str(err), "Node capacity cannot be less than 1")

        l4 = UnrolledLinkedList(3)
        l4.append(1)
        l4.append(2)
        l4.append(3)
        l4.append(4)
        self.assertEquals(str(l4), "{[1, 2], [3, 4]}")
        l4.append(5)
        self.assertEquals(str(l4), "{[1, 2], [3, 4, 5]}")

        #Example on git hub:
        l5 = UnrolledLinkedList(4)
        for i in range(8):
            l5.append(i+1)
        self.assertEquals(str(l5), "{[1, 2], [3, 4], [5, 6, 7, 8]}")

    def test_delete_large(self):
        l = UnrolledLinkedList(6)
        for i in range(20):
            l.append(i)
        del l[4]
        self.assertEquals(str(l),'{[0, 1, 2], [3, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14], [15, 16, 17, 18, 19]}' )


    def test_delete(self):
        l = UnrolledLinkedList(4)
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)
        del l[3]
        self.assertEquals(str(l), "{[1, 2, 3]}")
        passed()
        l.append(4)
        l.append(5)
        l.append(6)
        del l[4]
        self.assertEquals(str(l), "{[1, 2], [3, 4, 6]}")
        passed()

        del l[1]
        self.assertEquals(str(l), "{[1, 3, 4], [6]}")
        passed()

        try:
            l2 = UnrolledLinkedList(2)
            l2.append(1)
            del l2[1]
            self.assert_(False) #Should never reach here....
        except IndexError as err:
            self.assertTrue(True)
            passed()

        del l[3]
        self.assertEquals(str(l), "{[1, 3, 4]}")

        l3 = UnrolledLinkedList(1)
        l3.append(1)
        l3.append(2)
        l3.append(3)
        del l3[1]
        self.assertEquals(str(l3), "{[1], [3]}")

        l3.append(4)
        del l3[0]
        self.assertEquals(str(l3), "{[3], [4]}")

        l3.append(5)
        del l3[2]
        self.assertEquals(str(l3), "{[3], [4]}")

        l = UnrolledLinkedList(3)
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)
        l.append(5)
        l.append(6)
        l.append(7)

        del l[0]

        self.assertEquals(str(l), "{[2, 3], [4, 5], [6, 7]}")


    def test_count(self):
        l = UnrolledLinkedList(3)
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)
        self.assertEquals(len(l), 4)
        l.append(5)
        self.assertEquals(len(l), 5)
        l.append(6)
        l.append(7)
        self.assertEquals(len(l), 7)

        str(l)
        del l[0]
        self.assertEquals(len(l), 6)


    def testGetIndexSimple(self):
        l = UnrolledLinkedList(4)
        for i in range(4):
            l.append(i + 1)
        self.assertEquals(l[3], 4)

    @unittest.expectedFailure
    def testGetItemOutOfRange(self):
        l = UnrolledLinkedList(5)
        for i in range(6):
            l.append(i + 1)

    def testGetItemNegativeIndex(self):
        l = UnrolledLinkedList(5)
        for i in range(5):
            l.append(i + 1)
        self.assertEquals(l[-1], 5)
        self.assertEquals(l[-5], 1)

    @unittest.expectedFailure
    def testGetNegativeIndexOutOfBounds(self):
        l = UnrolledLinkedList(5)
        for i in range(1000):
            l.append(i + 1)
        self.assertEquals(l[-1001], 1)


    def testGetIndexComplex(self):
        l = UnrolledLinkedList(4)
        for i in range(10):
            l.append(i + 1)

        self.assertEquals(l[5], 6)

    def testSetItem(self):
        l = UnrolledLinkedList(4)
        for i in range(10):
            l.append(i + 1)
        l[0] = 100
        self.assertEquals(l[0], 100)
        l[9] = -1
        self.assertEquals(l[9], -1)

    def testIter(self):
        l = UnrolledLinkedList(4)
        for i in range(10):
            l.append(i + 1)

        newList = []
        for i in l:
            newList.append(i)
        self.assertEquals(str(newList), "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")



    def testContains(self):
        l = UnrolledLinkedList(4)
        for i in range(4):
            l.append(i + 1)

        self.assertEqual(3 in l, True)
        self.assertEqual(5 in l, False)
        self.assertEqual(1 in l, True)


    def testLength(self):
        l = UnrolledLinkedList(4)
        for i in range(10):
            l.append(i + 1)

        self.assertEquals(len(l), 10)
        del l[0]
        self.assertEquals(len(l), 9)

        l1 = UnrolledLinkedList()
        self.assertEquals(len(l1), 0)

    def testReversed(self):
        l = UnrolledLinkedList(4)
        for i in range(10):
            l.append(i + 1)

        newList = []
        for i in reversed(l):
            newList.append(i)
        self.assertEquals(str(newList), "[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]")

def passed():
    print("Passed!")