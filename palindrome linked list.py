"""Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise."""



def isPalindrome(head):
    prev = None #initialising the variables
    slow = head #slow pointer on head
    fast = head #fast pointer on head

    while fast and fast.next: #looping until fast pointer exist i.e not equals to none
        fast = fast.next.next # moving fast pointer two positions
        slow = slow.next # moving slow pointer one positions
    
    #after fast pointer reaches none, slow pointer reaches in the middle of the linked list
    #reversing the second half of the linked list using slow pointer
    while slow: # looping until slow pointer reaches none
        temp = slow.next # storing the slow.next value in temprory variable because we are about to break the link between
        slow.next = prev # now slow.next pointing to none breaking the link to the next link
        prev = slow #updating the prev value to the slow pointer value
        slow = temp #storing the temprory value into slow so it can be used for the next iteration

    #after reversing the second half of the linked list we are againg using two pointers from the opposite directions to check whether their values are equal or not
    left,right = head,prev  #iniatilising the variables

    while right: #looping until right pointer reaches none
        if left.val != right.val: #checking if right and left values equal to each other or not
            return False #if not then return false
        
        left = left.next #updating the variable to next node
        right = right.next #updating the variable to next node

    return True #returning true if everything turns out fine