A=[12, 124,-6235,12315,136634,-12543,219847,124]
A.sort()
      
with open("MINP.out","w")as out:
    if A[0]<0 and abs(A[1])>abs(A[len(A)-1]):
        out.writelines(str(A[0]*A[1]))
    else:
        out.writelines(str(A[0]*A[len(A)-1]))