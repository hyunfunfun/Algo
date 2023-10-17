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

def merge(start,mid,end):
    merged=[]
    l,r=start,mid+1
    while l<= mid and r<=end: #A반에 선수있따 and B반에 선수있다
        if array[l]<=array[r]: #싸움붙여서 A반 선수가 지거나 비기면
            merged.append(array[l]) #A반 선수 줄서있어
            l +=1
        else:
            merged.append(array[r])#B반 선수 줄서있어
            r+=1
    if l<=mid:
        merged+=array[l:mid+1] #남아있는 A반 merged로
        array[start:end+1]=merged
    else:
        array[start:r] = merged

def mergeSort(start, end): #end:inClusive (끝 포함)
    # size=end-start+1
    # if size <=1:return  #배열의 개수가 1이될때까지 나누기
    if start >=end:return

    mid=(start+end)//2
    mergeSort(start, mid) #왼쪽절반 sort   #mid 는 왼쪽그룹의 마지막
    mergeSort(mid+1, end) #오른쪽절반 sort
    merge(start,mid,end) #합체

mergeSort(0,l_arr-1)
print(array)
