import random

random.seed('class_04')
array = [

  '2020184009', 'hut', 'apostle', 'equipment', 'fop', 'refined', 'parapet', 'mog', 'amputate', 'covetous', 'somebody',

  'all', 'lobbyist', 'remark', 'subscriber', 'quorum', 'steppe', 'clean', 'cu', 'commend', 'prosy',

  'supererogation', 'indignation', 'wolverine', 'emporium', 'intersect', 'constitution', 'miscast', 'rabbi', 'enmity', 'loft',

  'temporize', 'speedboat', 'agenda', 'delusion', 'class04', 'idolize', 'romance', 'overestimate', 'revive', 'smell',

  'modem', 'splat', 'snaky', 'drawn', 'smoke', 'darky', 'lotus', 'mufti', 'pithy', 'jewel', 'nexus',

  'fluff', 'piton', 'finis', 'drake', 'caulk', 'pussy', 'bless', 'weeds', 'realm', 'swoon', 'thorn',

  'plant', 'aorta', 'cupid', 'wafer', 'jewry', 'sinus', 'proud', 'grape', 'cable', 'carer', 'pearl',

  'piece', 'party', 'sleet', 'palmy', 'oiled', 'synod', 'trove', 'voice', 'chest', 'story', 'range',

  'scout', 'sewer', 'lowly', 'usher', 'seine', 'gulch', 'fever', 'frith', 'pylon', 'wager', 'banns',

  'merit', 'cheap', 'booby', 'truss', 'codex', 'sepia', 'totem', 'poult', 'dregs', 'giddy', 'umber',

  'mooch', 'smarm', 'loath', 'spoil', 'drink', 'wrick', 'awake', 'mural', 'glide', 'pinch', 'thine',

  'tawny', 'swede', 'shier', 'satan', 'triad', 'splay', 'tacit',

]
#array=[random.randrange(100) for _ in range(30)]
l_arr=len(array)
print(array, l_arr)

def partition(arr,beg,end):
    ri=random.randrange(beg,end)
    arr[beg],arr[ri]=arr[ri],arr[beg]

    pv=arr[beg]

    p,q=beg,end
    while True:
        while True: #p증가
            p+=1
            if p>=q:break
            if arr[p]<pv:break
        while True: #q증가
            q-=1
            if p > q:break
            if arr[q] >= pv:break
        if p>=q:break
        arr[p],arr[q]=arr[q],arr[p]

    arr[q],arr[beg]=arr[beg],arr[q]
    return q
def quickSort(arr, beg, end): #end:exclusive (끝 불포함)
    size=end-beg
    if size <= 1: return
    pi = partition(arr,beg,end) #피벗값 설정
    quickSort(arr,beg,pi)
    quickSort(arr,pi+1,end)

quickSort(array,0,l_arr) #mergesort와 다른방법으로 배열 전달해보기
print(array)