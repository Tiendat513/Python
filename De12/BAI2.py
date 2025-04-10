def checkdx(S):
    DX=False
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            DX=True
            break
    return DX


n=int(input())
for i in range(n):
    S=input()
    if checkdx(S) == True:
        print("YES")
    else:
        print("NO")