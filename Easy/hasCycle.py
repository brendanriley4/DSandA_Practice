class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        # display(head)
        # curr = head
        # mySet = set()
        # while curr:
        #     if curr in mySet:
        #         return True
        #     mySet.add(curr) # add Node itself to set, this will store memory address and not
        #                     # integer value (multiple nodes can have same val)
        #     curr = curr.next
        # return False

        # constant memory complexity solution
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


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

    testCase = [3,2,0,-4]
    head = createLinkedList(testCase)
    ans = solution.hasCycle(head)
    print(f"{ans}")

    testCase = [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
    head = createLinkedList(testCase)
    ans = solution.hasCycle(head)
    print(f"{ans}")