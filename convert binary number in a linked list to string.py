"""Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list."""

head = [1,0,1]
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(head):
        binary = '' #initialising an empty string
        while head: #looping until head exist
            binary += str(head.val) #adding the nod val in binary using str function
            head = head.next #updating the variable
        return int(binary,2) #converting binary into a int 
