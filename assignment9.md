# Assignment #9: dfs, bfs, & dp

Updated 2107 GMT+8 Nov 19, 2024

2024 fall, Complied by <mark>卢殷文  物院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 18160: 最大连通域面积

dfs similar, http://cs101.openjudge.cn/practice/18160

思路：

简单dfs

有一个坑点是，如果输入全是“.”的话答案数组为空，调用max函数会RTE；解决方案是，在dfs函数时加"."对应 return 0，或者直接在答案数组创建时带上0

代码：

```python
def area(i,j):
    #if chess[i][j]==0:
    #    return 0
    ans=1
    chess[i][j]=1
    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            if chess[x][y]==-1:
                ans+=area(x,y)
    return ans

T=int(input())
for t in range(T):
    n,m=map(int,input().split())
    chess=[[0 for _ in range(m+2)]]
    for i in range(n):
        s=input()
        now=[0]
        for j in range(m):
            if s[j]=="W":
                now.append(-1)
            else:
                now.append(0)
        now.append(0)
        chess.append(now)
    chess.append([0 for _ in range(m+2)])
    island = [0]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if chess[i][j] == -1:
                island.append(area(i, j))
    print(max(island))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241120093921009](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241120093921009.png)



### 19930: 寻宝

bfs, http://cs101.openjudge.cn/practice/19930

思路：

简单广搜

代码：

```python
from collections import deque

m,n=map(int,input().split())
loca=[[2]*(n+2)]
for i in range(m):
    l=list(map(int,input().split()))
    loca.append([2]+l+[2])
loca.append([2]*(n+2))

def bfs(start_x,start_y):
    q=deque([(0,start_x,start_y)])
    in_queue={(start_x,start_y)}

    while q:
        step,x,y=q.popleft()
        if loca[x][y]==1:
            return step
        for (i,j) in [(x,y+1),(x,y-1),(x-1,y),(x+1,y)]:
            if loca[i][j]!=2 and (i,j) not in in_queue:
                in_queue.add((i,j))
                q.append((step+1,i,j))
    return "NO"

print(bfs(1,1))
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241120153744269](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241120153744269.png)



### 04123: 马走日

dfs, http://cs101.openjudge.cn/practice/04123

思路：



代码：

```python
def ri(x,y,n,m):
    l=[]
    for i in [-2,2]:
        for j in [-1,1]:
            if 0<=x+i<n and 0<=y+j<m:
                l.append((x+i,y+j))
            if 0<=x+j<n and 0<=y+i<m:
                l.append((x+j,y+i))
    return l

def dfs(cnt,x,y,n,m):
    if cnt>=n*m:
        return 1
    ans=0
    for (i,j) in ri(x,y,n,m):
        if flg[i][j]!=1:
            flg[i][j]=1
            ans+=dfs(cnt+1,i,j,n,m)
            flg[i][j]=0
    return ans

t=int(input())
for _ in range(t):
    n,m,x,y=map(int,input().split())
    flg = [[0] * m for _ in range(n)]
    flg[x][y]=1
    print(dfs(1,x,y,n,m))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241120170042939](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241120170042939.png)



### sy316: 矩阵最大权值路径

dfs, https://sunnywhy.com/sfbj/8/1/316

思路：

使用全局变量存储最值和其路径

代码：

```python
def dfs(x,y,n,m,now):
    global maxv,final
    if x==n-1 and y==m-1:
        if now>maxv:
            maxv=now
            final=temp[:]
        return
    flg[x][y]=1
    for (i,j) in [(-1,0),(0,1),(1,0),(0,-1)]:
        if 0<=x+i<n and 0<=y+j<m and flg[x+i][y+j]!=1:
            temp.append((x+i,y+j))
            dfs(x+i,y+j,n,m,now+mat[x+i][y+j])
            temp.pop()
    flg[x][y]=0
n,m=map(int,input().split())
maxv=-10**6
final=[]
temp=[(0,0)]
flg=[[0]*m for _ in range(n)]
mat=[]
for i in range(n):
    mm=list(map(int,input().split()))
    mat.append(mm)
dfs(0,0,n,m,mat[0][0])
for xi, yi in final:
    print(xi+1, yi+1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241120205859962](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241120205859962.png)



### LeetCode62.不同路径

dp, https://leetcode.cn/problems/unique-paths/

思路：

简单前缀和

代码：

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        l = [1] * n
        for _ in range(1, m):
            for i in range(1, n):
                l[i] += l[i - 1]
        return l[n - 1]

```

![image-20241121113026497](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241121113026497.png)

代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### sy358: 受到祝福的平方

dfs, dp, https://sunnywhy.com/sfbj/8/3/539

思路：

recursion

代码：

```python
from math import sqrt
from functools import lru_cache

def is_power(s:str):
    n=int(s)
    if n==0:
        return False
    elif int(sqrt(n))**2 == n:
        return True
    else:
        return False

@lru_cache(maxsize=256)
def blessed(s:str):
    if is_power(s):
        return True
    for i in range(1,len(s)):
        if blessed(s[:i]) and blessed(s[i:]):
            return True
    return False

a=input()
if blessed(a):
    print("Yes")
else:
    print("No")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241121114722604](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241121114722604.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

通过这次作业复习了bfs和dfs的基本写法；找了点力扣的题练练

感觉还是上次的田忌赛马题有意思，看了群里的讨论收获颇深



