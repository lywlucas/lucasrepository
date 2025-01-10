# Assignment #10: dp & bfs

Updated 2 GMT+8 Nov 25, 2024

2024 fall, Complied by <mark>卢殷文 物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### LuoguP1255 数楼梯

dp, bfs, https://www.luogu.com.cn/problem/P1255

思路：

math

代码：

```python
from math import comb
n=int(input())
ans=0
for i in range(0,n//2+1):
    ans+=comb(n-i,i)
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241126100228280](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241126100228280.png)



### 27528: 跳台阶

dp, http://cs101.openjudge.cn/practice/27528/

思路：

等价于在每两个台阶之间的间隔处决定是否停留，一共有n-1个间隔，所以共2^(n-1)种情况

代码：

```python
n=int(input())
print(2**(n-1))
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241126100508345](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241126100508345.png)



### 474D. Flowers

dp, https://codeforces.com/problemset/problem/474/D

思路：

相当于积累了k个R后可以翻成k个W

a[i]=a[i-1]+a[i-k]

代码：

```python
t,k=map(int,input().split())
N=10**9+7
ways=[1]*k
foresum=[n for n in range(k)]
for i in range(k,10**5+2):
    ways.append((ways[-1]+ways[-k])%N)
    foresum.append((foresum[-1]+ways[-1])%N)
for _ in range(t):
    a,b=map(int,input().split())
    print((foresum[b]-foresum[a-1])%N)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241126143453145](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241126143453145.png)



### LeetCode5.最长回文子串

dp, two pointers, string, https://leetcode.cn/problems/longest-palindromic-substring/

思路：

估计了以下时间复杂度，暴力解法O(n^3)也可以过

AC后看了题解，试图理解了Manacher's Algorithm算法，确实很妙

代码：

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ans=""
        leng=0
        for i in range(n):
            for j in range(i+1,n+1):
                s1=s[i:j]
                if s1==s1[::-1] and j-i>leng:
                    leng=j-i
                    ans=s1
        return ans

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241126145227461](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241126145227461.png)





### 12029: 水淹七军

bfs, dfs, http://cs101.openjudge.cn/practice/12029/

思路：

一开始死活RTE，最终找不着原因去群里看了一眼，得知要调用sys读取数据，尝试后AC

代码：

```python
import sys

sys.setrecursionlimit(30000)
input=sys.stdin.read


def dfs(x,y,m,n,h):
    water[x][y]=h
    for (ii,jj) in [(0,-1),(0,1),(-1,0),(1,0)]:
        if 0<=x+ii<m and 0<=y+jj<n:
            if water[x+ii][y+jj]<h and H[x+ii][y+jj]<=h:
                dfs(x+ii,y+jj,m,n,h)


def main():
    global H,water
    data=input().split()
    idx=0
    k=int(data[idx])
    idx+=1
    results=[]
    for kk in range(k):
        m, n = map(int, data[idx:idx+2])
        idx+=2
        H = []
        for _ in range(m):
            H.append(list(map(int,data[idx : idx+n])))
            idx+=n
        water = [[-1] * n for _ in range(m)]
        i, j = map(int, data[idx:idx+2])
        idx+=2
        p = int(data[idx])
        idx+=1
        for _ in range(p):
            x, y = map(int,data[idx:idx+2])
            idx+=2
            if H[x-1][y-1]<=H[i-1][j-1]:
                continue
            dfs( x-1, y-1, m, n, H[x-1][y-1])
        results.append("Yes" if water[i-1][j-1]>H[i-1][j-1] else "No")
    sys.stdout.write("\n".join(results)+"\n")

if __name__=="__main__":
    main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241126162638363](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241126162638363.png)



### 02802: 小游戏

bfs, http://cs101.openjudge.cn/practice/02802/

思路：

bfs

思路清晰但是代码有点长

代码：

```python
from collections import deque

def find_locate(x,y):
    ans=[]
    for i in range(x+1,h+2):
        if cards[i][y]==-1:
            break
        ans.append((i,y))
    for i in range(x-1,-1,-1):
        if cards[i][y]==-1:
            break
        ans.append((i,y))
    for j in range(y+1,w+2):
        if cards[x][j]==-1:
            break
        ans.append((x,j))
    for j in range(y-1,-1,-1):
        if cards[x][j]==-1:
            break
        ans.append((x,j))
    return ans

def bfs(start_x,start_y,end_x,end_y):
    q=deque([(0,start_x,start_y)])
    in_queue={(start_x,start_y)}

    while q:
        step,x,y=q.popleft()
        if x==end_x and y==end_y:
            return str(step)+" segments."
        for (i,j) in find_locate(x,y):
            if (i,j) not in in_queue:
                in_queue.add((i,j))
                q.append((step+1,i,j))
    return "impossible."

board=0
while True:
    w,h=map(int,input().split())
    if w==h==0:
        break
    board+=1
    print("Board #%d:"%board)
    cards=[[0]*(w+2) for _ in range(h+2)]
    for i in range(1,h+1):
        s=input()
        for j in range(1,w+1):
            if s[j-1]=="X":
                cards[i][j]=-1
    pair=0
    while True:
        x1,y1,x2,y2=map(int,input().split())
        if x1==x2==y1==y2==0:
            break
        cards[y2][x2]=0
        pair+=1
        print("Pair "+str(pair)+": "+bfs(y1,x1,y2,x2))
        cards[y2][x2]=-1
    print()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241126173401333](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241126173401333.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>



学习了Manacher's Algorithm算法，求最长回文子串；

学习了使用sys一次性读取数据的形式

