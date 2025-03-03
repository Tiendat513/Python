n=10
S=[1,2,3,4,5,6,7,8,9,10]
count=[0]*(n+2)

pos=[0]*(n+2)
pos[0]=1
S.insert(0, -10**9)
S.append(-10**9)
for i in range(1,n+2):
    for j in range(i):
        if S[i]>S[j] and count[i]<count[j]+1:
            count[i]=count[j]+1
            pos[i]=j
print(pos, end="\n")
print(count)
