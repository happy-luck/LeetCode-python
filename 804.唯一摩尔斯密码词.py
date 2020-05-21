class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dic = {'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
        res = []
        for i in range(len(words)):
            string = ''
            for s in words[i]:
                string += dic[s]
            if string not in res:
                res.append(string)
        return len(res)