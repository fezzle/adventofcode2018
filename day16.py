
opcode_samples = """Before: [2, 1, 1, 0]
10 1 3 1
After:  [2, 1, 1, 0]

Before: [1, 1, 3, 3]
6 1 0 0
After:  [1, 1, 3, 3]

Before: [2, 1, 2, 2]
14 1 3 0
After:  [0, 1, 2, 2]

Before: [1, 2, 2, 3]
1 0 2 2
After:  [1, 2, 0, 3]

Before: [2, 2, 3, 2]
12 0 2 3
After:  [2, 2, 3, 2]

Before: [1, 1, 0, 1]
13 3 3 2
After:  [1, 1, 0, 1]

Before: [1, 1, 2, 1]
15 3 2 3
After:  [1, 1, 2, 1]

Before: [2, 1, 1, 0]
8 2 1 2
After:  [2, 1, 0, 0]

Before: [1, 1, 1, 2]
8 2 1 3
After:  [1, 1, 1, 0]

Before: [0, 3, 1, 1]
0 0 0 2
After:  [0, 3, 0, 1]

Before: [1, 1, 1, 1]
6 1 0 2
After:  [1, 1, 1, 1]

Before: [3, 1, 2, 0]
10 1 3 1
After:  [3, 1, 2, 0]

Before: [1, 2, 2, 1]
1 0 2 2
After:  [1, 2, 0, 1]

Before: [2, 1, 3, 3]
12 0 2 3
After:  [2, 1, 3, 2]

Before: [0, 1, 1, 3]
7 2 3 1
After:  [0, 0, 1, 3]

Before: [1, 1, 2, 3]
2 1 2 2
After:  [1, 1, 0, 3]

Before: [3, 1, 3, 2]
14 1 3 2
After:  [3, 1, 0, 2]

Before: [1, 1, 1, 0]
6 1 0 2
After:  [1, 1, 1, 0]

Before: [1, 3, 0, 3]
9 0 2 0
After:  [0, 3, 0, 3]

Before: [0, 3, 2, 0]
3 2 1 1
After:  [0, 1, 2, 0]

Before: [3, 1, 2, 0]
2 1 2 3
After:  [3, 1, 2, 0]

Before: [0, 3, 0, 0]
0 0 0 3
After:  [0, 3, 0, 0]

Before: [2, 1, 2, 3]
2 1 2 3
After:  [2, 1, 2, 0]

Before: [1, 1, 3, 1]
6 1 0 2
After:  [1, 1, 1, 1]

Before: [0, 1, 2, 1]
15 3 2 3
After:  [0, 1, 2, 1]

Before: [1, 1, 2, 2]
2 1 2 2
After:  [1, 1, 0, 2]

Before: [1, 2, 2, 0]
1 0 2 1
After:  [1, 0, 2, 0]

Before: [1, 1, 0, 2]
6 1 0 2
After:  [1, 1, 1, 2]

Before: [2, 2, 3, 2]
12 3 2 0
After:  [2, 2, 3, 2]

Before: [1, 0, 2, 2]
11 2 2 2
After:  [1, 0, 2, 2]

Before: [2, 2, 0, 3]
7 1 3 3
After:  [2, 2, 0, 0]

Before: [1, 1, 3, 1]
6 1 0 0
After:  [1, 1, 3, 1]

Before: [2, 1, 2, 1]
9 1 3 1
After:  [2, 1, 2, 1]

Before: [2, 1, 1, 0]
4 0 1 3
After:  [2, 1, 1, 1]

Before: [2, 0, 0, 3]
8 0 1 1
After:  [2, 1, 0, 3]

Before: [0, 1, 2, 2]
14 1 3 2
After:  [0, 1, 0, 2]

Before: [2, 1, 3, 2]
12 3 2 1
After:  [2, 2, 3, 2]

Before: [1, 1, 0, 1]
6 1 0 3
After:  [1, 1, 0, 1]

Before: [0, 0, 2, 0]
0 0 0 0
After:  [0, 0, 2, 0]

Before: [1, 1, 2, 1]
1 0 2 2
After:  [1, 1, 0, 1]

Before: [0, 2, 2, 1]
0 0 0 1
After:  [0, 0, 2, 1]

Before: [3, 2, 0, 3]
8 0 2 3
After:  [3, 2, 0, 1]

Before: [3, 1, 2, 1]
2 1 2 1
After:  [3, 0, 2, 1]

Before: [3, 1, 0, 2]
14 1 3 0
After:  [0, 1, 0, 2]

Before: [3, 2, 2, 0]
11 2 2 3
After:  [3, 2, 2, 2]

Before: [0, 2, 2, 2]
0 0 0 2
After:  [0, 2, 0, 2]

Before: [1, 3, 2, 3]
11 2 2 3
After:  [1, 3, 2, 2]

Before: [2, 0, 2, 1]
15 3 2 3
After:  [2, 0, 2, 1]

Before: [0, 3, 0, 3]
0 0 0 2
After:  [0, 3, 0, 3]

Before: [1, 1, 2, 2]
1 0 2 0
After:  [0, 1, 2, 2]

Before: [1, 2, 3, 2]
12 1 2 3
After:  [1, 2, 3, 2]

Before: [3, 1, 1, 3]
5 3 0 2
After:  [3, 1, 1, 3]

Before: [0, 1, 1, 2]
0 0 0 2
After:  [0, 1, 0, 2]

Before: [0, 1, 2, 1]
9 1 3 3
After:  [0, 1, 2, 1]

Before: [0, 1, 2, 3]
2 1 2 3
After:  [0, 1, 2, 0]

Before: [3, 1, 2, 2]
14 1 3 2
After:  [3, 1, 0, 2]

Before: [2, 3, 3, 0]
3 0 1 3
After:  [2, 3, 3, 1]

Before: [3, 3, 2, 3]
5 3 0 1
After:  [3, 1, 2, 3]

Before: [2, 1, 2, 1]
13 3 3 3
After:  [2, 1, 2, 0]

Before: [1, 1, 2, 1]
8 3 1 3
After:  [1, 1, 2, 0]

Before: [1, 2, 0, 0]
9 0 2 0
After:  [0, 2, 0, 0]

Before: [2, 1, 1, 0]
10 1 3 3
After:  [2, 1, 1, 1]

Before: [3, 1, 1, 2]
14 1 3 3
After:  [3, 1, 1, 0]

Before: [1, 2, 3, 2]
12 3 2 3
After:  [1, 2, 3, 2]

Before: [3, 1, 1, 3]
7 2 3 2
After:  [3, 1, 0, 3]

Before: [1, 2, 0, 0]
9 0 2 1
After:  [1, 0, 0, 0]

Before: [1, 2, 3, 3]
12 1 2 2
After:  [1, 2, 2, 3]

Before: [1, 1, 2, 2]
11 2 2 0
After:  [2, 1, 2, 2]

Before: [1, 1, 0, 1]
6 1 0 2
After:  [1, 1, 1, 1]

Before: [1, 1, 1, 1]
6 1 0 0
After:  [1, 1, 1, 1]

Before: [3, 1, 1, 3]
5 3 0 0
After:  [1, 1, 1, 3]

Before: [2, 1, 1, 3]
4 0 1 0
After:  [1, 1, 1, 3]

Before: [2, 1, 2, 2]
14 1 3 2
After:  [2, 1, 0, 2]

Before: [0, 1, 3, 1]
9 1 3 3
After:  [0, 1, 3, 1]

Before: [2, 1, 1, 1]
9 1 3 2
After:  [2, 1, 1, 1]

Before: [1, 1, 3, 3]
6 1 0 2
After:  [1, 1, 1, 3]

Before: [1, 3, 2, 1]
15 3 2 2
After:  [1, 3, 1, 1]

Before: [2, 3, 2, 1]
15 3 2 1
After:  [2, 1, 2, 1]

Before: [3, 2, 3, 3]
12 1 2 3
After:  [3, 2, 3, 2]

Before: [0, 1, 3, 0]
10 1 3 2
After:  [0, 1, 1, 0]

Before: [0, 0, 3, 2]
0 0 0 3
After:  [0, 0, 3, 0]

Before: [0, 1, 0, 1]
13 3 3 1
After:  [0, 0, 0, 1]

Before: [0, 0, 2, 3]
7 2 3 0
After:  [0, 0, 2, 3]

Before: [2, 2, 3, 0]
12 0 2 3
After:  [2, 2, 3, 2]

Before: [0, 1, 2, 1]
9 1 3 0
After:  [1, 1, 2, 1]

Before: [3, 0, 2, 0]
4 0 2 1
After:  [3, 1, 2, 0]

Before: [3, 3, 2, 1]
4 0 2 0
After:  [1, 3, 2, 1]

Before: [2, 1, 1, 2]
4 0 1 2
After:  [2, 1, 1, 2]

Before: [2, 1, 3, 2]
14 1 3 3
After:  [2, 1, 3, 0]

Before: [0, 2, 2, 1]
15 3 2 2
After:  [0, 2, 1, 1]

Before: [2, 1, 3, 1]
5 2 3 3
After:  [2, 1, 3, 0]

Before: [3, 1, 0, 1]
9 1 3 1
After:  [3, 1, 0, 1]

Before: [2, 1, 2, 2]
14 1 3 1
After:  [2, 0, 2, 2]

Before: [0, 1, 0, 0]
10 1 3 2
After:  [0, 1, 1, 0]

Before: [1, 1, 2, 1]
6 1 0 0
After:  [1, 1, 2, 1]

Before: [1, 0, 0, 1]
9 0 2 0
After:  [0, 0, 0, 1]

Before: [1, 1, 2, 1]
13 3 3 0
After:  [0, 1, 2, 1]

Before: [3, 1, 1, 1]
9 1 3 2
After:  [3, 1, 1, 1]

Before: [0, 1, 1, 1]
9 1 3 2
After:  [0, 1, 1, 1]

Before: [2, 0, 0, 2]
8 0 1 3
After:  [2, 0, 0, 1]

Before: [1, 0, 2, 2]
1 0 2 1
After:  [1, 0, 2, 2]

Before: [1, 1, 2, 2]
2 1 2 1
After:  [1, 0, 2, 2]

Before: [3, 3, 2, 3]
5 3 0 3
After:  [3, 3, 2, 1]

Before: [3, 1, 0, 2]
14 1 3 1
After:  [3, 0, 0, 2]

Before: [2, 1, 3, 3]
8 2 0 2
After:  [2, 1, 1, 3]

Before: [0, 1, 2, 0]
10 1 3 2
After:  [0, 1, 1, 0]

Before: [3, 2, 2, 1]
15 3 2 3
After:  [3, 2, 2, 1]

Before: [2, 0, 1, 2]
8 0 1 0
After:  [1, 0, 1, 2]

Before: [2, 3, 0, 1]
13 3 3 1
After:  [2, 0, 0, 1]

Before: [2, 1, 3, 1]
5 2 3 2
After:  [2, 1, 0, 1]

Before: [0, 1, 2, 1]
2 1 2 2
After:  [0, 1, 0, 1]

Before: [2, 1, 2, 2]
2 1 2 0
After:  [0, 1, 2, 2]

Before: [3, 1, 1, 0]
10 1 3 0
After:  [1, 1, 1, 0]

Before: [2, 1, 1, 2]
4 0 1 3
After:  [2, 1, 1, 1]

Before: [2, 1, 0, 2]
14 1 3 3
After:  [2, 1, 0, 0]

Before: [2, 1, 0, 3]
7 1 3 2
After:  [2, 1, 0, 3]

Before: [1, 3, 1, 1]
13 2 3 1
After:  [1, 0, 1, 1]

Before: [0, 2, 2, 1]
15 3 2 1
After:  [0, 1, 2, 1]

Before: [0, 3, 1, 1]
13 2 3 3
After:  [0, 3, 1, 0]

Before: [0, 2, 3, 2]
12 3 2 3
After:  [0, 2, 3, 2]

Before: [1, 3, 2, 0]
1 0 2 2
After:  [1, 3, 0, 0]

Before: [2, 0, 2, 2]
11 2 2 3
After:  [2, 0, 2, 2]

Before: [1, 0, 0, 2]
9 0 2 2
After:  [1, 0, 0, 2]

Before: [1, 1, 2, 1]
2 1 2 1
After:  [1, 0, 2, 1]

Before: [3, 2, 2, 2]
3 2 0 0
After:  [1, 2, 2, 2]

Before: [1, 1, 3, 2]
6 1 0 1
After:  [1, 1, 3, 2]

Before: [1, 1, 2, 0]
6 1 0 0
After:  [1, 1, 2, 0]

Before: [1, 1, 0, 2]
13 3 3 3
After:  [1, 1, 0, 0]

Before: [0, 3, 1, 1]
13 2 3 0
After:  [0, 3, 1, 1]

Before: [0, 2, 3, 1]
0 0 0 1
After:  [0, 0, 3, 1]

Before: [0, 1, 2, 0]
10 1 3 3
After:  [0, 1, 2, 1]

Before: [1, 2, 2, 2]
5 2 1 0
After:  [1, 2, 2, 2]

Before: [1, 1, 0, 2]
6 1 0 1
After:  [1, 1, 0, 2]

Before: [1, 0, 1, 3]
7 2 3 1
After:  [1, 0, 1, 3]

Before: [0, 2, 2, 2]
5 2 1 0
After:  [1, 2, 2, 2]

Before: [2, 0, 3, 2]
12 3 2 1
After:  [2, 2, 3, 2]

Before: [1, 1, 0, 2]
14 1 3 1
After:  [1, 0, 0, 2]

Before: [2, 3, 3, 1]
3 0 1 3
After:  [2, 3, 3, 1]

Before: [3, 0, 2, 1]
15 3 2 2
After:  [3, 0, 1, 1]

Before: [3, 1, 2, 2]
14 1 3 3
After:  [3, 1, 2, 0]

Before: [1, 0, 2, 3]
1 0 2 3
After:  [1, 0, 2, 0]

Before: [0, 2, 0, 1]
0 0 0 1
After:  [0, 0, 0, 1]

Before: [3, 1, 0, 1]
9 1 3 3
After:  [3, 1, 0, 1]

Before: [1, 1, 3, 2]
14 1 3 1
After:  [1, 0, 3, 2]

Before: [2, 1, 1, 0]
4 0 1 1
After:  [2, 1, 1, 0]

Before: [2, 1, 1, 1]
8 3 1 3
After:  [2, 1, 1, 0]

Before: [0, 1, 1, 0]
10 1 3 2
After:  [0, 1, 1, 0]

Before: [1, 0, 2, 1]
1 0 2 2
After:  [1, 0, 0, 1]

Before: [1, 2, 2, 3]
11 2 2 1
After:  [1, 2, 2, 3]

Before: [3, 1, 2, 0]
4 0 2 1
After:  [3, 1, 2, 0]

Before: [0, 0, 1, 0]
0 0 0 0
After:  [0, 0, 1, 0]

Before: [0, 2, 3, 3]
7 1 3 3
After:  [0, 2, 3, 0]

Before: [3, 1, 2, 1]
15 3 2 3
After:  [3, 1, 2, 1]

Before: [3, 1, 3, 3]
7 1 3 2
After:  [3, 1, 0, 3]

Before: [1, 1, 2, 0]
10 1 3 3
After:  [1, 1, 2, 1]

Before: [2, 1, 2, 1]
2 1 2 1
After:  [2, 0, 2, 1]

Before: [1, 1, 1, 1]
13 3 3 3
After:  [1, 1, 1, 0]

Before: [2, 1, 3, 1]
4 0 1 0
After:  [1, 1, 3, 1]

Before: [1, 1, 1, 1]
8 2 1 3
After:  [1, 1, 1, 0]

Before: [1, 1, 1, 3]
7 2 3 2
After:  [1, 1, 0, 3]

Before: [3, 2, 2, 2]
13 3 3 0
After:  [0, 2, 2, 2]

Before: [1, 3, 3, 2]
13 3 3 0
After:  [0, 3, 3, 2]

Before: [0, 3, 2, 1]
15 3 2 2
After:  [0, 3, 1, 1]

Before: [1, 2, 2, 2]
1 0 2 3
After:  [1, 2, 2, 0]

Before: [3, 1, 2, 1]
4 0 2 3
After:  [3, 1, 2, 1]

Before: [1, 1, 2, 1]
2 1 2 3
After:  [1, 1, 2, 0]

Before: [0, 1, 2, 0]
2 1 2 0
After:  [0, 1, 2, 0]

Before: [1, 1, 2, 3]
2 1 2 3
After:  [1, 1, 2, 0]

Before: [1, 1, 1, 2]
6 1 0 1
After:  [1, 1, 1, 2]

Before: [2, 3, 3, 3]
3 0 1 0
After:  [1, 3, 3, 3]

Before: [3, 2, 2, 0]
4 0 2 1
After:  [3, 1, 2, 0]

Before: [3, 1, 3, 3]
7 1 3 0
After:  [0, 1, 3, 3]

Before: [2, 3, 3, 1]
3 0 1 0
After:  [1, 3, 3, 1]

Before: [0, 1, 3, 0]
10 1 3 3
After:  [0, 1, 3, 1]

Before: [3, 1, 1, 0]
10 1 3 2
After:  [3, 1, 1, 0]

Before: [2, 2, 2, 0]
5 2 1 2
After:  [2, 2, 1, 0]

Before: [1, 1, 0, 0]
9 0 2 2
After:  [1, 1, 0, 0]

Before: [2, 3, 3, 0]
3 0 1 1
After:  [2, 1, 3, 0]

Before: [2, 1, 3, 2]
14 1 3 0
After:  [0, 1, 3, 2]

Before: [0, 1, 2, 2]
0 0 0 0
After:  [0, 1, 2, 2]

Before: [2, 0, 3, 0]
12 0 2 0
After:  [2, 0, 3, 0]

Before: [1, 1, 0, 0]
10 1 3 2
After:  [1, 1, 1, 0]

Before: [1, 1, 1, 2]
14 1 3 1
After:  [1, 0, 1, 2]

Before: [2, 1, 2, 3]
2 1 2 1
After:  [2, 0, 2, 3]

Before: [2, 3, 1, 0]
3 0 1 0
After:  [1, 3, 1, 0]

Before: [0, 3, 1, 3]
7 2 3 2
After:  [0, 3, 0, 3]

Before: [0, 1, 2, 1]
15 3 2 0
After:  [1, 1, 2, 1]

Before: [3, 3, 2, 2]
11 2 2 2
After:  [3, 3, 2, 2]

Before: [0, 1, 3, 1]
0 0 0 2
After:  [0, 1, 0, 1]

Before: [3, 2, 0, 3]
5 3 0 1
After:  [3, 1, 0, 3]

Before: [0, 3, 2, 2]
3 2 1 0
After:  [1, 3, 2, 2]

Before: [1, 1, 3, 1]
6 1 0 1
After:  [1, 1, 3, 1]

Before: [2, 2, 2, 1]
15 3 2 1
After:  [2, 1, 2, 1]

Before: [1, 1, 2, 0]
10 1 3 0
After:  [1, 1, 2, 0]

Before: [1, 1, 1, 3]
6 1 0 2
After:  [1, 1, 1, 3]

Before: [2, 0, 3, 3]
8 0 1 3
After:  [2, 0, 3, 1]

Before: [3, 1, 3, 2]
13 3 3 3
After:  [3, 1, 3, 0]

Before: [3, 2, 2, 2]
4 0 2 2
After:  [3, 2, 1, 2]

Before: [1, 1, 1, 0]
8 2 1 2
After:  [1, 1, 0, 0]

Before: [1, 0, 2, 1]
1 0 2 0
After:  [0, 0, 2, 1]

Before: [2, 3, 2, 1]
13 3 3 0
After:  [0, 3, 2, 1]

Before: [3, 0, 2, 3]
4 0 2 2
After:  [3, 0, 1, 3]

Before: [2, 1, 0, 1]
9 1 3 0
After:  [1, 1, 0, 1]

Before: [3, 2, 2, 1]
15 3 2 2
After:  [3, 2, 1, 1]

Before: [3, 1, 2, 1]
2 1 2 3
After:  [3, 1, 2, 0]

Before: [1, 1, 0, 0]
6 1 0 0
After:  [1, 1, 0, 0]

Before: [1, 0, 3, 2]
13 3 3 0
After:  [0, 0, 3, 2]

Before: [0, 2, 2, 2]
5 2 1 3
After:  [0, 2, 2, 1]

Before: [2, 3, 3, 2]
12 0 2 3
After:  [2, 3, 3, 2]

Before: [0, 2, 1, 1]
0 0 0 0
After:  [0, 2, 1, 1]

Before: [3, 0, 2, 1]
11 2 2 3
After:  [3, 0, 2, 2]

Before: [3, 2, 2, 1]
4 0 2 3
After:  [3, 2, 2, 1]

Before: [3, 1, 0, 3]
7 1 3 2
After:  [3, 1, 0, 3]

Before: [1, 1, 2, 1]
9 1 3 0
After:  [1, 1, 2, 1]

Before: [0, 0, 1, 3]
7 2 3 0
After:  [0, 0, 1, 3]

Before: [0, 1, 3, 1]
8 3 1 3
After:  [0, 1, 3, 0]

Before: [2, 1, 1, 1]
4 0 1 2
After:  [2, 1, 1, 1]

Before: [1, 1, 0, 0]
10 1 3 0
After:  [1, 1, 0, 0]

Before: [0, 1, 3, 2]
13 3 3 3
After:  [0, 1, 3, 0]

Before: [1, 1, 2, 0]
1 0 2 0
After:  [0, 1, 2, 0]

Before: [3, 1, 2, 0]
2 1 2 1
After:  [3, 0, 2, 0]

Before: [0, 1, 1, 3]
7 2 3 3
After:  [0, 1, 1, 0]

Before: [0, 2, 3, 3]
12 1 2 0
After:  [2, 2, 3, 3]

Before: [2, 1, 1, 1]
8 3 1 0
After:  [0, 1, 1, 1]

Before: [0, 1, 1, 2]
14 1 3 2
After:  [0, 1, 0, 2]

Before: [3, 1, 2, 1]
9 1 3 1
After:  [3, 1, 2, 1]

Before: [1, 2, 3, 2]
12 1 2 2
After:  [1, 2, 2, 2]

Before: [2, 3, 2, 2]
3 0 1 0
After:  [1, 3, 2, 2]

Before: [1, 1, 1, 0]
10 1 3 0
After:  [1, 1, 1, 0]

Before: [3, 2, 2, 2]
4 0 2 0
After:  [1, 2, 2, 2]

Before: [3, 1, 0, 2]
14 1 3 3
After:  [3, 1, 0, 0]

Before: [0, 3, 3, 2]
12 3 2 3
After:  [0, 3, 3, 2]

Before: [3, 3, 0, 0]
8 0 2 1
After:  [3, 1, 0, 0]

Before: [3, 0, 2, 0]
4 0 2 3
After:  [3, 0, 2, 1]

Before: [0, 3, 2, 1]
3 2 1 1
After:  [0, 1, 2, 1]

Before: [3, 0, 2, 3]
4 0 2 0
After:  [1, 0, 2, 3]

Before: [0, 1, 0, 0]
10 1 3 1
After:  [0, 1, 0, 0]

Before: [3, 3, 3, 3]
5 3 2 1
After:  [3, 1, 3, 3]

Before: [1, 2, 2, 0]
1 0 2 2
After:  [1, 2, 0, 0]

Before: [0, 3, 1, 2]
0 0 0 1
After:  [0, 0, 1, 2]

Before: [0, 3, 2, 3]
3 2 1 1
After:  [0, 1, 2, 3]

Before: [3, 1, 3, 2]
14 1 3 0
After:  [0, 1, 3, 2]

Before: [3, 1, 1, 3]
7 1 3 3
After:  [3, 1, 1, 0]

Before: [2, 2, 2, 2]
13 3 3 0
After:  [0, 2, 2, 2]

Before: [1, 1, 3, 3]
6 1 0 1
After:  [1, 1, 3, 3]

Before: [1, 1, 2, 0]
6 1 0 3
After:  [1, 1, 2, 1]

Before: [3, 3, 2, 1]
3 2 0 1
After:  [3, 1, 2, 1]

Before: [1, 1, 2, 3]
2 1 2 0
After:  [0, 1, 2, 3]

Before: [0, 3, 3, 1]
13 3 3 1
After:  [0, 0, 3, 1]

Before: [1, 2, 2, 0]
1 0 2 3
After:  [1, 2, 2, 0]

Before: [3, 2, 2, 0]
4 0 2 0
After:  [1, 2, 2, 0]

Before: [3, 1, 1, 3]
7 1 3 1
After:  [3, 0, 1, 3]

Before: [2, 2, 2, 3]
7 2 3 2
After:  [2, 2, 0, 3]

Before: [2, 1, 2, 2]
2 1 2 2
After:  [2, 1, 0, 2]

Before: [2, 0, 0, 3]
11 3 3 2
After:  [2, 0, 3, 3]

Before: [1, 1, 2, 1]
1 0 2 1
After:  [1, 0, 2, 1]

Before: [0, 1, 2, 1]
15 3 2 1
After:  [0, 1, 2, 1]

Before: [0, 3, 3, 3]
0 0 0 3
After:  [0, 3, 3, 0]

Before: [0, 1, 2, 3]
2 1 2 0
After:  [0, 1, 2, 3]

Before: [3, 3, 2, 3]
4 0 2 2
After:  [3, 3, 1, 3]

Before: [3, 2, 3, 3]
12 1 2 0
After:  [2, 2, 3, 3]

Before: [1, 1, 3, 0]
6 1 0 2
After:  [1, 1, 1, 0]

Before: [2, 3, 3, 3]
5 3 2 1
After:  [2, 1, 3, 3]

Before: [0, 1, 1, 2]
0 0 0 0
After:  [0, 1, 1, 2]

Before: [3, 1, 3, 2]
12 3 2 0
After:  [2, 1, 3, 2]

Before: [1, 3, 2, 1]
1 0 2 3
After:  [1, 3, 2, 0]

Before: [0, 1, 3, 2]
14 1 3 1
After:  [0, 0, 3, 2]

Before: [1, 1, 2, 3]
7 1 3 1
After:  [1, 0, 2, 3]

Before: [2, 2, 3, 0]
12 0 2 1
After:  [2, 2, 3, 0]

Before: [0, 1, 2, 2]
14 1 3 1
After:  [0, 0, 2, 2]

Before: [1, 1, 1, 2]
13 3 3 2
After:  [1, 1, 0, 2]

Before: [3, 3, 2, 0]
4 0 2 0
After:  [1, 3, 2, 0]

Before: [2, 1, 2, 2]
11 2 2 0
After:  [2, 1, 2, 2]

Before: [0, 0, 1, 3]
0 0 0 2
After:  [0, 0, 0, 3]

Before: [1, 0, 2, 1]
15 3 2 1
After:  [1, 1, 2, 1]

Before: [3, 2, 2, 2]
4 0 2 1
After:  [3, 1, 2, 2]

Before: [0, 2, 3, 3]
12 1 2 3
After:  [0, 2, 3, 2]

Before: [3, 3, 0, 3]
8 0 2 2
After:  [3, 3, 1, 3]

Before: [1, 1, 0, 2]
14 1 3 0
After:  [0, 1, 0, 2]

Before: [2, 3, 0, 3]
3 0 1 2
After:  [2, 3, 1, 3]

Before: [1, 1, 1, 1]
8 2 1 1
After:  [1, 0, 1, 1]

Before: [1, 1, 2, 0]
1 0 2 3
After:  [1, 1, 2, 0]

Before: [1, 2, 2, 1]
5 2 1 0
After:  [1, 2, 2, 1]

Before: [1, 1, 2, 3]
1 0 2 3
After:  [1, 1, 2, 0]

Before: [0, 1, 3, 0]
10 1 3 0
After:  [1, 1, 3, 0]

Before: [0, 1, 1, 1]
9 1 3 1
After:  [0, 1, 1, 1]

Before: [1, 1, 0, 3]
6 1 0 0
After:  [1, 1, 0, 3]

Before: [1, 2, 2, 3]
1 0 2 0
After:  [0, 2, 2, 3]

Before: [3, 3, 1, 2]
13 3 3 2
After:  [3, 3, 0, 2]

Before: [2, 2, 2, 1]
15 3 2 3
After:  [2, 2, 2, 1]

Before: [1, 2, 1, 3]
7 1 3 1
After:  [1, 0, 1, 3]

Before: [1, 1, 0, 2]
9 0 2 3
After:  [1, 1, 0, 0]

Before: [3, 3, 0, 2]
8 0 2 1
After:  [3, 1, 0, 2]

Before: [1, 0, 0, 3]
11 3 3 3
After:  [1, 0, 0, 3]

Before: [0, 3, 2, 2]
0 0 0 2
After:  [0, 3, 0, 2]

Before: [2, 3, 3, 0]
3 0 1 0
After:  [1, 3, 3, 0]

Before: [3, 3, 2, 1]
3 2 0 2
After:  [3, 3, 1, 1]

Before: [1, 1, 2, 2]
14 1 3 3
After:  [1, 1, 2, 0]

Before: [3, 3, 1, 1]
13 2 3 3
After:  [3, 3, 1, 0]

Before: [3, 1, 2, 0]
4 0 2 3
After:  [3, 1, 2, 1]

Before: [0, 3, 2, 2]
3 2 1 3
After:  [0, 3, 2, 1]

Before: [3, 1, 2, 1]
15 3 2 2
After:  [3, 1, 1, 1]

Before: [3, 1, 2, 2]
2 1 2 2
After:  [3, 1, 0, 2]

Before: [0, 0, 2, 1]
15 3 2 1
After:  [0, 1, 2, 1]

Before: [1, 1, 2, 1]
15 3 2 1
After:  [1, 1, 2, 1]

Before: [1, 3, 2, 2]
8 3 2 0
After:  [0, 3, 2, 2]

Before: [1, 2, 2, 1]
15 3 2 3
After:  [1, 2, 2, 1]

Before: [2, 0, 2, 1]
15 3 2 2
After:  [2, 0, 1, 1]

Before: [2, 2, 2, 1]
15 3 2 0
After:  [1, 2, 2, 1]

Before: [1, 3, 3, 2]
13 3 3 3
After:  [1, 3, 3, 0]

Before: [2, 0, 0, 2]
13 3 3 2
After:  [2, 0, 0, 2]

Before: [1, 0, 0, 0]
9 0 2 1
After:  [1, 0, 0, 0]

Before: [2, 2, 2, 3]
11 3 3 0
After:  [3, 2, 2, 3]

Before: [1, 3, 2, 1]
1 0 2 2
After:  [1, 3, 0, 1]

Before: [3, 1, 3, 1]
9 1 3 1
After:  [3, 1, 3, 1]

Before: [0, 2, 3, 0]
12 1 2 2
After:  [0, 2, 2, 0]

Before: [1, 1, 3, 2]
6 1 0 0
After:  [1, 1, 3, 2]

Before: [3, 0, 2, 2]
8 3 2 1
After:  [3, 0, 2, 2]

Before: [1, 1, 0, 1]
9 0 2 0
After:  [0, 1, 0, 1]

Before: [1, 1, 2, 1]
9 1 3 1
After:  [1, 1, 2, 1]

Before: [2, 2, 2, 0]
5 2 0 0
After:  [1, 2, 2, 0]

Before: [3, 3, 2, 1]
15 3 2 2
After:  [3, 3, 1, 1]

Before: [0, 1, 1, 1]
9 1 3 3
After:  [0, 1, 1, 1]

Before: [1, 1, 3, 0]
6 1 0 1
After:  [1, 1, 3, 0]

Before: [0, 3, 1, 3]
0 0 0 2
After:  [0, 3, 0, 3]

Before: [2, 3, 3, 0]
8 2 0 1
After:  [2, 1, 3, 0]

Before: [3, 1, 3, 2]
14 1 3 1
After:  [3, 0, 3, 2]

Before: [0, 3, 1, 3]
7 2 3 0
After:  [0, 3, 1, 3]

Before: [2, 1, 3, 1]
4 0 1 2
After:  [2, 1, 1, 1]

Before: [0, 1, 3, 2]
0 0 0 2
After:  [0, 1, 0, 2]

Before: [2, 2, 3, 1]
12 0 2 2
After:  [2, 2, 2, 1]

Before: [3, 1, 3, 1]
13 3 3 3
After:  [3, 1, 3, 0]

Before: [3, 3, 2, 2]
3 2 1 0
After:  [1, 3, 2, 2]

Before: [0, 1, 2, 3]
2 1 2 2
After:  [0, 1, 0, 3]

Before: [3, 1, 2, 2]
3 2 0 0
After:  [1, 1, 2, 2]

Before: [0, 1, 1, 0]
8 2 1 3
After:  [0, 1, 1, 0]

Before: [1, 1, 2, 3]
1 0 2 0
After:  [0, 1, 2, 3]

Before: [1, 2, 0, 3]
7 1 3 3
After:  [1, 2, 0, 0]

Before: [2, 1, 3, 0]
10 1 3 1
After:  [2, 1, 3, 0]

Before: [3, 1, 2, 0]
3 2 0 0
After:  [1, 1, 2, 0]

Before: [1, 1, 2, 2]
6 1 0 2
After:  [1, 1, 1, 2]

Before: [0, 1, 2, 0]
10 1 3 1
After:  [0, 1, 2, 0]

Before: [2, 1, 2, 2]
5 2 0 1
After:  [2, 1, 2, 2]

Before: [2, 1, 0, 2]
14 1 3 0
After:  [0, 1, 0, 2]

Before: [1, 1, 2, 1]
15 3 2 2
After:  [1, 1, 1, 1]

Before: [3, 1, 2, 0]
2 1 2 2
After:  [3, 1, 0, 0]

Before: [1, 1, 2, 3]
2 1 2 1
After:  [1, 0, 2, 3]

Before: [3, 0, 2, 2]
3 2 0 2
After:  [3, 0, 1, 2]

Before: [0, 0, 3, 2]
13 3 3 2
After:  [0, 0, 0, 2]

Before: [1, 0, 2, 2]
1 0 2 2
After:  [1, 0, 0, 2]

Before: [0, 1, 2, 3]
11 3 3 3
After:  [0, 1, 2, 3]

Before: [2, 0, 3, 3]
5 3 2 1
After:  [2, 1, 3, 3]

Before: [0, 2, 0, 3]
0 0 0 3
After:  [0, 2, 0, 0]

Before: [2, 2, 0, 1]
13 3 3 3
After:  [2, 2, 0, 0]

Before: [0, 1, 2, 2]
14 1 3 3
After:  [0, 1, 2, 0]

Before: [2, 1, 2, 1]
4 0 1 1
After:  [2, 1, 2, 1]

Before: [1, 1, 3, 1]
9 1 3 0
After:  [1, 1, 3, 1]

Before: [1, 1, 1, 3]
6 1 0 1
After:  [1, 1, 1, 3]

Before: [3, 1, 1, 0]
8 2 1 1
After:  [3, 0, 1, 0]

Before: [3, 2, 2, 1]
15 3 2 1
After:  [3, 1, 2, 1]

Before: [2, 1, 2, 3]
11 3 3 0
After:  [3, 1, 2, 3]

Before: [0, 0, 2, 1]
15 3 2 2
After:  [0, 0, 1, 1]

Before: [1, 2, 2, 1]
15 3 2 0
After:  [1, 2, 2, 1]

Before: [0, 3, 2, 2]
0 0 0 3
After:  [0, 3, 2, 0]

Before: [2, 1, 2, 0]
2 1 2 3
After:  [2, 1, 2, 0]

Before: [0, 3, 2, 3]
3 2 1 0
After:  [1, 3, 2, 3]

Before: [1, 2, 2, 3]
1 0 2 3
After:  [1, 2, 2, 0]

Before: [2, 3, 0, 0]
3 0 1 3
After:  [2, 3, 0, 1]

Before: [2, 3, 1, 3]
3 0 1 1
After:  [2, 1, 1, 3]

Before: [3, 1, 2, 1]
2 1 2 0
After:  [0, 1, 2, 1]

Before: [3, 1, 3, 2]
12 3 2 1
After:  [3, 2, 3, 2]

Before: [3, 1, 2, 3]
2 1 2 3
After:  [3, 1, 2, 0]

Before: [2, 1, 2, 0]
2 1 2 2
After:  [2, 1, 0, 0]

Before: [0, 3, 2, 3]
0 0 0 3
After:  [0, 3, 2, 0]

Before: [1, 0, 0, 2]
13 3 3 3
After:  [1, 0, 0, 0]

Before: [2, 3, 3, 3]
3 0 1 1
After:  [2, 1, 3, 3]

Before: [0, 1, 0, 3]
7 1 3 3
After:  [0, 1, 0, 0]

Before: [0, 1, 2, 2]
2 1 2 2
After:  [0, 1, 0, 2]

Before: [2, 0, 3, 0]
8 2 0 3
After:  [2, 0, 3, 1]

Before: [2, 3, 2, 1]
15 3 2 3
After:  [2, 3, 2, 1]

Before: [0, 2, 3, 2]
13 3 3 3
After:  [0, 2, 3, 0]

Before: [0, 2, 2, 3]
7 1 3 2
After:  [0, 2, 0, 3]

Before: [3, 2, 1, 3]
7 1 3 3
After:  [3, 2, 1, 0]

Before: [2, 1, 1, 2]
14 1 3 0
After:  [0, 1, 1, 2]

Before: [3, 1, 2, 0]
4 0 2 2
After:  [3, 1, 1, 0]

Before: [1, 2, 3, 1]
12 1 2 0
After:  [2, 2, 3, 1]

Before: [0, 0, 3, 2]
12 3 2 3
After:  [0, 0, 3, 2]

Before: [2, 1, 2, 0]
10 1 3 3
After:  [2, 1, 2, 1]

Before: [2, 0, 3, 3]
12 0 2 3
After:  [2, 0, 3, 2]

Before: [1, 1, 1, 2]
14 1 3 2
After:  [1, 1, 0, 2]

Before: [0, 2, 0, 3]
11 3 3 2
After:  [0, 2, 3, 3]

Before: [3, 2, 1, 3]
7 2 3 3
After:  [3, 2, 1, 0]

Before: [3, 1, 2, 2]
8 3 2 3
After:  [3, 1, 2, 0]

Before: [2, 3, 2, 3]
3 0 1 0
After:  [1, 3, 2, 3]

Before: [2, 1, 2, 2]
4 0 1 3
After:  [2, 1, 2, 1]

Before: [3, 2, 2, 2]
3 2 0 2
After:  [3, 2, 1, 2]

Before: [3, 1, 2, 1]
4 0 2 2
After:  [3, 1, 1, 1]

Before: [2, 3, 2, 1]
15 3 2 0
After:  [1, 3, 2, 1]

Before: [2, 1, 3, 2]
4 0 1 3
After:  [2, 1, 3, 1]

Before: [0, 1, 3, 2]
14 1 3 0
After:  [0, 1, 3, 2]

Before: [1, 2, 2, 1]
15 3 2 1
After:  [1, 1, 2, 1]

Before: [1, 3, 0, 2]
9 0 2 0
After:  [0, 3, 0, 2]

Before: [1, 1, 3, 0]
6 1 0 3
After:  [1, 1, 3, 1]

Before: [1, 0, 2, 0]
1 0 2 2
After:  [1, 0, 0, 0]

Before: [0, 1, 0, 3]
0 0 0 1
After:  [0, 0, 0, 3]

Before: [1, 3, 2, 3]
1 0 2 1
After:  [1, 0, 2, 3]

Before: [3, 3, 2, 2]
3 2 1 2
After:  [3, 3, 1, 2]

Before: [2, 1, 0, 2]
4 0 1 3
After:  [2, 1, 0, 1]

Before: [2, 2, 1, 3]
7 2 3 0
After:  [0, 2, 1, 3]

Before: [2, 1, 2, 2]
4 0 1 2
After:  [2, 1, 1, 2]

Before: [2, 1, 3, 2]
12 3 2 3
After:  [2, 1, 3, 2]

Before: [2, 2, 3, 3]
5 3 2 1
After:  [2, 1, 3, 3]

Before: [0, 1, 1, 0]
10 1 3 0
After:  [1, 1, 1, 0]

Before: [0, 3, 2, 1]
13 3 3 3
After:  [0, 3, 2, 0]

Before: [0, 2, 3, 2]
12 3 2 1
After:  [0, 2, 3, 2]

Before: [0, 2, 3, 1]
0 0 0 0
After:  [0, 2, 3, 1]

Before: [1, 1, 0, 1]
9 0 2 1
After:  [1, 0, 0, 1]

Before: [3, 2, 3, 3]
7 1 3 1
After:  [3, 0, 3, 3]

Before: [0, 3, 0, 3]
11 3 3 3
After:  [0, 3, 0, 3]

Before: [3, 3, 2, 1]
15 3 2 1
After:  [3, 1, 2, 1]

Before: [1, 1, 2, 1]
6 1 0 1
After:  [1, 1, 2, 1]

Before: [3, 3, 2, 3]
4 0 2 0
After:  [1, 3, 2, 3]

Before: [2, 3, 3, 0]
12 0 2 3
After:  [2, 3, 3, 2]

Before: [1, 3, 2, 0]
3 2 1 1
After:  [1, 1, 2, 0]

Before: [3, 3, 2, 3]
3 2 0 1
After:  [3, 1, 2, 3]

Before: [0, 2, 3, 1]
12 1 2 0
After:  [2, 2, 3, 1]

Before: [3, 0, 2, 0]
3 2 0 1
After:  [3, 1, 2, 0]

Before: [1, 3, 2, 1]
1 0 2 1
After:  [1, 0, 2, 1]

Before: [1, 1, 2, 1]
6 1 0 3
After:  [1, 1, 2, 1]

Before: [1, 2, 3, 2]
12 1 2 1
After:  [1, 2, 3, 2]

Before: [1, 1, 2, 1]
1 0 2 3
After:  [1, 1, 2, 0]

Before: [2, 1, 0, 0]
10 1 3 0
After:  [1, 1, 0, 0]

Before: [1, 2, 2, 0]
5 2 1 1
After:  [1, 1, 2, 0]

Before: [3, 3, 2, 0]
4 0 2 1
After:  [3, 1, 2, 0]

Before: [0, 0, 0, 3]
0 0 0 0
After:  [0, 0, 0, 3]

Before: [1, 1, 1, 0]
6 1 0 0
After:  [1, 1, 1, 0]

Before: [1, 1, 2, 3]
1 0 2 2
After:  [1, 1, 0, 3]

Before: [3, 0, 2, 1]
4 0 2 0
After:  [1, 0, 2, 1]

Before: [1, 1, 0, 0]
6 1 0 2
After:  [1, 1, 1, 0]

Before: [1, 1, 1, 0]
8 2 1 0
After:  [0, 1, 1, 0]

Before: [3, 2, 2, 3]
5 2 1 2
After:  [3, 2, 1, 3]

Before: [3, 3, 2, 1]
4 0 2 2
After:  [3, 3, 1, 1]

Before: [2, 3, 0, 2]
3 0 1 2
After:  [2, 3, 1, 2]

Before: [1, 3, 0, 2]
9 0 2 2
After:  [1, 3, 0, 2]

Before: [1, 2, 0, 1]
9 0 2 1
After:  [1, 0, 0, 1]

Before: [2, 0, 2, 0]
5 2 0 3
After:  [2, 0, 2, 1]

Before: [1, 1, 3, 1]
8 3 1 2
After:  [1, 1, 0, 1]

Before: [1, 1, 3, 0]
10 1 3 0
After:  [1, 1, 3, 0]

Before: [2, 3, 3, 2]
8 2 0 2
After:  [2, 3, 1, 2]

Before: [3, 1, 0, 0]
10 1 3 1
After:  [3, 1, 0, 0]

Before: [1, 1, 0, 3]
9 0 2 1
After:  [1, 0, 0, 3]

Before: [3, 2, 3, 2]
12 3 2 2
After:  [3, 2, 2, 2]

Before: [1, 3, 2, 0]
1 0 2 1
After:  [1, 0, 2, 0]

Before: [1, 2, 0, 1]
13 3 3 0
After:  [0, 2, 0, 1]

Before: [0, 1, 3, 3]
5 3 2 3
After:  [0, 1, 3, 1]

Before: [1, 1, 1, 0]
10 1 3 1
After:  [1, 1, 1, 0]

Before: [2, 0, 2, 0]
5 2 0 1
After:  [2, 1, 2, 0]

Before: [0, 1, 2, 1]
2 1 2 3
After:  [0, 1, 2, 0]

Before: [3, 2, 3, 3]
7 1 3 0
After:  [0, 2, 3, 3]

Before: [0, 3, 0, 0]
0 0 0 0
After:  [0, 3, 0, 0]

Before: [3, 1, 3, 1]
8 3 1 1
After:  [3, 0, 3, 1]

Before: [0, 1, 3, 2]
14 1 3 2
After:  [0, 1, 0, 2]

Before: [2, 3, 1, 3]
3 0 1 0
After:  [1, 3, 1, 3]

Before: [1, 1, 0, 2]
6 1 0 3
After:  [1, 1, 0, 1]

Before: [1, 3, 2, 2]
3 2 1 1
After:  [1, 1, 2, 2]

Before: [0, 2, 2, 1]
15 3 2 0
After:  [1, 2, 2, 1]

Before: [2, 1, 2, 0]
10 1 3 1
After:  [2, 1, 2, 0]

Before: [2, 0, 2, 0]
11 2 2 0
After:  [2, 0, 2, 0]

Before: [0, 1, 0, 2]
13 3 3 0
After:  [0, 1, 0, 2]

Before: [1, 1, 0, 3]
6 1 0 3
After:  [1, 1, 0, 1]

Before: [1, 3, 2, 2]
1 0 2 3
After:  [1, 3, 2, 0]

Before: [3, 1, 2, 3]
2 1 2 2
After:  [3, 1, 0, 3]

Before: [3, 1, 2, 3]
4 0 2 0
After:  [1, 1, 2, 3]

Before: [2, 1, 3, 2]
12 0 2 3
After:  [2, 1, 3, 2]

Before: [3, 1, 2, 2]
2 1 2 0
After:  [0, 1, 2, 2]

Before: [1, 1, 2, 2]
14 1 3 0
After:  [0, 1, 2, 2]

Before: [3, 1, 0, 2]
8 0 2 0
After:  [1, 1, 0, 2]

Before: [2, 3, 2, 1]
15 3 2 2
After:  [2, 3, 1, 1]

Before: [3, 1, 0, 2]
13 3 3 3
After:  [3, 1, 0, 0]

Before: [3, 1, 2, 0]
10 1 3 3
After:  [3, 1, 2, 1]

Before: [0, 0, 1, 3]
0 0 0 1
After:  [0, 0, 1, 3]

Before: [3, 3, 3, 3]
11 3 3 2
After:  [3, 3, 3, 3]

Before: [0, 1, 1, 0]
10 1 3 3
After:  [0, 1, 1, 1]

Before: [3, 2, 2, 3]
5 2 1 3
After:  [3, 2, 2, 1]

Before: [1, 0, 0, 1]
9 0 2 2
After:  [1, 0, 0, 1]

Before: [2, 2, 2, 0]
5 2 1 0
After:  [1, 2, 2, 0]

Before: [1, 1, 2, 1]
15 3 2 0
After:  [1, 1, 2, 1]

Before: [2, 1, 1, 2]
14 1 3 2
After:  [2, 1, 0, 2]

Before: [3, 2, 2, 3]
11 3 3 1
After:  [3, 3, 2, 3]

Before: [1, 1, 2, 0]
6 1 0 2
After:  [1, 1, 1, 0]

Before: [3, 0, 0, 1]
8 0 2 3
After:  [3, 0, 0, 1]

Before: [3, 3, 3, 3]
5 3 2 3
After:  [3, 3, 3, 1]

Before: [0, 1, 2, 2]
14 1 3 0
After:  [0, 1, 2, 2]

Before: [3, 1, 0, 1]
9 1 3 2
After:  [3, 1, 1, 1]

Before: [3, 1, 3, 0]
10 1 3 0
After:  [1, 1, 3, 0]

Before: [3, 2, 1, 3]
7 2 3 2
After:  [3, 2, 0, 3]

Before: [2, 1, 3, 3]
8 2 0 3
After:  [2, 1, 3, 1]

Before: [0, 3, 2, 3]
11 2 2 3
After:  [0, 3, 2, 2]

Before: [0, 1, 2, 1]
2 1 2 1
After:  [0, 0, 2, 1]

Before: [2, 1, 2, 1]
4 0 1 0
After:  [1, 1, 2, 1]

Before: [1, 1, 3, 0]
6 1 0 0
After:  [1, 1, 3, 0]

Before: [2, 1, 2, 0]
4 0 1 1
After:  [2, 1, 2, 0]

Before: [0, 1, 0, 2]
14 1 3 2
After:  [0, 1, 0, 2]

Before: [1, 1, 1, 3]
7 1 3 3
After:  [1, 1, 1, 0]

Before: [0, 1, 1, 1]
0 0 0 0
After:  [0, 1, 1, 1]

Before: [1, 2, 3, 2]
12 3 2 2
After:  [1, 2, 2, 2]

Before: [1, 1, 0, 3]
7 1 3 3
After:  [1, 1, 0, 0]

Before: [1, 2, 1, 3]
7 2 3 1
After:  [1, 0, 1, 3]

Before: [3, 1, 0, 2]
14 1 3 2
After:  [3, 1, 0, 2]

Before: [2, 3, 3, 3]
12 0 2 3
After:  [2, 3, 3, 2]

Before: [3, 2, 3, 1]
12 1 2 0
After:  [2, 2, 3, 1]

Before: [1, 1, 1, 2]
6 1 0 2
After:  [1, 1, 1, 2]

Before: [0, 0, 2, 1]
11 2 2 3
After:  [0, 0, 2, 2]

Before: [0, 3, 1, 3]
0 0 0 1
After:  [0, 0, 1, 3]

Before: [2, 1, 3, 0]
8 2 0 2
After:  [2, 1, 1, 0]

Before: [2, 1, 3, 3]
12 0 2 1
After:  [2, 2, 3, 3]

Before: [1, 2, 3, 3]
12 1 2 1
After:  [1, 2, 3, 3]

Before: [1, 1, 0, 3]
6 1 0 2
After:  [1, 1, 1, 3]

Before: [3, 3, 2, 2]
4 0 2 3
After:  [3, 3, 2, 1]

Before: [3, 2, 0, 2]
13 3 3 3
After:  [3, 2, 0, 0]

Before: [1, 1, 0, 1]
6 1 0 1
After:  [1, 1, 0, 1]

Before: [3, 3, 2, 3]
7 2 3 0
After:  [0, 3, 2, 3]

Before: [3, 1, 2, 2]
2 1 2 1
After:  [3, 0, 2, 2]

Before: [3, 1, 3, 1]
9 1 3 2
After:  [3, 1, 1, 1]

Before: [3, 3, 2, 1]
15 3 2 3
After:  [3, 3, 2, 1]

Before: [0, 1, 3, 0]
10 1 3 1
After:  [0, 1, 3, 0]

Before: [1, 1, 2, 2]
6 1 0 0
After:  [1, 1, 2, 2]

Before: [2, 0, 1, 1]
8 0 1 2
After:  [2, 0, 1, 1]

Before: [1, 1, 2, 3]
11 2 2 2
After:  [1, 1, 2, 3]

Before: [0, 3, 3, 2]
12 3 2 1
After:  [0, 2, 3, 2]

Before: [0, 1, 2, 1]
9 1 3 1
After:  [0, 1, 2, 1]

Before: [3, 0, 3, 3]
5 3 0 1
After:  [3, 1, 3, 3]

Before: [1, 0, 0, 1]
9 0 2 3
After:  [1, 0, 0, 0]

Before: [0, 1, 1, 0]
10 1 3 1
After:  [0, 1, 1, 0]

Before: [1, 1, 3, 2]
6 1 0 2
After:  [1, 1, 1, 2]

Before: [3, 3, 3, 1]
5 2 3 0
After:  [0, 3, 3, 1]

Before: [3, 1, 2, 3]
7 1 3 2
After:  [3, 1, 0, 3]

Before: [3, 3, 2, 3]
11 3 3 0
After:  [3, 3, 2, 3]

Before: [1, 1, 0, 1]
8 3 1 2
After:  [1, 1, 0, 1]

Before: [0, 1, 3, 2]
14 1 3 3
After:  [0, 1, 3, 0]

Before: [2, 3, 0, 3]
3 0 1 3
After:  [2, 3, 0, 1]

Before: [2, 1, 3, 2]
12 0 2 2
After:  [2, 1, 2, 2]

Before: [2, 1, 0, 0]
10 1 3 3
After:  [2, 1, 0, 1]

Before: [3, 2, 2, 0]
3 2 0 0
After:  [1, 2, 2, 0]

Before: [2, 2, 2, 1]
13 3 3 2
After:  [2, 2, 0, 1]

Before: [3, 1, 3, 1]
5 2 3 1
After:  [3, 0, 3, 1]

Before: [2, 3, 3, 3]
12 0 2 1
After:  [2, 2, 3, 3]

Before: [1, 1, 1, 1]
6 1 0 3
After:  [1, 1, 1, 1]

Before: [0, 1, 0, 0]
10 1 3 0
After:  [1, 1, 0, 0]

Before: [3, 1, 2, 3]
7 1 3 0
After:  [0, 1, 2, 3]

Before: [2, 1, 2, 1]
15 3 2 2
After:  [2, 1, 1, 1]

Before: [3, 1, 3, 2]
13 3 3 2
After:  [3, 1, 0, 2]

Before: [0, 1, 3, 1]
8 3 1 2
After:  [0, 1, 0, 1]

Before: [0, 0, 3, 0]
0 0 0 0
After:  [0, 0, 3, 0]

Before: [2, 3, 3, 1]
12 0 2 1
After:  [2, 2, 3, 1]

Before: [0, 1, 3, 1]
9 1 3 0
After:  [1, 1, 3, 1]

Before: [3, 1, 1, 0]
10 1 3 3
After:  [3, 1, 1, 1]

Before: [1, 1, 0, 1]
6 1 0 0
After:  [1, 1, 0, 1]

Before: [0, 2, 0, 0]
0 0 0 0
After:  [0, 2, 0, 0]

Before: [3, 0, 2, 3]
3 2 0 0
After:  [1, 0, 2, 3]

Before: [0, 2, 2, 3]
0 0 0 2
After:  [0, 2, 0, 3]

Before: [0, 3, 3, 3]
11 3 3 2
After:  [0, 3, 3, 3]

Before: [3, 1, 1, 3]
5 3 0 3
After:  [3, 1, 1, 1]

Before: [1, 2, 0, 3]
11 3 3 2
After:  [1, 2, 3, 3]

Before: [0, 3, 1, 1]
0 0 0 1
After:  [0, 0, 1, 1]

Before: [2, 1, 0, 0]
10 1 3 1
After:  [2, 1, 0, 0]

Before: [2, 1, 0, 1]
9 1 3 1
After:  [2, 1, 0, 1]

Before: [2, 3, 2, 3]
3 2 1 1
After:  [2, 1, 2, 3]

Before: [0, 3, 0, 2]
0 0 0 3
After:  [0, 3, 0, 0]

Before: [0, 2, 2, 3]
11 2 2 2
After:  [0, 2, 2, 3]

Before: [3, 2, 2, 1]
15 3 2 0
After:  [1, 2, 2, 1]

Before: [2, 3, 2, 3]
11 2 2 2
After:  [2, 3, 2, 3]

Before: [1, 0, 2, 1]
15 3 2 3
After:  [1, 0, 2, 1]

Before: [2, 3, 3, 2]
3 0 1 0
After:  [1, 3, 3, 2]

Before: [3, 3, 2, 2]
4 0 2 0
After:  [1, 3, 2, 2]

Before: [3, 1, 3, 2]
14 1 3 3
After:  [3, 1, 3, 0]

Before: [2, 1, 2, 3]
2 1 2 0
After:  [0, 1, 2, 3]

Before: [3, 1, 3, 3]
5 3 0 0
After:  [1, 1, 3, 3]

Before: [0, 1, 2, 2]
2 1 2 0
After:  [0, 1, 2, 2]

Before: [1, 1, 2, 3]
6 1 0 0
After:  [1, 1, 2, 3]

Before: [1, 3, 2, 2]
1 0 2 2
After:  [1, 3, 0, 2]

Before: [1, 1, 2, 0]
2 1 2 0
After:  [0, 1, 2, 0]

Before: [1, 2, 0, 1]
9 0 2 0
After:  [0, 2, 0, 1]

Before: [3, 2, 2, 3]
4 0 2 0
After:  [1, 2, 2, 3]

Before: [2, 2, 3, 2]
12 0 2 2
After:  [2, 2, 2, 2]

Before: [2, 0, 2, 1]
15 3 2 0
After:  [1, 0, 2, 1]

Before: [2, 1, 2, 3]
5 2 0 0
After:  [1, 1, 2, 3]

Before: [2, 1, 2, 1]
9 1 3 0
After:  [1, 1, 2, 1]

Before: [3, 3, 2, 0]
3 2 1 0
After:  [1, 3, 2, 0]

Before: [1, 3, 2, 3]
1 0 2 3
After:  [1, 3, 2, 0]

Before: [0, 0, 2, 1]
15 3 2 3
After:  [0, 0, 2, 1]

Before: [1, 3, 2, 2]
1 0 2 1
After:  [1, 0, 2, 2]

Before: [3, 0, 3, 3]
5 3 0 0
After:  [1, 0, 3, 3]

Before: [2, 3, 1, 3]
7 2 3 2
After:  [2, 3, 0, 3]

Before: [0, 1, 0, 2]
14 1 3 1
After:  [0, 0, 0, 2]

Before: [2, 1, 2, 1]
2 1 2 3
After:  [2, 1, 2, 0]

Before: [2, 0, 1, 3]
7 2 3 1
After:  [2, 0, 1, 3]

Before: [1, 1, 1, 2]
14 1 3 0
After:  [0, 1, 1, 2]

Before: [2, 1, 0, 1]
4 0 1 0
After:  [1, 1, 0, 1]

Before: [2, 3, 0, 2]
3 0 1 0
After:  [1, 3, 0, 2]

Before: [2, 3, 2, 2]
5 2 0 3
After:  [2, 3, 2, 1]

Before: [0, 0, 2, 1]
15 3 2 0
After:  [1, 0, 2, 1]

Before: [1, 1, 3, 2]
14 1 3 2
After:  [1, 1, 0, 2]

Before: [1, 3, 0, 3]
9 0 2 3
After:  [1, 3, 0, 0]

Before: [1, 3, 3, 1]
13 3 3 0
After:  [0, 3, 3, 1]

Before: [3, 2, 2, 1]
4 0 2 1
After:  [3, 1, 2, 1]

Before: [2, 3, 1, 1]
3 0 1 3
After:  [2, 3, 1, 1]

Before: [1, 1, 0, 0]
9 0 2 3
After:  [1, 1, 0, 0]

Before: [2, 1, 3, 0]
8 2 0 0
After:  [1, 1, 3, 0]

Before: [2, 2, 2, 0]
5 2 1 1
After:  [2, 1, 2, 0]

Before: [1, 1, 2, 1]
6 1 0 2
After:  [1, 1, 1, 1]

Before: [0, 3, 1, 0]
0 0 0 2
After:  [0, 3, 0, 0]

Before: [1, 3, 2, 2]
8 3 2 1
After:  [1, 0, 2, 2]

Before: [1, 1, 1, 0]
10 1 3 2
After:  [1, 1, 1, 0]

Before: [1, 2, 2, 0]
11 2 2 1
After:  [1, 2, 2, 0]

Before: [2, 1, 2, 2]
11 2 2 2
After:  [2, 1, 2, 2]

Before: [1, 3, 2, 1]
15 3 2 1
After:  [1, 1, 2, 1]

Before: [0, 2, 3, 3]
0 0 0 0
After:  [0, 2, 3, 3]

Before: [0, 2, 2, 3]
11 2 2 0
After:  [2, 2, 2, 3]

Before: [3, 2, 3, 3]
5 3 2 2
After:  [3, 2, 1, 3]

Before: [2, 0, 3, 3]
12 0 2 2
After:  [2, 0, 2, 3]

Before: [2, 1, 1, 1]
9 1 3 0
After:  [1, 1, 1, 1]

Before: [1, 1, 2, 1]
9 1 3 2
After:  [1, 1, 1, 1]

Before: [1, 1, 2, 2]
11 2 2 3
After:  [1, 1, 2, 2]

Before: [2, 1, 3, 2]
12 3 2 0
After:  [2, 1, 3, 2]

Before: [1, 1, 0, 2]
9 0 2 0
After:  [0, 1, 0, 2]

Before: [1, 1, 3, 3]
6 1 0 3
After:  [1, 1, 3, 1]

Before: [1, 3, 0, 2]
13 3 3 2
After:  [1, 3, 0, 2]

Before: [1, 1, 0, 0]
6 1 0 3
After:  [1, 1, 0, 1]

Before: [3, 2, 3, 3]
5 3 0 3
After:  [3, 2, 3, 1]

Before: [1, 1, 1, 3]
8 2 1 3
After:  [1, 1, 1, 0]

Before: [3, 1, 2, 2]
14 1 3 0
After:  [0, 1, 2, 2]

Before: [1, 0, 2, 0]
1 0 2 1
After:  [1, 0, 2, 0]

Before: [2, 1, 3, 3]
7 1 3 2
After:  [2, 1, 0, 3]

Before: [1, 1, 2, 1]
2 1 2 0
After:  [0, 1, 2, 1]

Before: [2, 1, 0, 2]
14 1 3 1
After:  [2, 0, 0, 2]

Before: [0, 3, 2, 1]
15 3 2 3
After:  [0, 3, 2, 1]

Before: [2, 3, 3, 3]
3 0 1 3
After:  [2, 3, 3, 1]

Before: [3, 0, 2, 3]
4 0 2 1
After:  [3, 1, 2, 3]

Before: [0, 2, 1, 3]
7 2 3 1
After:  [0, 0, 1, 3]

Before: [1, 3, 2, 0]
3 2 1 3
After:  [1, 3, 2, 1]

Before: [3, 2, 3, 3]
5 3 0 0
After:  [1, 2, 3, 3]

Before: [2, 0, 0, 1]
8 0 1 0
After:  [1, 0, 0, 1]

Before: [2, 1, 3, 1]
9 1 3 2
After:  [2, 1, 1, 1]

Before: [0, 2, 2, 1]
11 2 2 1
After:  [0, 2, 2, 1]

Before: [0, 1, 0, 3]
0 0 0 3
After:  [0, 1, 0, 0]

Before: [2, 1, 1, 3]
4 0 1 1
After:  [2, 1, 1, 3]

Before: [3, 3, 2, 2]
3 2 0 0
After:  [1, 3, 2, 2]

Before: [2, 2, 3, 2]
12 1 2 0
After:  [2, 2, 3, 2]

Before: [3, 0, 2, 1]
11 2 2 2
After:  [3, 0, 2, 1]

Before: [2, 0, 3, 2]
8 2 0 0
After:  [1, 0, 3, 2]

Before: [0, 1, 2, 1]
0 0 0 0
After:  [0, 1, 2, 1]

Before: [1, 2, 2, 1]
1 0 2 0
After:  [0, 2, 2, 1]

Before: [2, 1, 1, 1]
8 2 1 0
After:  [0, 1, 1, 1]

Before: [1, 1, 2, 2]
14 1 3 1
After:  [1, 0, 2, 2]

Before: [0, 3, 3, 2]
12 3 2 0
After:  [2, 3, 3, 2]

Before: [0, 3, 2, 1]
15 3 2 1
After:  [0, 1, 2, 1]

Before: [2, 2, 3, 0]
8 2 0 0
After:  [1, 2, 3, 0]

Before: [3, 3, 2, 1]
4 0 2 1
After:  [3, 1, 2, 1]

Before: [1, 1, 2, 2]
14 1 3 2
After:  [1, 1, 0, 2]

Before: [3, 2, 3, 3]
12 1 2 1
After:  [3, 2, 3, 3]

Before: [1, 1, 2, 2]
6 1 0 1
After:  [1, 1, 2, 2]

Before: [2, 1, 3, 0]
10 1 3 0
After:  [1, 1, 3, 0]

Before: [2, 1, 2, 1]
15 3 2 0
After:  [1, 1, 2, 1]

Before: [1, 3, 3, 3]
11 3 3 2
After:  [1, 3, 3, 3]

Before: [3, 3, 2, 2]
8 3 2 3
After:  [3, 3, 2, 0]

Before: [2, 1, 0, 1]
4 0 1 2
After:  [2, 1, 1, 1]

Before: [1, 1, 0, 3]
7 1 3 2
After:  [1, 1, 0, 3]

Before: [2, 3, 3, 2]
12 3 2 3
After:  [2, 3, 3, 2]

Before: [1, 2, 0, 3]
9 0 2 0
After:  [0, 2, 0, 3]

Before: [1, 0, 0, 0]
9 0 2 0
After:  [0, 0, 0, 0]

Before: [2, 2, 3, 3]
12 0 2 0
After:  [2, 2, 3, 3]

Before: [2, 3, 3, 3]
11 3 3 1
After:  [2, 3, 3, 3]

Before: [0, 3, 2, 3]
11 2 2 1
After:  [0, 2, 2, 3]

Before: [2, 2, 3, 3]
12 1 2 0
After:  [2, 2, 3, 3]

Before: [3, 1, 1, 0]
10 1 3 1
After:  [3, 1, 1, 0]

Before: [3, 1, 2, 1]
9 1 3 3
After:  [3, 1, 2, 1]

Before: [1, 2, 1, 3]
7 1 3 3
After:  [1, 2, 1, 0]

Before: [2, 1, 2, 1]
2 1 2 2
After:  [2, 1, 0, 1]

Before: [2, 1, 3, 2]
14 1 3 1
After:  [2, 0, 3, 2]

Before: [1, 1, 1, 3]
6 1 0 3
After:  [1, 1, 1, 1]

Before: [0, 1, 1, 2]
14 1 3 3
After:  [0, 1, 1, 0]

Before: [3, 1, 0, 3]
8 0 2 0
After:  [1, 1, 0, 3]

Before: [1, 0, 2, 1]
15 3 2 0
After:  [1, 0, 2, 1]

Before: [0, 1, 2, 2]
13 3 3 1
After:  [0, 0, 2, 2]

Before: [3, 1, 2, 1]
15 3 2 0
After:  [1, 1, 2, 1]

Before: [1, 1, 1, 2]
6 1 0 0
After:  [1, 1, 1, 2]

Before: [1, 1, 2, 1]
13 3 3 2
After:  [1, 1, 0, 1]

Before: [0, 1, 1, 1]
0 0 0 3
After:  [0, 1, 1, 0]

Before: [0, 1, 0, 0]
10 1 3 3
After:  [0, 1, 0, 1]

Before: [1, 1, 0, 0]
6 1 0 1
After:  [1, 1, 0, 0]

Before: [0, 1, 2, 1]
13 3 3 0
After:  [0, 1, 2, 1]

Before: [1, 3, 2, 3]
3 2 1 0
After:  [1, 3, 2, 3]

Before: [1, 2, 0, 2]
9 0 2 2
After:  [1, 2, 0, 2]

Before: [1, 3, 2, 1]
15 3 2 3
After:  [1, 3, 2, 1]

Before: [2, 2, 0, 3]
7 1 3 2
After:  [2, 2, 0, 3]

Before: [1, 1, 2, 3]
7 1 3 0
After:  [0, 1, 2, 3]

Before: [1, 0, 2, 1]
1 0 2 3
After:  [1, 0, 2, 0]

Before: [1, 2, 2, 2]
1 0 2 0
After:  [0, 2, 2, 2]

Before: [1, 1, 0, 3]
6 1 0 1
After:  [1, 1, 0, 3]

Before: [1, 2, 2, 2]
1 0 2 1
After:  [1, 0, 2, 2]

Before: [1, 1, 2, 3]
7 2 3 2
After:  [1, 1, 0, 3]

Before: [1, 1, 0, 2]
14 1 3 3
After:  [1, 1, 0, 0]

Before: [0, 1, 1, 2]
0 0 0 3
After:  [0, 1, 1, 0]

Before: [1, 0, 1, 1]
13 2 3 3
After:  [1, 0, 1, 0]

Before: [3, 1, 2, 2]
14 1 3 1
After:  [3, 0, 2, 2]

Before: [2, 1, 1, 0]
4 0 1 2
After:  [2, 1, 1, 0]

Before: [0, 2, 1, 1]
13 3 3 0
After:  [0, 2, 1, 1]

Before: [0, 3, 1, 3]
11 3 3 1
After:  [0, 3, 1, 3]

Before: [1, 3, 0, 2]
9 0 2 3
After:  [1, 3, 0, 0]

Before: [3, 2, 2, 3]
7 2 3 0
After:  [0, 2, 2, 3]

Before: [2, 1, 2, 2]
2 1 2 1
After:  [2, 0, 2, 2]

Before: [2, 2, 2, 1]
15 3 2 2
After:  [2, 2, 1, 1]

Before: [3, 3, 1, 1]
13 3 3 3
After:  [3, 3, 1, 0]

Before: [2, 2, 2, 3]
5 2 0 3
After:  [2, 2, 2, 1]

Before: [0, 3, 2, 3]
11 3 3 3
After:  [0, 3, 2, 3]

Before: [2, 3, 2, 0]
3 2 1 2
After:  [2, 3, 1, 0]

Before: [2, 1, 2, 1]
2 1 2 0
After:  [0, 1, 2, 1]

Before: [3, 3, 1, 3]
7 2 3 2
After:  [3, 3, 0, 3]

Before: [3, 0, 2, 0]
11 2 2 0
After:  [2, 0, 2, 0]

Before: [0, 3, 1, 2]
0 0 0 2
After:  [0, 3, 0, 2]

Before: [1, 1, 2, 0]
2 1 2 1
After:  [1, 0, 2, 0]

Before: [3, 1, 3, 2]
12 3 2 3
After:  [3, 1, 3, 2]

Before: [0, 0, 1, 2]
0 0 0 0
After:  [0, 0, 1, 2]

Before: [3, 1, 1, 1]
8 3 1 1
After:  [3, 0, 1, 1]

Before: [0, 0, 2, 1]
0 0 0 0
After:  [0, 0, 2, 1]

Before: [1, 1, 2, 3]
1 0 2 1
After:  [1, 0, 2, 3]

Before: [2, 3, 2, 0]
3 2 1 1
After:  [2, 1, 2, 0]

Before: [1, 3, 3, 2]
12 3 2 1
After:  [1, 2, 3, 2]

Before: [0, 1, 3, 2]
0 0 0 1
After:  [0, 0, 3, 2]

Before: [2, 1, 2, 0]
10 1 3 2
After:  [2, 1, 1, 0]

Before: [2, 2, 3, 2]
12 0 2 0
After:  [2, 2, 3, 2]

Before: [2, 0, 2, 3]
7 2 3 0
After:  [0, 0, 2, 3]

Before: [3, 1, 3, 3]
11 3 3 2
After:  [3, 1, 3, 3]

Before: [3, 1, 3, 0]
10 1 3 3
After:  [3, 1, 3, 1]

Before: [0, 1, 1, 3]
7 2 3 0
After:  [0, 1, 1, 3]

Before: [1, 1, 2, 0]
1 0 2 2
After:  [1, 1, 0, 0]

Before: [1, 1, 1, 0]
10 1 3 3
After:  [1, 1, 1, 1]

Before: [1, 1, 3, 2]
13 3 3 3
After:  [1, 1, 3, 0]

Before: [2, 0, 3, 1]
8 0 1 0
After:  [1, 0, 3, 1]

Before: [3, 2, 2, 3]
3 2 0 0
After:  [1, 2, 2, 3]

Before: [0, 3, 2, 3]
0 0 0 2
After:  [0, 3, 0, 3]

Before: [2, 2, 1, 2]
13 3 3 3
After:  [2, 2, 1, 0]

Before: [0, 2, 3, 3]
5 3 2 0
After:  [1, 2, 3, 3]

Before: [2, 1, 2, 2]
2 1 2 3
After:  [2, 1, 2, 0]

Before: [2, 1, 0, 3]
4 0 1 1
After:  [2, 1, 0, 3]

Before: [2, 1, 1, 0]
10 1 3 0
After:  [1, 1, 1, 0]

Before: [2, 3, 3, 2]
12 3 2 1
After:  [2, 2, 3, 2]

Before: [3, 2, 3, 1]
5 2 3 2
After:  [3, 2, 0, 1]

Before: [3, 3, 3, 1]
5 2 3 1
After:  [3, 0, 3, 1]

Before: [1, 1, 3, 3]
7 1 3 1
After:  [1, 0, 3, 3]

Before: [2, 1, 2, 3]
2 1 2 2
After:  [2, 1, 0, 3]

Before: [3, 1, 2, 3]
2 1 2 0
After:  [0, 1, 2, 3]

Before: [3, 1, 3, 1]
5 2 3 0
After:  [0, 1, 3, 1]

Before: [0, 2, 3, 3]
12 1 2 2
After:  [0, 2, 2, 3]

Before: [1, 0, 2, 2]
1 0 2 0
After:  [0, 0, 2, 2]

Before: [1, 1, 1, 2]
6 1 0 3
After:  [1, 1, 1, 1]

Before: [0, 3, 3, 1]
13 3 3 0
After:  [0, 3, 3, 1]

Before: [2, 1, 2, 1]
4 0 1 3
After:  [2, 1, 2, 1]

Before: [1, 1, 1, 3]
7 2 3 1
After:  [1, 0, 1, 3]

Before: [0, 3, 1, 2]
0 0 0 0
After:  [0, 3, 1, 2]

Before: [3, 3, 2, 2]
4 0 2 1
After:  [3, 1, 2, 2]

Before: [0, 3, 2, 2]
3 2 1 2
After:  [0, 3, 1, 2]

Before: [3, 1, 1, 3]
7 2 3 3
After:  [3, 1, 1, 0]

Before: [2, 1, 2, 1]
15 3 2 1
After:  [2, 1, 2, 1]

Before: [1, 1, 1, 0]
6 1 0 3
After:  [1, 1, 1, 1]

Before: [1, 3, 3, 2]
12 3 2 2
After:  [1, 3, 2, 2]

Before: [3, 1, 1, 2]
14 1 3 1
After:  [3, 0, 1, 2]

Before: [0, 2, 2, 3]
0 0 0 0
After:  [0, 2, 2, 3]

Before: [1, 1, 2, 3]
6 1 0 3
After:  [1, 1, 2, 1]

Before: [1, 1, 1, 0]
6 1 0 1
After:  [1, 1, 1, 0]

Before: [2, 3, 1, 3]
7 2 3 3
After:  [2, 3, 1, 0]

Before: [0, 1, 3, 0]
0 0 0 0
After:  [0, 1, 3, 0]

Before: [3, 0, 0, 3]
11 3 3 0
After:  [3, 0, 0, 3]

Before: [3, 1, 2, 1]
9 1 3 0
After:  [1, 1, 2, 1]

Before: [3, 0, 2, 1]
15 3 2 0
After:  [1, 0, 2, 1]

Before: [1, 1, 1, 1]
6 1 0 1
After:  [1, 1, 1, 1]""".split("\n")


program = """1 2 3 0
1 0 0 3
0 2 0 2
6 2 3 2
8 3 2 0
0 0 3 0
10 1 0 1
15 1 1 2
1 3 3 3
1 1 3 0
1 2 0 1
1 1 3 0
0 0 2 0
10 0 2 2
15 2 0 3
1 0 2 1
1 1 1 0
1 3 0 2
0 0 2 0
0 0 2 0
10 0 3 3
15 3 3 1
1 0 0 2
1 3 0 0
1 0 1 3
13 2 0 0
0 0 1 0
10 1 0 1
15 1 2 0
1 2 2 2
1 1 3 1
12 2 3 3
0 3 1 3
0 3 1 3
10 0 3 0
15 0 1 1
1 3 1 2
1 0 1 3
1 3 2 0
2 0 2 2
0 2 1 2
10 1 2 1
15 1 1 2
0 2 0 0
6 0 1 0
0 0 0 1
6 1 2 1
1 2 1 3
12 1 3 0
0 0 3 0
10 0 2 2
15 2 1 0
1 3 3 1
1 0 2 3
1 3 1 2
8 3 2 3
0 3 3 3
10 0 3 0
15 0 2 3
1 3 1 0
1 0 2 2
1 0 2 1
13 2 0 0
0 0 3 0
10 0 3 3
1 3 2 2
0 0 0 0
6 0 3 0
1 2 1 1
11 1 0 0
0 0 3 0
10 3 0 3
1 1 3 0
0 3 0 1
6 1 1 1
1 2 2 2
15 0 2 1
0 1 2 1
10 3 1 3
15 3 0 2
1 3 2 1
1 2 2 3
1 0 2 0
14 1 3 1
0 1 3 1
0 1 2 1
10 2 1 2
15 2 3 0
1 3 2 2
1 3 1 1
2 1 2 3
0 3 3 3
10 0 3 0
15 0 3 1
0 3 0 3
6 3 1 3
1 1 3 0
1 2 0 2
15 0 2 0
0 0 1 0
10 0 1 1
15 1 1 0
1 3 2 1
1 0 3 2
1 2 3 2
0 2 1 2
10 2 0 0
15 0 2 1
1 1 3 0
1 0 3 3
1 2 3 2
7 3 2 3
0 3 3 3
10 3 1 1
15 1 2 0
0 2 0 2
6 2 0 2
1 3 0 3
1 0 0 1
2 3 2 3
0 3 1 3
10 3 0 0
15 0 2 3
1 3 1 0
0 3 0 1
6 1 3 1
2 0 2 2
0 2 3 2
10 2 3 3
15 3 0 2
1 2 2 0
1 2 0 3
0 1 0 1
6 1 2 1
5 0 3 0
0 0 2 0
10 2 0 2
15 2 3 0
1 0 1 2
0 1 0 1
6 1 1 1
1 1 2 3
0 3 2 2
0 2 3 2
0 2 2 2
10 2 0 0
15 0 1 2
1 1 2 0
1 0 1 3
1 3 0 1
6 0 1 0
0 0 1 0
0 0 3 0
10 2 0 2
15 2 0 1
0 1 0 0
6 0 0 0
1 2 2 2
7 3 2 3
0 3 2 3
0 3 2 3
10 3 1 1
1 0 2 3
12 2 3 0
0 0 2 0
10 1 0 1
0 2 0 3
6 3 3 3
0 0 0 2
6 2 0 2
0 3 0 0
6 0 2 0
2 3 2 3
0 3 1 3
10 3 1 1
1 2 3 3
1 3 3 2
1 1 3 0
9 0 3 2
0 2 1 2
10 2 1 1
15 1 1 3
1 3 3 2
1 0 0 1
6 0 1 1
0 1 3 1
10 1 3 3
15 3 2 2
1 3 2 3
1 1 0 1
10 0 0 1
0 1 1 1
10 2 1 2
15 2 1 1
1 0 2 2
1 3 1 0
0 0 0 3
6 3 2 3
8 2 3 3
0 3 2 3
10 3 1 1
15 1 0 2
1 2 0 0
1 1 1 3
0 2 0 1
6 1 3 1
4 0 3 1
0 1 2 1
0 1 2 1
10 2 1 2
1 3 1 1
1 2 3 3
3 0 1 0
0 0 2 0
10 2 0 2
15 2 3 1
1 0 3 2
1 3 3 0
8 2 3 0
0 0 2 0
0 0 2 0
10 0 1 1
15 1 3 0
1 2 2 2
1 3 2 1
1 0 2 3
7 3 2 1
0 1 2 1
10 0 1 0
15 0 0 3
0 0 0 2
6 2 0 2
1 3 1 1
1 1 1 0
6 0 1 0
0 0 3 0
0 0 2 0
10 3 0 3
15 3 3 1
1 1 2 0
0 2 0 2
6 2 2 2
1 0 1 3
7 3 2 2
0 2 1 2
10 2 1 1
15 1 1 2
0 1 0 0
6 0 2 0
1 2 2 1
1 1 1 3
4 0 3 1
0 1 2 1
10 1 2 2
0 1 0 3
6 3 2 3
0 1 0 1
6 1 1 1
1 1 1 0
10 1 0 1
0 1 2 1
10 1 2 2
15 2 3 3
0 3 0 1
6 1 3 1
0 1 0 2
6 2 0 2
6 0 1 1
0 1 3 1
10 3 1 3
15 3 1 0
1 2 0 3
0 2 0 1
6 1 3 1
8 2 3 3
0 3 3 3
10 0 3 0
1 1 1 3
1 0 0 1
0 3 2 3
0 3 1 3
10 3 0 0
15 0 3 1
1 1 3 3
1 3 1 0
0 2 0 2
6 2 2 2
11 2 0 0
0 0 1 0
10 1 0 1
15 1 3 0
1 0 0 3
0 2 0 2
6 2 3 2
1 1 3 1
0 1 2 3
0 3 1 3
0 3 3 3
10 0 3 0
15 0 1 2
1 1 3 0
0 2 0 1
6 1 0 1
1 1 0 3
6 0 1 1
0 1 3 1
10 2 1 2
15 2 3 0
1 3 2 1
1 0 2 2
6 3 1 2
0 2 3 2
10 2 0 0
1 0 3 1
1 0 3 3
0 3 0 2
6 2 2 2
7 3 2 1
0 1 3 1
10 0 1 0
15 0 2 1
1 1 3 3
0 3 0 0
6 0 3 0
0 2 0 2
6 2 0 2
1 2 3 3
0 3 1 3
10 1 3 1
15 1 1 2
1 2 3 3
1 2 3 1
14 0 1 0
0 0 1 0
10 2 0 2
15 2 0 0
0 0 0 3
6 3 0 3
1 2 0 2
1 0 2 1
7 3 2 2
0 2 1 2
0 2 3 2
10 0 2 0
15 0 3 3
1 2 2 2
1 2 2 1
0 1 0 0
6 0 3 0
11 1 0 1
0 1 3 1
10 1 3 3
15 3 3 1
1 2 1 0
0 0 0 3
6 3 1 3
1 0 0 2
4 0 3 3
0 3 1 3
10 3 1 1
15 1 1 3
1 1 3 0
1 1 1 1
10 1 0 2
0 2 3 2
10 2 3 3
15 3 1 1
1 2 1 3
1 2 2 2
12 2 3 3
0 3 3 3
10 1 3 1
15 1 3 2
1 2 1 1
1 2 2 3
1 3 2 0
14 0 3 1
0 1 1 1
10 1 2 2
1 2 0 1
11 1 0 1
0 1 3 1
0 1 2 1
10 1 2 2
1 2 2 1
14 0 1 1
0 1 2 1
0 1 2 1
10 1 2 2
15 2 0 0
1 0 2 2
1 3 3 1
0 0 0 3
6 3 3 3
2 3 2 1
0 1 1 1
10 0 1 0
15 0 1 1
1 0 2 3
0 1 0 2
6 2 3 2
1 1 3 0
8 3 2 3
0 3 2 3
0 3 3 3
10 3 1 1
15 1 3 2
1 2 3 3
1 2 3 1
0 0 0 0
6 0 2 0
5 0 3 3
0 3 1 3
10 2 3 2
15 2 0 3
1 1 0 0
0 3 0 2
6 2 0 2
0 0 2 0
0 0 2 0
10 0 3 3
15 3 3 1
0 1 0 0
6 0 3 0
1 2 1 3
1 1 3 2
2 0 2 3
0 3 1 3
0 3 2 3
10 1 3 1
1 1 1 0
1 2 3 3
1 2 3 2
15 0 2 3
0 3 1 3
10 1 3 1
1 3 3 0
1 1 2 3
3 2 0 3
0 3 1 3
0 3 2 3
10 1 3 1
15 1 2 0
1 3 2 2
1 1 0 3
1 3 3 1
2 1 2 3
0 3 3 3
0 3 3 3
10 3 0 0
1 0 0 3
0 1 0 1
6 1 2 1
1 2 3 2
7 3 2 1
0 1 2 1
10 0 1 0
15 0 3 2
1 2 0 0
1 2 0 3
1 3 2 1
5 0 3 1
0 1 3 1
0 1 1 1
10 1 2 2
15 2 3 1
1 3 0 3
1 1 2 0
0 1 0 2
6 2 0 2
2 3 2 3
0 3 3 3
10 1 3 1
15 1 1 2
1 3 0 1
1 2 1 3
1 0 2 0
14 1 3 3
0 3 3 3
0 3 3 3
10 3 2 2
15 2 1 1
1 0 2 2
1 2 3 0
0 0 0 3
6 3 1 3
0 3 2 0
0 0 3 0
10 1 0 1
15 1 0 3
1 2 2 2
1 1 3 0
1 3 0 1
10 0 0 0
0 0 3 0
10 3 0 3
15 3 0 0
0 3 0 2
6 2 0 2
1 1 1 3
6 3 1 3
0 3 1 3
0 3 3 3
10 0 3 0
15 0 1 1
0 0 0 2
6 2 2 2
1 1 2 3
1 2 0 0
4 0 3 3
0 3 1 3
0 3 2 3
10 1 3 1
1 0 1 0
1 0 0 2
1 2 3 3
8 2 3 3
0 3 2 3
10 1 3 1
1 3 3 0
1 2 1 3
14 0 3 2
0 2 3 2
10 1 2 1
15 1 0 2
1 2 0 0
1 3 1 1
3 0 1 3
0 3 3 3
10 2 3 2
15 2 2 3
1 3 0 2
14 1 0 2
0 2 3 2
10 3 2 3
15 3 3 1
1 0 2 0
1 0 2 2
0 1 0 3
6 3 2 3
1 2 0 0
0 0 1 0
0 0 1 0
10 1 0 1
15 1 3 3
1 3 3 1
1 2 3 0
1 1 1 2
14 1 0 1
0 1 3 1
10 1 3 3
15 3 0 2
1 0 2 1
1 2 1 3
5 0 3 1
0 1 1 1
10 2 1 2
15 2 3 1
1 0 1 3
1 1 0 0
1 2 1 2
7 3 2 0
0 0 3 0
0 0 2 0
10 1 0 1
0 2 0 0
6 0 3 0
1 1 2 3
1 3 3 2
0 3 2 0
0 0 2 0
10 0 1 1
15 1 0 0
1 0 3 2
0 1 0 1
6 1 0 1
6 3 1 1
0 1 1 1
10 1 0 0
15 0 1 3
1 1 0 0
1 0 2 1
6 0 1 1
0 1 2 1
0 1 3 1
10 3 1 3
15 3 1 0
1 0 1 1
1 2 3 3
8 2 3 3
0 3 1 3
0 3 1 3
10 3 0 0
15 0 0 1
1 1 1 3
0 0 0 0
6 0 2 0
1 2 0 2
9 3 0 3
0 3 3 3
0 3 1 3
10 1 3 1
1 3 3 2
1 2 2 3
13 0 2 2
0 2 1 2
10 2 1 1
15 1 0 0
1 0 0 3
1 1 3 1
1 2 2 2
7 3 2 3
0 3 2 3
0 3 3 3
10 3 0 0
15 0 2 1
1 1 2 0
1 3 2 2
1 2 0 3
9 0 3 3
0 3 3 3
10 3 1 1
1 1 0 3
1 2 2 0
9 3 0 2
0 2 3 2
10 1 2 1
1 0 0 2
9 3 0 0
0 0 3 0
10 1 0 1
15 1 3 2
1 2 0 1
1 2 2 0
9 3 0 0
0 0 2 0
10 2 0 2
1 2 2 3
1 2 1 0
12 1 3 3
0 3 1 3
10 3 2 2
1 1 0 0
0 1 0 3
6 3 2 3
9 0 3 1
0 1 1 1
10 1 2 2
15 2 2 0
0 2 0 2
6 2 3 2
1 3 0 1
14 1 3 2
0 2 2 2
10 0 2 0
15 0 1 2
1 2 1 0
0 1 0 1
6 1 1 1
1 1 0 3
4 0 3 3
0 3 2 3
10 2 3 2
15 2 0 0
0 3 0 3
6 3 0 3
1 2 3 2
7 3 2 1
0 1 3 1
10 1 0 0
15 0 2 1
1 2 0 0
0 2 0 3
6 3 3 3
1 3 2 2
13 0 2 0
0 0 2 0
0 0 1 0
10 1 0 1
1 2 3 2
1 0 3 3
1 0 1 0
12 2 3 2
0 2 2 2
10 1 2 1
15 1 1 2
1 0 0 1
1 2 1 3
1 2 3 0
5 0 3 3
0 3 2 3
10 3 2 2
15 2 1 3
1 3 1 0
1 2 3 2
3 2 0 1
0 1 2 1
10 1 3 3
15 3 1 1
0 1 0 0
6 0 2 0
0 3 0 3
6 3 1 3
4 0 3 2
0 2 1 2
10 2 1 1
15 1 0 3
1 1 0 0
1 0 0 1
1 1 2 2
6 0 1 1
0 1 3 1
10 1 3 3
15 3 0 0
0 1 0 1
6 1 2 1
1 3 1 3
1 0 0 2
14 3 1 2
0 2 1 2
10 0 2 0
15 0 3 3
0 3 0 2
6 2 1 2
1 3 0 0
0 1 0 1
6 1 3 1
2 0 2 1
0 1 2 1
10 1 3 3
15 3 3 1
1 2 0 0
1 2 2 2
1 1 2 3
4 0 3 0
0 0 2 0
10 0 1 1
15 1 1 3
1 3 0 1
1 1 2 0
1 0 2 2
0 0 2 1
0 1 2 1
10 3 1 3
1 2 0 1
1 2 3 2
15 0 2 0
0 0 1 0
10 0 3 3
15 3 1 0
1 3 1 1
0 1 0 3
6 3 1 3
6 3 1 3
0 3 3 3
10 0 3 0
15 0 3 1
1 0 0 3
1 3 0 0
11 2 0 2
0 2 1 2
10 1 2 1
1 0 1 2
1 0 0 0
1 3 0 2
0 2 3 2
10 2 1 1
1 1 2 0
1 0 3 2
1 1 3 3
0 3 2 3
0 3 2 3
10 1 3 1
15 1 0 3
1 2 3 2
1 3 0 0
1 3 0 1
3 2 1 0
0 0 3 0
10 0 3 3
15 3 1 2
1 2 1 1
1 0 1 3
0 1 0 0
6 0 3 0
14 0 1 3
0 3 1 3
0 3 2 3
10 2 3 2
15 2 0 1
0 2 0 3
6 3 0 3
1 3 0 2
1 2 1 0
12 0 3 3
0 3 3 3
10 3 1 1
15 1 3 0
0 3 0 3
6 3 0 3
1 1 3 1
0 1 2 2
0 2 1 2
10 0 2 0
15 0 2 2
1 2 0 3
1 2 2 0
5 0 3 1
0 1 3 1
10 1 2 2
15 2 2 1
1 3 2 2
1 3 1 3
2 3 2 0
0 0 1 0
0 0 1 0
10 0 1 1
0 1 0 2
6 2 2 2
1 2 0 3
1 2 0 0
12 2 3 2
0 2 2 2
0 2 1 2
10 2 1 1
15 1 3 3
1 1 1 0
1 3 2 2
1 2 1 1
11 1 2 0
0 0 3 0
10 0 3 3
15 3 2 1
1 2 2 0
1 3 2 3
2 3 2 2
0 2 3 2
0 2 2 2
10 2 1 1
1 0 1 2
1 1 2 3
4 0 3 2
0 2 2 2
10 2 1 1
15 1 3 0
0 2 0 2
6 2 2 2
1 0 2 3
1 0 0 1
7 3 2 3
0 3 1 3
10 3 0 0
1 2 1 3
1 2 3 1
1 1 0 2
12 1 3 2
0 2 1 2
0 2 2 2
10 0 2 0
1 0 0 2
8 2 3 1
0 1 2 1
10 1 0 0
15 0 1 3
1 2 3 2
0 0 0 0
6 0 1 0
1 3 0 1
15 0 2 1
0 1 2 1
10 3 1 3
15 3 2 1
1 2 1 0
1 1 0 2
0 2 0 3
6 3 2 3
5 0 3 2
0 2 2 2
10 2 1 1
15 1 1 0
1 1 2 3
0 0 0 1
6 1 0 1
0 1 0 2
6 2 1 2
10 3 3 2
0 2 1 2
10 0 2 0
15 0 2 2
1 2 3 0
1 2 1 1
1 2 0 3
12 1 3 0
0 0 2 0
10 2 0 2
0 1 0 1
6 1 3 1
1 1 1 3
1 0 0 0
6 3 1 3
0 3 2 3
10 2 3 2
15 2 1 0
1 3 1 2
1 0 1 3
8 3 2 2
0 2 2 2
10 0 2 0
15 0 1 2
1 1 2 1
1 1 0 0
1 1 0 3
10 0 0 0
0 0 2 0
0 0 3 0
10 0 2 2
15 2 0 0
0 0 0 2
6 2 2 2
0 3 0 1
6 1 2 1
10 3 3 3
0 3 1 3
0 3 1 3
10 3 0 0
15 0 0 1
1 3 0 0
1 3 2 3
3 2 0 2
0 2 3 2
10 2 1 1
15 1 1 3
1 1 3 1
1 3 1 2
0 1 2 1
0 1 2 1
10 3 1 3
15 3 2 0""".split("\n")

grouped_rules = [
    opcode_samples[i:i+3] 
    for i in range(0, len(opcode_samples), 4)
    ]

rules = [
    (
        [int(x) for x in g[0][9:-1].split(", ")], 
        [int(x) for x in g[1].split(" ")],
        [int(x) for x in g[2][9:-1].split(", ")]
        ) for g in grouped_rules ]

def seti(regs, a, b, o):
    regs[o] = a
    return regs

def getr(regs, r):
    return regs[r]

def addr(regs, a, b, c): 
    return seti(regs, getr(regs, a) + getr(regs, b), None, c)

def addi(regs, a, b, c): 
    return seti(regs, getr(regs, a) + b, None, c)

def mulr(regs, a, b, c): 
    return seti(regs, getr(regs, a) * getr(regs, b), None, c)

def muli(regs, a, b, c): 
    return seti(regs, getr(regs, a) * b, None, c)

def banr(regs, a, b, c): 
    return seti(regs, getr(regs, a) & getr(regs, b), None, c)

def bani(regs, a, b, c): 
    return seti(regs, getr(regs, a) & b, None, c)

def borr(regs, a, b, c): 
    return seti(regs, getr(regs, a) | getr(regs, b), None, c)

def bori(regs, a, b, c): 
    return seti(regs, getr(regs, a) | b, None, c)

def setr(regs, a, b, c): 
    return seti(regs, getr(regs, a), None, c)

def gtir(regs, a, b, c): 
    return seti(regs, 1 if a > getr(regs, b) else 0, None, c)

def gtri(regs, a, b, c): 
    return seti(regs, 1 if getr(regs, a) > b else 0, None, c)

def gtrr(regs, a, b, c): 
    return seti(regs, 1 if getr(regs, a) > getr(regs, b) else 0, None, c)

def eqir(regs, a, b, c): 
    return seti(regs, 1 if a == getr(regs, b) else 0, None, c)

def eqri(regs, a, b, c): 
    return seti(regs, 1 if getr(regs, a) == b else 0, None, c)

def eqrr(regs, a, b, c): 
    return seti(regs, 1 if getr(regs, a) == getr(regs, b) else 0, None, c)

operators = [
    addr, addi, mulr, muli, 
    banr, bani, borr, bori,
    setr, seti, 
    gtir, gtri, gtrr, 
    eqir, eqri, eqrr, 
    ]


samples_behaving_like_three_or_more_instructions = 0
for input, instruction, output in rules:
    candidates = [
        operator
        for operator in operators
        if operator(input.copy(), *instruction[1:]) == output
        ]
    if len(candidates) >= 3:
        samples_behaving_like_three_or_more_instructions += 1    
print("Part 1, samples behaving like 3 or more instructions: {}".format(
    samples_behaving_like_three_or_more_instructions
    ))



opcode_possibilities = {
    i: set(operators) for i in range(0, 16)
    }

for input, instruction, output in rules:   
    for operator in list(opcode_possibilities[instruction[0]]):
        if operator(input.copy(), *instruction[1:]) != output:
            opcode_possibilities[instruction[0]].remove(operator)


opcode_possibilities = sorted(opcode_possibilities.items(), key=lambda x: len(x[1]))
opcode_possibilities = [(k, sorted(list(v), key=lambda f: f.__name__)) for k,v in opcode_possibilities]

indexes = [0] * len(opcode_possibilities)
indexes_i = 0

choices = [None] * len(opcode_possibilities)
while True:
    # pp [(k, ",".join(sorted([f.__name__ for f in v]))) for k,v in opcode_possibilities]
    while indexes_i < len(opcode_possibilities): # for i in range(indexes_i, len(indexes)):
        if indexes[indexes_i] >= len(opcode_possibilities[indexes_i][1]):
            #print("reversing: {}".format([n and n.__name__ for n in choices]))
            indexes[indexes_i] = 0
            choices[indexes_i] = None
            indexes_i -= 1
            if indexes_i < 0:
                print("unable to find a solution")
                import pdb; pdb.set_trace()
            indexes[indexes_i] += 1
            continue

        if opcode_possibilities[indexes_i][1][indexes[indexes_i]] in choices:
            #print("crash    : {}".format([n and n.__name__ for n in choices]))
            indexes[indexes_i] += 1
            continue
        else:
            choices[indexes_i] = opcode_possibilities[indexes_i][1][indexes[indexes_i]]
            #print("trying   : {}".format([n and n.__name__ for n in choices]))
            indexes_i += 1             
    else:
        break

opcode_map = {opcode_possibilities[i][0]: v for i, v in enumerate(choices)}

program_codes = [[int(v) for v in l.split(" ")] for l in program]
registers = [0, 0, 0, 0]

for instruction in program_codes:
    opcode_map[instruction[0]](registers, *instruction[1:])


print("Part 2, register 0: {}".format(registers[0]))
