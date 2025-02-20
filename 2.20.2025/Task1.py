def longest(num):
    tails=[]
    for i in num:
        if not tails or i>tails[-1]:
            tails.append(num) 
        else:
            l,r=0,len(tails)-1
            while l<=r:
                mid=(l+r)//2
                if tails[mid]<num:
                    l=mid+1
                else:
                    r=mid-1
            tails[l]=num
    return len(tails)
num=[3,10,2,1,20]
print(do_dai= longest(num))
