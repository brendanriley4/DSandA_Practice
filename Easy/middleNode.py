class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head.next:
            return head
        len = 0
        curr = head
        while curr: # Can also do this with fast and slow pointers
            len += 1
            curr = curr.next
        while len // 2 > 0:
            len -= 1
            head = head.next
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

    testCase = [3]
    head = createLinkedList(testCase)
    ans = solution.middleNode(head)
    print(f"{ans}")

    testCase = [1,2,3,4,5]
    head = createLinkedList(testCase)
    ans = solution.middleNode(head)
    print(f"{ans}")