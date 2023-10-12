import random
random.seed('class_04')
array=[random.randrange(1000) for _ in range(10)]
l_arr=len(array)
maxv=max(array)
print(array,maxv)

results = array[:]

div=1
while div<=maxv: #제일큰값으 자릿수까지 올림
    counts = [0 for _ in range(10)] #자릿수동 10개의 배열 생성
    for v in array:
        digit=v//div%10
        counts[digit]+=1

    for i in range(len(counts) - 1):  # 카운트된 배열을 인덱스로 바꾸기위해 각 배열의 값 더하기
        counts[i + 1] += counts[i]

    for i in range(l_arr - 1, 0 - 1, -1):  # 배열인덱스만큼 다시 array에 넣기
        v = array[i]
        digit = v // div % 10
        counts[digit] -= 1
        ri = counts[digit]
        results[ri] = v
    array=results[:]
    print(results,div)

    div *=10

exit()
