"""Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node."""

def middleNode(head): #function to find the middle node of a linked list
        slow = head  #initialising the variable
        fast = head #initialising the variable

        while fast and fast.next: #looping until fast.next exist
            slow = slow.next #moving slow pointer one step
            fast = fast.next.next #moving fast pointer two step
        return slow #returning slow because when fast pointer reaches the last node then slow pointer will reach half of its distance as fast pointer moving with double speed as of slow pointer