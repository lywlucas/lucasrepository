# Assignment #D: 十全十美 

Updated 1254 GMT+8 Dec 17, 2024

2024 fall, Complied by <mark>卢殷文</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 02692: 假币问题

brute force, http://cs101.openjudge.cn/practice/02692

思路：

枚举即可

代码：

```python
def check(coins,case):
    for i in range(3):
        left = sum(coins[ord(s) - ord('A')] for s in case[i][0])
        right = sum(coins[ord(s) - ord('A')] for s in case[i][1])
        flg = case[i][2]
        if left==right and flg!="even":
            return False
        elif left<right and flg!="down":
            return False
        elif left>right and flg!="up":
            return False
    return True

def do():
    case = [[], [], []]
    for i in range(3):
        case[i] = input().split()
    for i in range(12):
        coins = [0] * 12
        for (fallacy, f) in [(-1, "light"), (1, "heavy")]:
            coins[i] = fallacy
            if check(coins, case):
                print("%s is the counterfeit coin and it is %s." % (chr(ord('A') + i), f))
                return
n=int(input())
for _ in range(n):
    do()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241218201120405](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241218201120405.png)



### 01088: 滑雪

dp, dfs similar, http://cs101.openjudge.cn/practice/01088

思路：

按照高度从小到大递归

代码：

```python
r,c=map(int,input().split())
length=[[1]*c for _ in range(r)]
height=[[-1]*c for _ in range(r)]
manage=[]
for i in range(r):
    l=list(map(int,input().split()))
    for j in range(c):
        height[i][j]=l[j]
        manage.append((i,j,l[j]))
manage.sort(key=lambda x:x[2])
for (i,j,h) in manage:
    for (dx,dy) in [(1,0),(-1,0),(0,1),(0,-1)]:
        x,y=i+dx,j+dy
        if 0<=x<r and 0<=y<c and height[x][y]<height[i][j]:
            length[i][j]=max(length[i][j],length[x][y]+1)
print(max(max(length[i]) for i in range(r)))
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241218202941617](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241218202941617.png)



### 25572: 螃蟹采蘑菇

bfs, dfs, http://cs101.openjudge.cn/practice/25572/

思路：

用lx，ly表示螃蟹体型，每次bfs经过时加体型判定

代码：

```python
from collections import deque

n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))
a = []
for i in range(n):
    for j in range(n):
        if mat[i][j] == 5:
            a.append([i, j])
lx = a[1][0] - a[0][0]
ly = a[1][1] - a[0][1]
dire = [[-1, 0], [0, 1], [1, 0], [0, -1]]
v = [[0] * n for i in range(n)]


def bfs(x, y, lx, ly):
    v[x][y] = 1
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        if mat[x][y] == 9 and mat[x + lx][y + ly] != 1:
            return "yes"
        elif mat[x][y] != 1 and mat[x + lx][y + ly] == 9:
            return "yes"
        for i in range(4):
            dx = x + dire[i][0]
            dy = y + dire[i][1]
            if 0 <= dx < n and 0 <= dy < n and 0 <= dx + lx < n and 0 <= dy + ly < n:
                if v[dx][dy] == 0 and mat[dx][dy] != 1 and mat[dx + lx][dy + ly] != 1:
                    queue.append((dx, dy))
                    v[dx][dy] = 1
    return 'no'

print(bfs(a[0][0], a[0][1],lx,ly))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241218203750035](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241218203750035.png)



### 27373: 最大整数

dp, http://cs101.openjudge.cn/practice/27373/

思路：

这题出的很综合，把最大整数排序和0-1背包问题结合在一起。

代码：

```python
from functools import cmp_to_key
m=int(input())
n=int(input())
l=list(input().split())
l.sort(key = cmp_to_key(lambda x, y: int(y + x) - int(x + y)))
dp=[['']*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if len(l[i-1])>j:
            dp[i][j]=dp[i-1][j]
        else:
            now=dp[i-1][j-len(l[i-1])]+l[i-1]
            if dp[i-1][j]=='':
                dp[i][j]=now
            elif int(dp[i-1][j])<int(now):
                dp[i][j]=now
            else:
                dp[i][j]=dp[i-1][j]
print(dp[n][m])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241218210628945](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241218210628945.png)



### 02811: 熄灯问题

brute force, http://cs101.openjudge.cn/practice/02811

思路：

题目的提示很重要，这意味着我们一旦确定了第一行的灯的情况，后续的所有情况就确定了。

这样我们只要枚举2**6种可能即可。

灯用0/1表示，那么按按钮就对应与1作异或操作。

---------------------------------------------------------------

看群里居然还有用线代知识变为m*n^2的，主要用到矩阵求逆，感觉好厉害

代码：

```python
from copy import deepcopy
from itertools import product

m = [[0] * 8] + [[0, *map(int, input().split()), 0] for i in range(5)] + [[0] * 8]
for test in product(range(2), repeat=6):
    matrix = deepcopy(m)
    triggers = [list(test)]
    for i in range(1,6):
        for j in range(1,7):
            if triggers[i-1][j-1]:
                for (dx,dy) in [(-1,0),(0,1),(1,0),(0,-1),(0,0)]:
                    matrix[i+dx][j+dy] = matrix[i+dx][j+dy]^1
        triggers.append(matrix[i][1:7])
    if matrix[5][1:7] == [0, 0, 0, 0, 0, 0]:
        for trigger in triggers[:-1]:
            print(' '.join(map(str, trigger)))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241218214121712](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241218214121712.png)



### 08210: 河中跳房子

binary search, greedy, http://cs101.openjudge.cn/practice/08210/

思路：

想了许久这题和二分查找有什么关系，最后豁然开朗，对所求值作二分查找，这样的偏大偏小判定是很好写的

代码：

```python
L,N,M=map(int,input().split())
locate=[0]+[int(input()) for _ in range(N)]+[L]

def check(x:int):
    cnt,now=0,0
    for i in range(1,N+2):
        if locate[i]-now<x:
            cnt+=1
        else:
            now=locate[i]
    if cnt>M:
        return True
    else:
        return False

lo,hi=0,L+1
ans=-1
while lo<hi:
    mid=(lo+hi)//2
    if check(mid):
        hi=mid
    else:
        ans=mid
        lo=mid+1
print(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241219104722866](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241219104722866.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

基本上进入期末复习了

正在整理cheat paper， 同时也有在复习笔试



