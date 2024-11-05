# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        if not head.next:
            return None
        display(head)
        curr = head
        i = 0
        while curr:
            i += 1
            curr = curr.next
        if n == i:
            head = head.next
            display(head)
            return head
        i -= n + 1
        curr = head
        while curr and i > 0:
            curr = curr.next
            i -= 1
        if curr.next.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        display(head)
        return head


# Linked list template
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))

def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for value in values[1:]:
        curr.next = ListNode(value)
        curr = curr.next
    return head

if __name__ == '__main__':
    solution = Solution()

    testCase = [1,2,3,4,5]
    n = 2
    head = createLinkedList(testCase)
    solution.removeNthFromEnd(head, n)
    print("\n")

    testCase = [1, 2]
    n = 2
    head = createLinkedList(testCase)
    solution.removeNthFromEnd(head, n)
    print("\n")

    testCase = [1, 2]
    n = 1
    head = createLinkedList(testCase)
    solution.removeNthFromEnd(head, n)
    print("\n")