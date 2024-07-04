class Memoization:
    def __init__(self):
        self.memo={}
    def memoization_fibonacci(self,n):
        if n in self.memo.keys():
            return self.memo[n]
        if n<=2:
            return 1
        else:
            self.memo[n] = self.memoization_fibonacci(n-1)+self.memoization_fibonacci(n-2)
            return self.memo[n]


mem = Memoization()

print(mem.memoization_fibonacci(6))
