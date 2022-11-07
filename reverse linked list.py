"""Given the head of a singly linked list, reverse the list, and return the reversed list."""

def reverseList(self, head):
        prev = None #initialising the variable
        while head:
            curr = head #curr stores the head value
            head = head.next #head stores the next value
            curr.next = prev #curr.next pointing to prev
            prev=curr #now updating the prev variable
        return prev