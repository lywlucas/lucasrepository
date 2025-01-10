# Assignment #C: 五味杂陈 

Updated 1148 GMT+8 Dec 10, 2024

2024 fall, Complied by <mark>卢殷文 物院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 1115. 取石子游戏

dfs, https://www.acwing.com/problem/content/description/1117/

思路：

不妨假设a>=b.由于游戏没有平局，每一对a,b组合不是必胜就是必败。

当a>=2*b时，考虑(b,a%b)组合：

如果该组合必胜，则可以取成(b+a%b,b)组合，对手只有唯一解，于是我方获得必胜组合；

如果该组合必败，则取成该组合，对手必败，我方必胜。

综上所述，只要a>=2*b，先手必胜。

然而剩下的情况先手只有唯一操作，时间复杂度极低。

代码：

```python
import sys
sys.setrecursionlimit(10**8)

def game(a,b):
    if a==b or a>=2*b:
        return True
    else:
        return not game(b,a-b)

while True:
    try:
        a,b=map(int,input().split())
    except EOFError:
        break
    if a==b==0:
        break
    if b>a:
        a,b=b,a
    if game(a,b):
        print("win")
    else:
        print("lose")

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241210160041519](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241210160041519.png)



### 25570: 洋葱

Matrices, http://cs101.openjudge.cn/practice/25570

思路：

输入输出题

代码：

```python
n=int(input())
m=(n+1)//2
sum_storey=[0]*m
for i in range(n):
    l=list(map(int,input().split()))
    for j in range(n):
        flg=min(i,j,n-1-i,n-1-j)
        sum_storey[flg]+=l[j]
print(max(sum_storey))
```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-12-10 163337](D:\学习软件\2024秋\计算概论 闫鸿飞\作业C\屏幕截图 2024-12-10 163337.png)



### 1526C1. Potions(Easy Version)

greedy, dp, data structures, brute force, *1500, https://codeforces.com/problemset/problem/1526/C1

思路：

O(n^2)都可以，那就简单dp

代码：

```python
INF=10**14
n=int(input())
potions=list(map(int,input().split()))
health=[0]
for i in range(n):
    health.append(0)
    for j in range(i,0,-1):
        health[j]=max(health[j]+potions[i],health[j-1])
        if health[j]<0:
            health[j]=-INF
    if health[0]+potions[i]>=0:
        health[0]+=potions[i]
    else:
        health[0]=-INF
for j in range(n+1):
    if health[j]>=0:
        print(n-j)
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241210165839974](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241210165839974.png)

### 22067: 快速堆猪

辅助栈，http://cs101.openjudge.cn/practice/22067/

思路：

使用min_pigs存储此刻最小猪，注意min_pigs和pigs的长度差值不变

代码：

```python
import math
pigs=[]
min_pigs=[math.inf]
def pop():
    if pigs:
        pigs.pop()
        min_pigs.pop()
def push(x):
    pigs.append(x)
    min_pigs.append(min(x,min_pigs[-1]))
def getmin():
    if pigs:
        print(min_pigs[-1])

while True:
    try:
        s=input()
    except EOFError:
        break
    if s=='pop':
        pop()
    elif s=='min':
        getmin()
    else:
        s1,s2=s.split(' ')
        push(int(s2))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241210171625942](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241210171625942.png)



### 20106: 走山路

Dijkstra, http://cs101.openjudge.cn/practice/20106/

思路：

dijkstra还没有很熟练，debug了好一会

代码：

```python
import heapq
import math

m,n,p=map(int,input().split())
mat=[list(input().split()) for _ in range(m)]
def dijkstra(start_x,start_y,end_x,end_y,m,n):
    if mat[start_x][start_y]=="#" or mat[end_x][end_y]=="#":
        return "NO"
    heap=[]
    heapq.heappush(heap,(0,start_x,start_y))
    distance=[[math.inf]*n for _ in range(m)]
    distance[start_x][start_y]=0
    while heap:
        now,x,y=heapq.heappop(heap)
        if x==end_x and y==end_y:
            return now
        h=int(mat[x][y])
        for (dx,dy) in [(-1,0),(0,1),(1,0),(0,-1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and mat[nx][ny]!="#":
                if distance[nx][ny]>now+abs(h-int(mat[nx][ny])):
                    distance[nx][ny]=now+abs(h-int(mat[nx][ny]))
                    heapq.heappush(heap,(distance[nx][ny],nx,ny))
    return "NO"

for _ in range(p):
    x,y,z,w=map(int,input().split())
    print(dijkstra(x,y,z,w,m,n))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241210200513047](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241210200513047.png)



### 04129: 变换的迷宫

bfs, http://cs101.openjudge.cn/practice/04129/

思路：

将时间也看作迷宫的坐标，并加上周期性边界条件temp=(time+1)%k

代码：

```python
from collections import deque

def bfs(x, y):
    visited={(0, x, y)}
    queue=deque([(0, x, y)])
    while queue:
        time,x,y=queue.popleft()
        for (dx,dy) in [(0,1), (1,0), (-1,0), (0,-1)]:
            nx,ny=x+dx,y+dy
            temp=(time+1)%k
            if 0<=nx<r and 0<=ny<c and (temp,nx,ny) not in visited:
                now=maze[nx][ny]
                if now=='E':
                    return time+1
                elif now!='#'or temp==0:
                    queue.append((time+1,nx,ny))
                    visited.add((temp,nx,ny))
    return 'Oop!'

t = int(input())
for _ in range(t):
    r, c, k = map(int, input().split())
    maze = [list(input()) for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if maze[i][j] == 'S':
                print(bfs(i, j))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241210174343641](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241210174343641.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

这次作业总算是回归正常难度了

复习了dijkstra的写法；

主要在看笔试试题



