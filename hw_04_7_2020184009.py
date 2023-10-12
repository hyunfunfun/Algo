import random
random.seed('class_04')
words = [

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
l_arr=len(words)

def downHeap(root,size):
    ch=root*2+1 #root=0일때 왼쪽자식노드

    # pyramid of doom (if안에 if)vs early return(빠른 리턴을 해서 if를 덜 씀)
    if ch >= size: return #왼쪽자식노드가 없으면

    if ch+1 < size and words[ch] < words[ch+1]: #ch+1 = 오른쪽자식노드가 있고, 크면 교체
        ch=ch+1

    if words[root]>=words[ch]:return

    words[root],words[ch]=words[ch],words[root] #루트와 왼쪽자식노드 비교후 교체
    downHeap(ch,size) #다운힙 진행후 자식노드의 자식노드도 다운힙

for i in range(l_arr//2-1,0-1,-1):
    downHeap(i,l_arr)


heapSize=l_arr
for i in range(l_arr, 0, -1):
    heapSize-=1
    words[0], words[heapSize] = words[heapSize], words[0]
    downHeap(0,heapSize)
print(words)