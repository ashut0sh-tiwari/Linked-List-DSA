"""Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well."""

#function to delete the duplicates nodes in the linked list
class Solution:
    def deleteDuplicates(self, head):
        #initialising the variable
        curr =head
        #using while loop until curr value exist
        while curr:
            #if curr value matches its next node value then skip that node
            if curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        return head