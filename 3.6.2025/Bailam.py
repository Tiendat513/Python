with open("Bai1.INP") as f:
    s1=f.readline()
    s2=f.readline()
n=len(s1)
m=len(s2)
dp=[[0]*(m+1) for i in range(n+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
i=n
j=m
res=""
while i>0 and j>0:
    if s1[i-1]==s2[j-1]:
        res+=s1[i-1]
        i-=1
        j-=1
    elif dp[i-1][j]>dp[i][j-1]:
        i-=1
    else:
        j-=1
def find(A):
    pos = []
    res1 = res[::-1]
    count = len(res)
    for i in range(len(A)+1):
        if A[i-1] == res1[len(res)-count]:
            pos.append(i)
            count -= 1
        if count == 0:
            break
    return pos
pos1=find(s1)
pos2=find(s2)
with open("Bai1.OUT","w") as fo:
    fo.write(str(dp[n][m])+"\n")
    fo.write(str(pos1)+"\n")
    fo.write(str(pos2))