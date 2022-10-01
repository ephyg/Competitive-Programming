class Solution:
    def sortSentence(self, s: str) -> str:
        Splited_list=s.split()
        Indexes_=[]
        string_=[]
        Answer=[""]*len(Splited_list)
        for i in range(len(Splited_list)):
            x=Splited_list[i]
            Indexes_.append(x[-1])
            z=x.replace(x[-1],"")
            string_.append(z)
        Indexes_=[int(i) for i in Indexes_]
        for i in range(len(Splited_list)):
            Answer[Indexes_[i]-1]=string_[i]
        Ans_In_Str=""
        for i in Answer:
            Ans_In_Str+=i+" "
        Ans_In_Str=Ans_In_Str[:len(Ans_In_Str)-1]
        return Ans_In_Str