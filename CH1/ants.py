l = int(input())
n = int(input())
x = list(map(int,input().split()))

"最小時間はl/2の中で最も遠い蟻が落ちるところ"
min_time = 0
for i in range(n):
    min_time = max(min_time,min(x[i],l-x[i]))

"最大時間は端から端に行く蟻"
max_time = 0
for i in range(n):
    d = abs(l - x[i])
    max_time = max(d,max_time)
print("min = ",min_time)
print("max = " ,max_time)

