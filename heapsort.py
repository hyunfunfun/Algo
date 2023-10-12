import random
random.seed('class_04')
array=[random.randrange(100) for _ in range(30)]
l_arr=len(array)
print(array)

# array=list(map(lambda e:(-e,e), array))
# print(array)
# import heapq
# heapq.heapify(array)
# print(array)

def downHeap(root,size):
    ch=root*2+1 #root=0일때 왼쪽자식노드

    # pyramid of doom (if안에 if)vs early return(빠른 리턴을 해서 if를 덜 씀)
    if ch >= size: return #왼쪽자식노드가 없으면

    if ch+1 < size and array[ch] < array[ch+1]: #ch+1 = 오른쪽자식노드가 있고, 크면 교체
        ch=ch+1

    if array[root]>=array[ch]:return

    array[root],array[ch]=array[ch],array[root] #루트와 왼쪽자식노드 비교후 교체
    downHeap(ch,size) #다운힙 진행후 자식노드의 자식노드도 다운힙

for i in range(l_arr//2-1,0-1,-1):
    downHeap(i,l_arr)

print(array)

heapSize=l_arr
for i in range(l_arr, 0, -1):
    heapSize-=1
    array[0], array[heapSize] = array[heapSize], array[0]
    downHeap(0,heapSize)
print(array)