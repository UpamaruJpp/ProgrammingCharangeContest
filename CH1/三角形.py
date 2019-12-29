n = int(input())
li = input().split()

ans = 0
for i in range(len(li)):
    for j in range(i+1,len(li)):
        for k in range(j+1,len(li)):
            shu = int(li[i]) + int(li[j]) + int(li[k])
            ma = max(int(li[k]),max(int(li[i]),int(li[j])))
            re = shu - ma
            if ma<re:
                ans = max(ans,shu)
print(ans)
