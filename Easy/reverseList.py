class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        display(head)
        if not head.next:
            return head
        curr = head
        ahead = head.next
        curr.next = None
        if not ahead.next:
            ahead.next = curr
            display(ahead)
            return ahead
        wayAhead = ahead.next
        while wayAhead:
            ahead.next = curr
            curr = ahead
            ahead = wayAhead
            wayAhead = wayAhead.next
        ahead.next = curr
        display(ahead)
        return ahead





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
    head = createLinkedList(testCase)
    solution.reverseList(head)

    testCase = [1,2]
    head = createLinkedList(testCase)
    solution.reverseList(head)