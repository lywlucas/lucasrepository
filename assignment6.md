# Assignment #6: Recursion and DP

Updated 2201 GMT+8 Oct 29, 2024

2024 fall, Complied by **<u>卢殷文 物院</u>**



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### sy119: 汉诺塔

recursion, https://sunnywhy.com/sfbj/4/3/119  

思路：

一开始想用O(n)的递推+字符替换的，结果TLE后意识到字符替换本身是O(2^n)的，那不如直接递推的时候用O(2^n)，这样时间常数还小一点。

代码：

```python
def hano(n:int,fromh:str,toh:str,byh:str):
    if n==1:
        return fromh+"->"+toh+"\n"
    else:
        return hano(n-1,fromh,byh,toh)+fromh+"->"+toh+"\n"+hano(n-1,byh,toh,fromh)
n=int(input())
print(2**n-1)
print(hano(n,"A","C","B"))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241102104638676](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241102104638676.png)



### sy132: 全排列I

recursion, https://sunnywhy.com/sfbj/4/3/132

思路：

经典dfs

代码：

```python
n=int(input())
flg=[True]*(n+1)
now=[]

def dfs(loca:int,n:int):
    if loca>=n+1:
        print(" ".join(now))
        return
    for i in range(1,n+1):
        if flg[i]:
            now.append(str(i))
            flg[i]=False
            dfs(loca+1,n)
            flg[i]=True
            now.pop()

dfs(1,n)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241102111908724](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241102111908724.png)



### 02945: 拦截导弹 

dp, http://cs101.openjudge.cn/2024fallroutine/02945

思路：

这题等价于求最长单调不减序列LNIS，dp是O(n^2)肯定能AC，不过前段时间在LeetCode看到一个O(nlogn)的算法，觉得挺有意思，这里也就试着写了一下，过了

大致想法就是，将一个数组${ c_1,c_2,\cdots,c_n }$按照以下2条规则分为m堆，使得m最小：

① 如果某一堆中已经含有数$x$，那么不能放入小于等于$x$的其他数。已经在本堆的除外；

② 始终把新的数放在最靠前的符合规则的堆里。如果没有这样的堆，则在最后另起一堆。

这个算法是贪心的。我们可以利用二分查找将时间复杂度优化为O(nlogn)。

显然这样的操作与题目本身看起来并不等价。但是我们可以证明，堆数$m=len(LNIS)$

----------------------------------------------------

***闲得没事干自己推导了一下

证：假设存在LNIS，有：$len(LNIS)=l$
$$
c_1\ge c_2 \ge \cdots \ge c_l
$$
1、证明$m \ge l$

假设我们知道$c_i$被分在了某一堆。考察$c_{i+1}$的位置：

首先，基于规则①，$c_{i+1}$不能和$c_i$在同一堆；

其次，$c_{i+1}$不能在$c_i$的前面的某一堆，否则按规则$c_i$也本可以放在那一堆，违反了规则②。

因此，$c_{i+1}$一定在$c_i$后面的某一堆，那么对所有的$i$累加这个结论得到$m\ge l$

2、证明$m\le l$

只需在每一堆中选取一个数，构造出单调不增序列$c_i$即可。

首先考虑最后一堆中的最大数$c_m$

当它放入最后一堆时，它一定小于等于前面一堆的所有数，自然也就存在第$m-1$堆中的$c_{m-1}$使得$c_{m-1}\le c_m$

同样，当$c_{m-1}$被放入第$m-1$堆时，一定小于等于**当时**前面一堆所有的数（至少有一个），也即可以找到$c_{m-2}$

以此类推，我们找到了长度为$m$的单调不增序列，即$l\ge m$



综上两条，得$m=l$，即得证

-----------------------------------------------------------



代码：

```python
k=int(input())
enemy=list(map(int,input().split()))
tails=[0]*k
size=0
for x in enemy:
    i,j=0,size
    while i!=j:
        m=(i+j)//2
        if tails[m]>=x:
            i=m+1
        else:
            j=m
    tails[i]=x
    size=max(i+1,size)
print(size)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241102114543088](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241102114543088.png)



### 23421: 小偷背包 

dp, http://cs101.openjudge.cn/practice/23421

思路：

简单dfs

（似乎动态数组可以让代码更简洁？）

代码：

```python
n,b=map(int,input().split())
val=list(map(int,input().split()))
wei=list(map(int,input().split()))
flg=[True]*(n)
goods=[]
chance=[]
def dfs(loca:int,bag:int,n:int,b:int):
    if bag>b:
        now=sum(goods)-goods[-1]
        chance.append(now)
        return
    elif loca>n:
        now=sum(goods)
        chance.append(now)
        return
    for i in range(n):
        if flg[i]:
            flg[i]=False
            goods.append(val[i])
            dfs(loca+1,bag+wei[i],n,b)
            flg[i]=True
            goods.pop()
dfs(1,0,n,b)
print(max(chance))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241102123256865](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241102123256865.png)



### 02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/practice/02754

思路：

直接使用之前写过的全排列，枚举审核是否符合题意即可

代码：

```python
n=8
flg=[True]*(n+1)
now=[]
chance=[]
def queen(s:str):
    for i in range(n):
        for j in range(i+1,n):
            if abs(int(s[i])-int(s[j])) == j-i:
                return False
    return True
def dfs(loca:int,n:int):
    if loca>=n+1:
        ans="".join(now)
        if queen(ans):
            chance.append(int(ans))
        return
    for i in range(1,n+1):
        if flg[i]:
            now.append(str(i))
            flg[i]=False
            dfs(loca+1,n)
            flg[i]=True
            now.pop()
dfs(1,n)
chance.sort()
t=int(input())
for i in range(t):
    b=int(input())
    print(chance[b-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241102124600663](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241102124600663.png)



### 189A. Cut Ribbon 

brute force, dp 1300 https://codeforces.com/problemset/problem/189/A

思路：

简单枚举即可

代码：

```python
n,a,b,c=map(int,input().split())
a,b,c=sorted((a,b,c),reverse=True)
x=n//a
y=n//b
num=0
for i in range(x+1):
    for j in range(y+1-a*i//b):
        ans=n-a*i-b*j
        if ans%c==0:
            num=max(i+j+ans//c,num)
print(num)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241102134224866](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241102134224866.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

很多时候想要找到一个省时的算法，结果回过头来发现还不如直接暴力枚举。以后做题时不妨先估算以下暴力穷举/dp是否已经符合时间要求。



