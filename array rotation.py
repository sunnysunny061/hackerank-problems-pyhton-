def fun(arr,r):
    l=len(arr)-1
    for i in range(0,r):
        arr[0],arr[l]=arr[l],arr[0]


arr=list(map(int,input().input()))
r=int(input())
fun(arr,r)