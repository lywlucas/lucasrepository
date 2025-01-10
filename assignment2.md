# Assignment #2: 语法练习

Updated 0126 GMT+8 Sep 24, 2024

2024 fall, Complied by ==同学的姓名、院系==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 263A. Beautiful Matrix

https://codeforces.com/problemset/problem/263/A



思路：



##### 代码

```python
def jdz(x,y):
    if x>=y:
        return x-y
    else:
        return y-x
s=[]
ans=0
for i in range(5):
    s.append(list(input().split()))
    for j in range(5):
        if s[i][j]=='1':
            ans=jdz(i,2)+jdz(j,2)
            break
print(ans)

```



代码运行截图 ==（至少包含有"Accepted"）==

![{AB106626-105C-47DF-A455-A05AE0EEB9EF}](C:\Users\ThinkPad\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\TempState\ScreenClip\{AB106626-105C-47DF-A455-A05AE0EEB9EF}.png)



### 1328A. Divisibility Problem

https://codeforces.com/problemset/problem/1328/A



思路：



##### 代码

```python
def divy(x,y):
    if x%y==0:
        return 0
    else:
        return y-x%y
 
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print(divy(a,b))

```



代码运行截图 ==（至少包含有"Accepted"）==

![{7E44BD89-D7DB-4183-B4CA-C43B429DAAC6}](C:\Users\ThinkPad\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\TempState\ScreenClip\{7E44BD89-D7DB-4183-B4CA-C43B429DAAC6}.png)



### 427A. Police Recruits

https://codeforces.com/problemset/problem/427/A



思路：



##### 代码

```python
n=int(input())
lst=list(map(int,input().split()))
rec=0
untr=0
for i in range(n):
    flg=lst[i]
    if flg==-1:
        if rec>0:
            rec-=1
        else:
            untr+=1
    else:
        rec+=flg
print(untr)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![{F8DC7DBD-51B2-4312-8E1D-0B6853C2C47B}](C:\Users\ThinkPad\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\TempState\ScreenClip\{F8DC7DBD-51B2-4312-8E1D-0B6853C2C47B}.png)



### 02808: 校门外的树

http://cs101.openjudge.cn/practice/02808/



思路：



##### 代码

```python
l,m=map(int,input().split())
subw=[]
for i in range(m):
    a,b=map(int,input().split())
    subw.append([a,1])
    subw.append([b+1,-1])
sub=sorted(subw)
num=l+1
flg=0
fro=-1
for i in range(len(sub)):
    r=sub[i][1]
    flg+=r
    if r==-1 and flg==0:
        num-=sub[i][0]-fro
    elif r==1 and flg==1:
        fro=sub[i][0]
print(num)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![{BF6AD276-C59C-48DD-B49F-D27AD88F6DA0}](C:\Users\ThinkPad\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\TempState\ScreenClip\{BF6AD276-C59C-48DD-B49F-D27AD88F6DA0}.png)



### sy60: 水仙花数II

https://sunnywhy.com/sfbj/3/1/60



思路：



##### 代码

```python
def isflow(n):
    a=n//100
    b=n%100//10
    c=n%10
    ans=a**3+b**3+c**3
    return ans==n
a,b=map(int,input().split())
flg=0
for i in range(a,b+1):
    if isflow(i):
        if flg==0:
            print(i,end="")
        else:
            print(" %d"%i,end="")
        flg=1
if flg==0:
    print("NO",end="")
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240924083310132](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20240924083310132.png)



### 01922: Ride to School

http://cs101.openjudge.cn/practice/01922/



思路：



##### 代码

```python
INF=1E6
def rtime(v,t):
    if t<0:
        return INF
    else:
        ans=4.5*3600/v+t
    if int(ans)==ans:
        return int(ans)
    else:
        return int(ans)+1
while True:
    n=int(input())
    if n==0:
        break
    else:
        mint=INF
    for i in range(n):
        a,b=map(int,input().split())
        ans=rtime(a,b)
        if ans<mint:
            mint=ans
    print(mint)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![{755813A4-9E1B-4C25-BA1D-B5840A069617}](C:\Users\ThinkPad\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\TempState\ScreenClip\{755813A4-9E1B-4C25-BA1D-B5840A069617}.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==



挑选了CF若干C、D的题目



