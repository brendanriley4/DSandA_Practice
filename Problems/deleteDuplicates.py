class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        display(head)
        curr = head
        ahead = curr.next # unnecessary memory usage
        while ahead:
            if ahead.val <= curr.val:
                curr.next = ahead.next
                ahead = ahead.next
            else:
                ahead = ahead.next
                curr = curr.next
        display(head)


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

    testCase = [1]
    head = createLinkedList(testCase)
    solution.deleteDuplicates(head)

    testCase = [1,1,2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 100, 100, 101]
    head = createLinkedList(testCase)
    solution.deleteDuplicates(head)
