# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        curr = head
        myDict = {}

        while curr:
            newNode = Node(curr.val)
            myDict[curr] = newNode
            curr = curr.next

        curr = head
        while curr:
            newNode = myDict[curr]
            newNode.next = myDict[curr.next] if curr.next else None
            newNode.random = myDict[curr.random] if curr.random else None
            curr = curr.next

        return myDict[head]




# Linked list template, with random modifications
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        elements.append(f" Random({str(curr.random)}) ")
        curr = curr.next
    print(' -> '.join(elements))

def createLinkedList(values):
    if not values:
        return None
    head = Node(values[0][0])
    curr = head
    for value in values[1:]:
        curr.next = Node(value[0])
        if value[1] is not None:
            curr.random = value[1]
        curr = curr.next
    return head

if __name__ == '__main__':
    solution = Solution()

    testCase = [[7,None],[13,0],[11,4],[10,2],[1,0]]
    head = createLinkedList(testCase)
    solution.copyRandomList(head)
    print("\n")

    testCase = [[1,1],[2,1]]
    head = createLinkedList(testCase)
    solution.copyRandomList(head)
    print("\n")

    testCase = [[3,None],[3,0],[3,None]]
    head = createLinkedList(testCase)
    solution.copyRandomList(head)
    print("\n")
