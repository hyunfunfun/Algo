edges = [ 
  (0, 7, 450), (0, 16, 90), (0, 17, 191), (1, 8, 236), (1, 11, 322), 
  (1, 15, 279), (2, 5, 394), (2, 6, 248), (2, 12, 373), (3, 5, 521), 
  (3, 14, 461), (4, 5, 130), (4, 10, 458), (4, 11, 321), (4, 12, 164), 
  (4, 14, 149), (5, 8, 474), (5, 10, 361), (5, 11, 348), (5, 14, 218), 
  (6, 10, 450), (7, 11, 241), (7, 15, 453), (7, 16, 437), (8, 15, 515), 
  (9, 11, 440), (9, 13, 458), (9, 15, 239), (9, 16, 514), (9, 17, 500), 
  (10, 12, 294), (12, 14, 178), (15, 16, 276), (15, 17, 269), 
]
num_vertex = 18

roots = [ i for i in range(num_vertex)]

def getRoot(v):
  r = roots[v]
  if r == v: return r
  roots[v] = getRoot(r)
  return roots[v]

def connectNodes(v1, v2):
  r1 = getRoot(v1)
  r2 = getRoot(v2)
  roots[v1] = v2

mst = []

# edges.sort()
# sorted_edges = edges.sorted()
sorted_edges = sorted(edges, key=lambda e: e[2]) #e는 튜플, e[2]는 2번째 (0,7,450)에서는 450 

# for은 몇번 루프할 것인지 알 때, while은 몇번 루프를 돌지는 모르겠지만 조건에 의해서 반복할 때. 돌고있는데 mst가 완료가 될 때 까지 돌겠다면 while

for edge in sorted_edges: #edge는 start end를 갖는 튜플
  if getRoot(edge[0]) == getRoot(edge[1]): continue
  mst.append(edge) 
  if len(mst) == num_vertex - 1: break
  connectNodes(edge[0], edge[1])



print(mst)



