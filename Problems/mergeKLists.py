from typing import List, Optional
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = [] # heapq defaults to min heap
        for i, node in enumerate(lists): # enumerates over the heads of the linked lists
            if node: # heads can be empty, don't push empty ones to the heap
                heapq.heappush(min_heap, (node.val, i, node)) # we need to push node.val in order to use it to sort the heap 

        ans = ListNode() # return value, hold empty pointer to first element
        curr = ans
        while min_heap: # while there are still elements in the heap
            val, i, node = heapq.heappop(min_heap) # pop the head on the min_heap
            curr.next = node # attach newly popped node to the linked list
            curr = node # move curr pointer to said node
            node = node.next # move node pointer to next element in the linked list
            if node: # if this is not none, we must push back onto min_heap in order to sort relevant to the other elements
                heapq.heappush(min_heap, (node.val, i, node))

        return ans.next # once the min_heap is empty, ans.next points to its heap



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

    testCase = [[1,4,5],[1,3,4],[2,6]]
    i = 0
    head = []
    while i < len(testCase):
        head.append(createLinkedList(testCase[i]))
        i += 1
    solution.mergeKLists(head)