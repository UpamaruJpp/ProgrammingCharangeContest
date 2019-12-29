n = int(input())
a = list(map(int,input().split()))
k = int(input())

def dfs(i,s):
    if i == n:
         return s == k
    
    if dfs(i+1,s):
        return True
    
    if dfs(i+1,s + a[i]):
        return True
    
    return False

if dfs(0,0):
    print("Yes")
else:
    print("No")