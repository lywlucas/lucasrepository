# Assign #3: Oct Mock Exam暨选做题目满百

Updated 1537 GMT+8 Oct 10, 2024

2024 fall, Complied by 卢殷文 物理学院 2400011462



**说明：**

1）Oct⽉考： AC6==（请改为同学的通过数）== 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/practice/28674/



思路：

AC

5-10min



代码

```python
k=int(input())
k=k%26
s=input()
ans=""
for i in range(len(s)):
    a=s[i]
    asc = ord(s[i])
    if 'a'<=a<='z':
        asc-=k
        if asc>=ord('a'):
            ans+=chr(asc)
        else:
            ans+=chr(asc+26)
    else:
        asc-=k
        if asc>=ord('A'):
            ans+=chr(asc)
        else:
            ans+=chr(asc+26)
print(ans)

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241011114829755](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241011114829755.png)



### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/practice/28691/



思路：

AC

2min

代码

```python
a,b=input().split()
x=int(a[0:2])
y=int(b[0:2])
print(x+y)

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241011115026510](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241011115026510.png)



### M28664: 验证身份证号

http://cs101.openjudge.cn/practice/28664/



思路：

AC

5-10min

代码

```python

timeslist=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
testlist=[1,0,"X",9,8,7,6,5,4,3,2]
n=int(input())
for i in range(n):
    id=input()
    test=0
    for j in range(17):
        x=int(id[j])
        test+=x*timeslist[j]
    test=test%11
    if id[-1]==str(testlist[test]):
        print("YES")
    else:
        print("NO")
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241011115143038](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241011115143038.png)



### M28678: 角谷猜想

http://cs101.openjudge.cn/practice/28678/



思路：

AC

10min

（调格式化输出%d花了一段时间……）

代码

```python
def jiaogu(n):
    if n==1:
        print("End")
        return
    elif n%2==1:
        next=3*n+1
        print("%d*3+1=%d"%(n,next))
    else:
        next=n//2
        print("%d/2=%d"%(n,next))
    return jiaogu(next)
n=int(input())
jiaogu(n)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241011115410345](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241011115410345.png)



### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/practice/28700/



思路：

AC

10-15min

先写了个10进制转罗马数字的程序

反过来懒得写了，数据样本量不大，直接打表

##### 代码

```python
ones=["I","X","C","M"]
fives=["V","L","D",""]
romans=[""]*4000
for n in range(1,4000):
    a=n//1000
    b=n%1000//100
    c=n%100//10
    d=n%10
    num=[d,c,b,a]
    ans=""
    for i in range(3,-1,-1):
        if num[i]==9:
            ans+=ones[i]+ones[i+1]
        elif num[i]==4:
            ans+=ones[i]+fives[i]
        elif num[i]>=5:
            ans+=fives[i]+(num[i]-5)*ones[i]
        else:
            ans+=num[i]*ones[i]
    romans[n]=ans

s = input()
if '0'<=s[0]<='9':
    print(romans[int(s)])
else:
    for i in range(1,4000):
        if romans[i]==s:
            print(i)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241011115631645](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241011115631645.png)



### *T25353: 排队 （选做）

http://cs101.openjudge.cn/practice/25353/



思路：

题目等价于：间隔大于d的两个数的相对位置不会改变。

所以如果要判断一个数能否到达队首，只需看它前面的所有数是否与之相差d以内

-------------------------------------------------------------------------------------------------------------------------

考试的时候花了将近1h结果还是WA

当时的思路是，分组排序，确保每一组内的数两两之差不超过d；

每次读入的数如果不能进上一组，就新开一组；

最后组内排序后，再优化，后面组内的数如果较小且可以滑到前一组，则进上并重新排序。

写下来O(n^2)，样例过了，但是WA；

现在想应该是上滑的“较小”判定写的不好

-------------------------------------------------------------------------------------------

现在想其实如果都是最差O(n^2)，没必要在整个表里搞分组优化。

不如直接遍历一轮，把所有可能来到队首的筛出来，作为“第一组”，剩下的再重新循环即可。

调用deque队列来维护，这样使用popleft时不至于太慢

判定时采取动态min，max

代码

```python

from collections import deque
n,d=map(int,input().split())
h=deque(int(input()) for i in range(n))
ans=[]
while h:
    part=[]
    maxh=h[0]
    minh=h[0]
    for i in range(len(h)):
        hi=h.popleft()
        if maxh-d<=hi<=minh+d:
            part.append(hi)
        else:
            h.append(hi)
        if hi<minh:
            minh=hi
        if hi>maxh:
            maxh=hi
    ans += sorted(part)

print(*ans, sep='\n')

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241011120921834](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20241011120921834.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

排队题还是挺有意思的；不过放在考试里对我来说有点难了。



每日选做跟着，把较难一点的题做了

