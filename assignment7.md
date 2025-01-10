# Assignment #7: Nov Mock Exam立冬

Updated 1646 GMT+8 Nov 7, 2024

2024 fall, Complied by <mark>卢殷文 物院</mark>



**说明：**

1）⽉考： AC5<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E07618: 病人排队

sorttings, http://cs101.openjudge.cn/practice/07618/

思路：



代码：

```python
def cmp(x,y):
    if x[1]>=60 or y[1]>=60:
        if x[1]==y[1]:
            return x[0]<y[0]
        else:
            return x[1]>y[1]
    else:
        return x[0]<y[0]


t=int(input())
pat=[]
for i in range(t):
    id,age=input().split()
    pat.append([i,int(age),id])
for i in range(t-1):
    for j in range(i+1,t):
        if cmp(pat[j],pat[i]):
            pat[i],pat[j]=pat[j],pat[i]
for i in range(t):
    print(pat[i][2])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241107194714397](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241107194714397.png)



### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/practice/23555/

思路：



代码：

```python
n,m1,m2=map(int,input().split())
X=[]
Y=[]
for i in range(m1):
    l=list(map(int,input().split()))
    X.append(l)
for i in range(m2):
    l = list(map(int, input().split()))
    Y.append(l)
ans=[[0]*n for _ in range(n)]
for i in range(m1):
    for j in range(m2):
        if X[i][1]==Y[j][0]:
            ans[X[i][0]][Y[j][1]]+=X[i][2]*Y[j][2]
for i in range(n):
    for j in range(n):
        if ans[i][j]!=0:
            print(i,j,ans[i][j])
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241107195045908](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241107195045908.png)



### M18182: 打怪兽 

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/

思路：

很奇怪考试时调用的cmp_to_key不灵，最后无奈写成lambda函数形式

代码：

```python
nCases=int(input())
for _ in range(nCases):
    n,m,b=map(int,input().split())
    able=[]
    for i in range(n):
        ti,xi=map(int,input().split())
        able.append([ti,xi])
    ables=sorted(able,key=lambda x:(x[0],-x[1]))
    t=0
    now=1
    for i in range(n):
        if ables[i][0]==t:
            now+=1
            if now<=m:
                b-=ables[i][1]
        else:
            t=ables[i][0]
            now=1
            b-=ables[i][1]
        if b<=0:
            print(t)
            break
    else:
        print("alive")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241107195151150](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241107195151150.png)



### M28780: 零钱兑换3

dp, http://cs101.openjudge.cn/practice/28780/

思路：

考虑到考试时时间限制10s以上，不用优化，直接O(m*n) 即可AC

代码：

```python
n,m=map(int,input().split())
coins=list(map(int,input().split()))
flg=[-1]*(10**6+1)
for i in coins:
    flg[i]=1
for i in range(1,m+1):
    if flg[i]==1:
        continue
    ans=10**7
    for j in coins:
        if i<j:
            continue
        if flg[i-j]!=-1 and flg[i-j]<ans:
            ans=flg[i-j]
    if ans!=10**7:
        flg[i]=ans+1
print(flg[m])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241107195331482](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241107195331482.png)



### T12757: 阿尔法星人翻译官

implementation, http://cs101.openjudge.cn/practice/12757

思路：

这题考试的时候觉得太烦，小做一会跳了

回头看其实还行

代码很长，但是思路是清晰的：将英文单词分为“分界符”和“数字符”两种

代码：

```python
num_dict={"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10, "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19, "twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90,"":0}
def num(s:str):
    ans=0
    for i in s.split():
        ans+=num_dict[i]
    return ans

def hud(s:str):
    if "hundred" in s:
        x=s.find("hundred")
        s1=s[:x]
        s2=s[x+7:]
        ans=num(s1)*100+num(s2)
    else:
        ans=num(s)
    return ans


def thu(s: str):
    if "thousand" in s:
        x = s.find("thousand")
        s1 = s[:x]
        s2 = s[x + 8:]
        ans = hud(s1) * 10 ** 3 + hud(s2)
    else:
        ans = hud(s)
    return ans


def mil(s:str):
    if "million" in s:
        x = s.find("million")
        s1 = s[:x]
        s2 = s[x + 7:]
        ans = thu(s1) * 10 ** 6 + thu(s2)
    else:
        ans = thu(s)
    return ans

s=input()
if s[:8]=="negative":
    print(-1*mil(s[9:]))
else:
    print(mil(s))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-07 201850](D:\学习软件\2024秋\计算概论 闫鸿飞\作业7\屏幕截图 2024-11-07 201850.png)



### T16528: 充实的寒假生活

greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/

思路：

反而是整个月考过程中做的最顺的一题

代码：

```python
n=int(input())
act=[]
for i in range(n):
    fro,to=map(int,input().split())
    act.append([fro,to])
act.sort(key=lambda x:x[1])
pre=-1
ans=0
for i in range(n):
    if act[i][0]>pre:
        pre=act[i][1]
        ans+=1
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241107195558405](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241107195558405.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

考试的时候在cmp_to_key函数的失效问题上纠结了很久，最终还是采取最原始的排序表达；结果考试最后看时间剩的不多就放弃外星人这题了，可惜

回自家电脑pycharm上一试又可以了(?) 可能考的时候哪里写错了



