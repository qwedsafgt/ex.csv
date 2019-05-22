class csv:
    def __init__(self,filename):
        self.csvfile=open(filename,"r")

    def judge_csv(self):
        a=self.csvfile.read()
        global arr
        arr=a.split()
        b=arr[0]
        c=b.split()
        n=["Name","Age","No"]
        if len(a and n) > 0:
            for a in arr:
                print(a)
        else:
             exit(0)




cat=csv("ex0_sample.csv")
cat.judge_csv()
