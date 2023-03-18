import numpy

n,m=input().split()
n=int(n)    #物品个数
m=float(m)    #背包容量
m=int(m*100)
dp=numpy.zeros((n+1,m+1)) #dp[i][j]=max(dp[i-1][j],dp[i-1][j-w]+p)

for i in range(1,n+1):
    w,p=map(float,input().split())
    for j in range(0,m+1):
        if j>=int(w*100):
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-int(w*100)]+p)
        else:
            dp[i][j]=dp[i-1][j]
#print(dp)
print("%.5f" %dp[n][m])