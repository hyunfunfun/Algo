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

import heapdict
D = heapdict.heapdict()
g = { s:dict() for s in range(num_vertex)  }
for s,e,d in edges:
  g[s][e] = d # g[s].append({e:d})
  g[e][s] = d
#print(g)
origins = dict()
completed = set()

startIndex = 4

D[startIndex] = 0
origins [startIndex] = startIndex

#main loop
while D:
  e,d = D.popitem() #가장 싼 순서대로 
  completed.add(e)
  s = origins[e]
  for a,w in g[e].items():
    if a in completed: continue 
    if not a in D or D[a] > d + w: 
      D[a] = d + w
      origins[a] = e

for i in range(num_vertex):
  path = str(i)
  dist = 0
  while True:
    o = origins[i]
    if o == i: break
    dist += g[i][o]
    path = f'{o}-{path}'
    i = o
  print(f'{path},({dist})')


