class Solution(object):
    def lengthOfLastWord(self, s):
        s_ = s.strip()
        if " " not in s_:
            return len(s_)
        sind = 0
        for i in s_:
            if i == " ":
                sind = s_.index(i)
                s_ = s_.replace(i,"_",1)
        return len(s_)-sind-1
   
        
