inpf = open("input2.txt", "r")
outf = open("output2.txt", "w")
n = int(inpf.readline()) 

arr = list(map(int, inpf.readline().strip().split(" ")))

def get_Max(arr):
    size=len(arr)
    if size == 1:
        return -9999
    if size == 2:
        return arr[0] + arr[1] ** 2

    if size>2:
        mid=size // 2
        left= get_Max(arr[:mid])
        right=get_Max(arr[mid:])

        left_max=arr[0]
        for i in range(0,mid):
            if arr[i]>left_max:
                left_max=arr[i]


        right_max=arr[mid]**2
        for i in range(mid+1,size):
            if arr[i]**2>right_max:
                right_max=arr[i]**2

        cross =left_max+right_max

        return max(left,right,cross)



outf.write(str(get_Max(arr)))
outf.close()
print("me")

