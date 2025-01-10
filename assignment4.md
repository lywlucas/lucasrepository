# Assignment #4: T-primes + 贪心

Updated 0337 GMT+8 Oct 15, 2024

2024 fall, Complied by  卢殷文  物理学院  2400011462



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 34B. Sale

greedy, sorting, 900, https://codeforces.com/problemset/problem/34/B



思路：



代码

```python
n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
ans=0
for i in range(m):
    if l[i]>=0:
        break
    else:
        ans-=l[i]
print(ans)

```



代码运行截图 ==（至少包含有"Accepted"）==



![屏幕截图 2024-10-15 080349](D:\学习软件\2024秋\计算概论 闫鸿飞\作业4\屏幕截图 2024-10-15 080349.jpg)

### 160A. Twins

greedy, sortings, 900, https://codeforces.com/problemset/problem/160/A

思路：



代码

```python
n=int(input())
l=list(map(int,input().split()))
l.sort()
l.reverse()
flg=sum(l)/2
val=0
for i in range(n):
    val+=l[i]
    if val>flg:
        print(i+1)
        break

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241015080615997](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241015080615997.png)



### 1879B. Chips on the Board

constructive algorithms, greedy, 900, https://codeforces.com/problemset/problem/1879/B

思路：



代码

```python
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    ans1=sum(a)+n*min(b)
    ans2=n*min(a)+sum(b)
    ans=min(ans1,ans2)
    print(ans)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==



![image-20241015080740309](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241015080740309.png)

### 158B. Taxi

*special problem, greedy, implementation, 1100, https://codeforces.com/problemset/problem/158/B

思路：



代码

```python
n=int(input())
num=[0]*5
ss=list(map(int,input().split()))
for i in range(n):
    num[ss[i]]+=1
ans=num[4]+num[3]+num[2]//2
num[2]-=num[2]//2*2
num[1]-=num[3]+2*num[2]
if num[2]>0:
    ans+=1
if num[1]>0:
    ans+=num[1]//4
    num[1]-=num[1]//4*4
    if num[1]>0:
        ans+=1
print(ans)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241015082710699](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241015082710699.png)



### *230B. T-primes（选做）

binary search, implementation, math, number theory, 1300, http://codeforces.com/problemset/problem/230/B

思路：

（挺有意思的）

题目等价于：判断一个数 ( <1E12) 是否是质数的平方

计划在1E6范围内欧拉筛，再判断题目给出数的平方根是否在质数表里

又加了一点小优化，省了若干常数才过

代码

```python
from math import sqrt
n=1000000
a=[False]*(n+1)
prime=[]
def Euler(n):
    global cnt
    cnt=0
    for i in range(2,n+1):
        if not a[i]:
            cnt+=1
            prime.append(i)
        for j in range(cnt):
            flg=i*prime[j]
            if flg>n:
                break
            else:
                a[flg]=True
                if i%prime[j]==0:
                    break
    return
def isintp(n):
    if n>endd or n<=1:
        return False
    bg,ed=0,cnt
    ni=sqrt(n)
    if ni!=int(ni):
        return False
    n=int(ni)
    if not a[n]:
        return True
    else:
        return False
Euler(n)
global endd
endd=prime[-1]**2
t=int(input())
l=list(map(int,input().split()))
for i in range(t):
    if isintp(l[i]):
        print("YES")
    else:
        print("NO")

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241015083329300](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241015083329300.png)



### *12559: 最大最小整数 （选做）

greedy, strings, sortings, http://cs101.openjudge.cn/practice/12559

思路：

做的时候小卡了一下，因为不会用key表述排序方式

后来搜了一下有个 "cmp_to_key" 函数，也就顺利AC了

代码

```python
import functools
def cmp(x,y):
    xx,yy=int(x+y),int(y+x)
    return xx-yy
n=int(input())
num=list(map(str,input().split()))
nums=sorted(num,key= functools.cmp_to_key(cmp))
big=""
sma=""
for i in range(n):
    big=nums[i]+big
    sma=sma+nums[i]
print(big,sma)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==



![image-20241015094355550](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241015094355550.png)

## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

学会了调用cmp_to_key；初步接触了算法常系数的优化





