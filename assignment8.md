# Assignment #8: 田忌赛马来了

Updated 1021 GMT+8 Nov 12, 2024

2024 fall, Complied by <mark>卢殷文 物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/practice/12558/ 

思路：

直接使用海岸线定义做

代码：

```python
n,m=map(int,input().split())
isle=[[0]*(m+2)]
for i in range(n):
    l_m=list(map(int,input().split()))
    isle.append([0]+l_m+[0])
isle.append([0]*(m+2))
ans=0
for i in range(n+1):
    for j in range(m+1):
        if isle[i][j]!=isle[i+1][j]:
            ans+=1
        if isle[i][j]!=isle[i][j+1]:
            ans+=1
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241113181752211](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241113181752211.png)



### LeetCode54.螺旋矩阵

matrice, https://leetcode.cn/problems/spiral-matrix/

与OJ这个题目一样的 18106: 螺旋矩阵，http://cs101.openjudge.cn/practice/18106

思路：

这个是我的暴力思路，绕一圈递归n-2

题解的取模转向还是很漂亮的

代码：

```python
def cir(n,x):
    if n==1:
        return [[x]]
    elif n==2:
        return [[x,x+1],[x+3,x+2]]
    else:
        flg=x+4*n-5
        li=cir(n-2,flg+1)
        for i in range(len(li)):
            li[i]=[flg-i]+li[i]+[x+n+i]
        return [[i for i in range(x,n+x)]]+li+[[i for i in range(flg-n+2,flg-2*n+2,-1)]]

n=int(input())
l=cir(n,1)
for i in l:
    print(*i)
```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-11-14 155524](D:\学习软件\2024秋\计算概论 闫鸿飞\作业8\屏幕截图 2024-11-14 155524.png)



### 04133:垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/

思路：



代码：

```python
N=1025
garb=[[0]*N for _ in range(N)]
d=int(input())
n=int(input())
for _ in range(n):
    x,y,i=map(int,input().split())
    for xi in range(max(0,x-d),min(N,x+d+1)):
        for yi in range(max(0,y-d),min(N,y+d+1)):
            garb[xi][yi]+=i
maxg=0
maxnum=1
for i in range(N):
    for j in range(N):
        if garb[i][j]>maxg:
            maxg=garb[i][j]
            maxnum=1
        elif garb[i][j]==maxg:
            maxnum+=1
print(maxnum,maxg)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241114161004613](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241114161004613.png)



### LeetCode376.摆动序列

greedy, dp, https://leetcode.cn/problems/wiggle-subsequence/

与OJ这个题目一样的，26976:摆动序列, http://cs101.openjudge.cn/routine/26976/

思路：

简单greedy

代码：

```python
n=int(input())
l=list(map(int,input().split()))
if n==1:
    print(n)
else:
    cnt,pre=0,0
    for i in range(n - 1):
        now = l[i] - l[i + 1]
        if pre==0 and now!=0:
            pre=now
            cnt+=1
        elif now * pre < 0:
            cnt += 1
            pre = now
    print(cnt+1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241114163226768](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241114163226768.png)



### CF455A: Boredom

dp, 1500, https://codeforces.com/contest/455/problem/A

思路：

简单dp

代码：

```python
N=10**5+1
nums=[0]*N
score=[0]*N
n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    nums[l[i]]+=1
lmax=max(l)
score[1]=nums[1]
for i in range(2,lmax+1):
    score[i]=max(score[i-1],score[i-2]+i*nums[i])
print(score[lmax])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241114163327764](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241114163327764.png)

### 02287: Tian Ji -- The Horse Racing

greedy, dfs http://cs101.openjudge.cn/practice/02287

思路：

一开始想建个优先队列，然后按警察抓小偷的方案做；然后发现对“平局”的分类讨论无法描述

于是遇事不决试试dp，结果居然以27s的成绩过了（

看了眼题解greedy的双指针，确实挺妙的

代码：

```python
while True:
    n = int(input())
    if n == 0:
        break
    Tian = list(map(int, input().split()))
    King = list(map(int, input().split()))
    Tian.sort(reverse=True)
    King.sort(reverse=True)
    money = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if Tian[i-1] > King[j-1]:
                money[i][j] = max(money[i-1][j], money[i][j-1], money[i-1][j-1] + 2)
            elif Tian[i-1] < King[j-1]:
                money[i][j]=max(money[i-1][j], money[i][j-1], money[i-1][j-1])
            else:
                money[i][j]=max(money[i-1][j],money[i][j-1],money[i-1][j-1] + 1)
    print(200*(money[n][n]-n))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241114175323527](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241114175323527.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

这次作业耗时3小时AC

熟练地运用dp的暴力美学（bushi）

回头看了螺旋矩阵和田忌赛马的题解，还是有不少收获的



