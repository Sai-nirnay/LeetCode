class Solution(object):
    def isPalindrome(self, x):
       
        li = []

        for i in str(x):
            li.append(i)

        if len(li)%2==0:
            li1 = li[:len(li)//2]
            li2 = li[len(li)//2:]
        else:
            lix = li
            lix.pop(len(lix)//2)
            li1 = lix[:len(lix)//2]
            li2 = lix[len(lix)//2:]

        if li1 == li2[::-1]:
            return True
        else:
            return False
