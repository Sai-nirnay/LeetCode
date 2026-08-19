class Solution(object):
    def lengthOfLastWord(self, s):
        wordsize = 0
        for i in range (len(s) -1 , -1, -1):
            if s[i] == " ":
                if wordsize == 0:
                    continue
                else:
                    break
            else:
                wordsize += 1
        return wordsize

   
        
