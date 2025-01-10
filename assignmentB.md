# Assignment #B: Dec Mock Exam大雪前一天

Updated 1649 GMT+8 Dec 5, 2024

2024 fall, Complied by <mark>卢殷文 物院</mark>



**说明：**

1）⽉考： <mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E22548: 机智的股民老张

http://cs101.openjudge.cn/practice/22548/

思路：

简单sort

代码：

```python
a=list(map(int,input().split()))
flg=0
maxa,mina=a[0],a[0]
for i in range(len(a)):
    maxa=max(a[i],maxa)
    if a[i]<mina:
        mina=a[i]
        maxa=a[i]
    flg=max(flg,maxa-mina)
print(flg)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241206085715569](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241206085715569.png)



### M28701: 炸鸡排

greedy, http://cs101.openjudge.cn/practice/28701/

思路：

这个greedy卡了有一会儿，最终想到先处理最大的鸡排，如果它小于平均时间，则已经做完了；否则它就一直在锅里，化成k-1，n-1的问题

代码：

```python
n,k=map(int,input().split())
t=list(map(int,input().split()))
t.sort()
def do(n,k):
    ans=sum(t)/k
    if t[-1]>ans:
        t.pop()
        return do(n-1,k-1)
    else:
        return ans
print("%.3f"%do(n,k))
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241206091350245](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241206091350245.png)



### M20744: 土豪购物

dp, http://cs101.openjudge.cn/practice/20744/

思路：

第一眼就觉得可以取关键元素为末尾坐标

终稿dp以末尾元素和去除标记作为坐标，思路还是比较自然的

代码：

```python
v=list(map(int,input().split(',')))
if max(v)<0:
    print(max(v))
else:
    buy1,buy2=[0],[0]
    for i in range(len(v)):
        buy1.append(max(v[i],buy1[i]+v[i]))
        buy2.append(max(buy1[i],buy2[i]+v[i]))
    print(max(max(buy1),max(buy2),max(v)))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241206094630158](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241206094630158.png)



### T25561: 2022决战双十一

brute force, dfs, http://cs101.openjudge.cn/practice/25561/

思路：

最多有5^8=3*10^5种情况，直接暴力枚举即可，利用itertools.product生成所有方案

思路不难实现，只是处理输入有点烦

代码：

```python
import itertools

inf=10**9
n,m=map(int,input().split())
p=[[inf]*m for _ in range(n)]
q=[[] for _ in range(m)]
for i in range(n):
    *sold,=input().split()
    for s in sold:
        si=int(s[0])-1
        pi=int(s[2:])
        p[i][si]=pi
for j in range(m):
    *quan,=input().split()
    for s in quan:
        a,b=map(int,s.split('-'))
        q[j].append([a,b])
plans=itertools.product(range(m),repeat=n)
final_money=inf
for plan in plans:
    money=[0]*m
    for i in range(n):
        money[plan[i]]+= p[i][plan[i]]
    final=sum(money)
    final-=final//300*50
    for j in range(m):
        maxq=0
        for qq in q[j]:
            if money[j]>=qq[0]:
                maxq=max(qq[1],maxq)
        final-=maxq
    if final<final_money:
        final_money=final
print(final_money)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241206105030601](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241206105030601.png)



### T20741: 两座孤岛最短距离

dfs, bfs, http://cs101.openjudge.cn/practice/20741/

思路：

这题时间卡的太死了，喜提n个TLE

被折磨了一个半小时后遂决定看题解

题解的高明之处在于：多源并行bfs，并省去了原先dfs的标记数组和bfs的in_queue集合，没有一丁点多余的操作

另外，同学的解利用Dijkstra算法，使用0作为陆地权值，也很巧妙



下面的代码就是题解的，不用看了

代码：

```python
from collections import deque

def dfs(x, y, grid, n, queue, directions):
    grid[x][y] = 2
    queue.append((x, y))
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
            dfs(nx, ny, grid, n, queue, directions)

def bfs(grid, n, queue, directions):
    distance = 0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if grid[nx][ny] == 1:
                        return distance
                    elif grid[nx][ny] == 0:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
        distance += 1
    return distance

def main():
    n = int(input())
    grid = [list(map(int, input())) for _ in range(n)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque()

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i, j, grid, n, queue, directions)
                return bfs(grid, n, queue, directions)

if __name__ == "__main__":
    print(main())

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241206124254777](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241206124254777.png)



### T28776: 国王游戏

greedy, http://cs101.openjudge.cn/practice/28776

思路：

感觉这一题反而是所有题中最简单的（？）

就是考虑所有人左手的总乘积$\Pi$一定，最后一个人的奖赏就是$\Pi$/(a*b)，所以只要按左右手乘积排序就行

不难证明，这样的排序下任何换位的行为都会增大最大值。

代码：

```python
n=int(input())
pl=[]
maxv=0
reward,x=map(int,input().split())
for _ in range(n):
    ai,bi=map(int,input().split())
    pl.append((ai,bi))
pl.sort(key=lambda x:x[0]*x[1])
for i in range(n):
    v=reward//pl[i][1]
    maxv=max(maxv,v)
    reward*=pl[i][0]
print(maxv)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241206112212538](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241206112212538.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>



庆幸月考不在现场，不然按作业的进度可能只对两三道……orz

收获最大的在两孤岛问题

