import random
random.seed('class_04')
array=[random.randrange(15) for _ in range(100)]
l_arr=len(array)
maxv=max(array)
print(array,maxv)
counts=[0 for _ in range(maxv+1)] #최댓값까지의 배열생성
print(counts,len(counts))
for v in array:
    counts[v]+=1 #각 값에 맞는 배열에 1증가
print(counts,len(counts))

for i in range(len(counts)-1): #카운트된 배열을 인덱스로 바꾸기위해 각 배열의 값 더하기
    counts[i+1]+=counts[i]
print(counts,len(counts))

#results=[0 for _ in range(l_arr)] #l_arr만큼 배열생성
#results=[0]*l_arr #l_arr만큼 배열생성
results=array[:] #array를 복사 results=array를 하게되면 복사가 아닌 공유느낌
for i in range(l_arr-1,0-1,-1): #배열인덱스만큼 다시 array에 넣기
    v=array[i]
    counts[v]-=1
    ri=counts[v]
    results[ri]=v

print(results)