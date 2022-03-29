
import sys
sys.stdin=open("1181/input.txt","r")



n=int(input())
List=[]
for i in range(n):
    List.append(sys.stdin.readline().strip())
List_set=set(List)
List_list=list(List_set)

List_list.sort()
List_list.sort(key=len)
# List_list.sort(key=len)

for x in List_list:
    print(x)