class memoization:
    def __init__(self):
        self.dp={}

    def gridTravelerProb(self,m,n):
        k = str(m) + ',' + str(n)
        if k in self.dp.keys():
            return self.dp[k]
        if n==1 and m==1:
            return 1
        elif m==0 or n==0:
            return 0
        else:
            self.dp[k]=self.gridTravelerProb(m-1,n)+self.gridTravelerProb(m,n-1)
            return self.dp[k]

memo=memoization()
print(memo.gridTravelerProb(2,3))
