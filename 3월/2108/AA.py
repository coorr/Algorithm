sys.stdin=open("2108/input.txt","r")
from collections import Counter
import sys


n = int(sys.stdin.readline())
List=[]
for i in range(n):
    List.append(int(sys.stdin.readline()))
List.sort()
print(round(sum(List)/n))
print(List[n//2])

cnt = Counter(List).most_common()

big=cnt[0][1]
lis=[]
for x in cnt:
    if x[1] == big:
        lis.append(x)

if len(lis) != 1:
    lis =sorted(lis)
    print(lis[1][0])
else:
    print(lis[0][0])

Min=min(List)
Max=max(List)
print(Max- Min)

        
    
        