input = """268, 273
211, 325
320, 225
320, 207
109, 222
267, 283
119, 70
138, 277
202, 177
251, 233
305, 107
230, 279
243, 137
74, 109
56, 106
258, 97
248, 346
71, 199
332, 215
208, 292
154, 80
74, 256
325, 305
174, 133
148, 51
112, 71
243, 202
136, 237
227, 90
191, 145
345, 133
340, 299
322, 256
86, 323
341, 310
342, 221
50, 172
284, 160
267, 142
244, 153
131, 147
245, 323
42, 241
90, 207
245, 167
335, 106
299, 158
181, 186
349, 286
327, 108""".split("\n")

k = [n.split(", ") for n in input]
map = [(-1,9999)] * (400 * 400)

for n, (x, y) in enumerate(k):
  for i in range(0,400):
    for j in range(0,400):
      dist = abs(i - int(x)) + abs(j - int(y))
      if map[i + j * 400][1] > dist:
        map[i + j * 400] = (n, dist)
      elif map[i + j * 400][1] == dist:
        map[i + j * 400] = ('X', dist)

from collections import defaultdict
counts = defaultdict(int)
for o in map: 
  counts[o[0]] += 1

counts = [(y,x) for x,y in counts.items()]
counts = sorted(counts)
counts.reverse()

edges = set([m[0] for m in (map[0:400] + map[159600:160000] + map[0:160000:400] + map[399:160000:400])])

counts = [c for c in counts if c[0] not in edges]
print("part1: {}".format(counts))


map = [0] * (400 * 400)
for n, (x, y) in enumerate(k):
  for i in range(0,400):
    for j in range(0,400):
      dist = abs(i - int(x)) + abs(j - int(y))
      map[i + j * 400] += dist

safespots = [o for o in map if o < 10000]
len(safespots)

