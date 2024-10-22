# Assignment #5: Greedy穷举Implementation

Updated 1939 GMT+8 Oct 21, 2024

2024 fall, Complied by <mark>卢殷文 物院 2400011462</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 04148: 生理周期

brute force, http://cs101.openjudge.cn/practice/04148

思路：



代码：

```python
n=0
while True:
    d,p,e,i=map(int,input().split())
    if d==p==e==i==-1:
        break
    n+=1
    x=i+1
    flg=0
    while x<21252+i:
        if x%33==e%33 and x%23==d%23 and x%28==p%28:
                break
        else:
            x+=1
    print("Case %d: the next triple peak occurs in %d days."%(n,x-i))
```

![image-20241022100828267]([lucasrepository/屏幕截图 2024-10-22 100810.jpg at assignment-5 · lywlucas/lucasrepository (github.com)](https://github.com/lywlucas/lucasrepository/blob/assignment-5/屏幕截图 2024-10-22 100810.jpg))

代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/practice/18211

思路：



代码：

```python
p=int(input())
weapons=sorted(list(map(int,input().split())))
x,y=0,len(weapons)-1
curr,ans=0,0
while x<=y:
    if p>=weapons[x]:
        curr+=1
        if curr>ans:
            ans=curr
        p-=weapons[x]
        x+=1
    elif not curr:
        break
    else:
        curr-=1
        p+=weapons[y]
        y-=1
print(ans)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241022144112070](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241022144112070.png)



### 21554: 排队做实验

greedy, http://cs101.openjudge.cn/practice/21554

思路：



代码：

```python
n=int(input())
t=list(map(int,input().split()))
stu=sorted([ (t[i],i+1) for i in range(n)])
total=0
for j in range(n):
    total+=stu[j][0]*(n-j-1)
    print(stu[j][1],end=" ")
print()
ans=total/n
print("%.2f"%ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241022145058001](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241022145058001.png)



### 01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/

思路：



代码：

```python
Haab = {"pop": 0, "no": 1, "zip": 2, "zotz": 3, "tzec": 4, "xul": 5, "yoxkin": 6, "mol": 7, "chen": 8, "yax": 9, "zac": 10, "ceh": 11, "mac": 12, "kankin": 13, "muan": 14, "pax": 15, "koyab": 16, "cumhu": 17, "uayet": 18}
Tzolkin = {0: "imix", 1: "ik", 2: "akbal", 3: "kan", 4: "chicchan", 5: "cimi", 6: "manik", 7: "lamat", 8: "muluk", 9: "ok", 10: "chuen", 11: "eb", 12: "ben", 13: "ix", 14: "mem", 15: "cib", 16: "caban", 17: "eznab", 18: "canac", 19: "ahau"}
n = int(input())
print(n)
for _ in range(n):
    day, month, year = input().split()
    day = int(day[:-1])
    total = int(year) * 365 + Haab[month] * 20 + day
    print(total % 13 + 1, Tzolkin[total % 20], total // 260)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241022150538959](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241022150538959.png)



### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C

思路：

要想通，从左往右的贪心是合法的；

事实上，如果“反悔”，至多影响一棵树，相当于一换一，总数不会改变。

代码：

```python
n = int(input())
trees = []
for i in range(n):
    xi,hi=map(int,input().split())
    trees.append((xi,hi))
if n==1:
    print(1)
else:
    ans = 2
    curr = trees[0][0]
    for i in range(1, n - 1):
        if trees[i][0] - curr > trees[i][1]:
            ans += 1
            curr = trees[i][0]
        elif trees[i + 1][0] - trees[i][0] > trees[i][1]:
            ans += 1
            curr = trees[i][0] + trees[i][1]
        else:
            curr = trees[i][0]
    print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241022154939476](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241022154939476.png)



### 01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/

思路：

预处理各个小岛，成为可接受的雷达位置范围；

以范围的后界排序，贪心处理

代码：

```python
import math
casenum=0
while True:
    casenum+=1
    n,d=map(int,input().split())
    radars=[]
    if n==d==0:
        break
    flg=False
    for i in range(n):
        x,y=map(int,input().split())
        if y>d:
            flg=True
            continue
        lo=x-math.sqrt(d**2-y**2)
        hi=x+math.sqrt(d**2-y**2)
        radars.append([lo,hi])
    if flg:
        input()
        ans=-1
        print("Case %d: %d" % (casenum, ans))
        continue
    radars.sort(key=lambda x:x[1])
    ans=0
    cur=-math.inf
    for i in range(n):
        if radars[i][0]<=cur:
            continue
        else:
            ans+=1
            cur=radars[i][1]
    print("Case %d: %d"%(casenum,ans))
    input()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241022164133323](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241022164133323.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

学习了几种常见的区间问题；较为熟练地利用间断点debug

感觉面对贪心算法的问题思路更加开阔了



