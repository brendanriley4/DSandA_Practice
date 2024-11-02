class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        display(list1)
        display(list2)
        if not list1:
            return list2
        if not list2:
            return list1
        curr1 = list1
        curr2 = list2
        if curr1.val < curr2.val:
            head = curr1
            merged = curr1
            curr1 = curr1.next
        else:
            head = curr2
            merged = curr2
            curr2 = curr2.next
        while curr1 and curr2:
            if curr1.val < curr2.val:
                merged.next = curr1
                curr1 = curr1.next
            else:
                merged.next = curr2
                curr2 = curr2.next
            merged = merged.next
        merged.next = curr1 if curr1 else curr2
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

    testCase = [1,2,4]
    testCaseb = [1,3,4]
    head = createLinkedList(testCase)
    headb = createLinkedList(testCaseb)
    solution.mergeTwoLists(head, headb)

    testCase = []
    testCaseb = [0]
    head = createLinkedList(testCase)
    headb = createLinkedList(testCaseb)
    solution.mergeTwoLists(head, headb)