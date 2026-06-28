class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        leni = 200
        for i in strs:
            if len(i)<leni:
                leni = len(i)
        lists = [] 
        listf = []   
        for m in range(leni):
            for l in strs:
                lists.append(l[m])
            if len(set(lists))==1:
                listf.append(lists[0])
                lists = [] 
            else:
                if len(listf)==0:
                    return ""
                else:
                     break 
        return "".join(listf)
