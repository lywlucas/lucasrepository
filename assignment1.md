# Assignment #1: 自主学习

Updated 0110 GMT+8 Sep 10, 2024

2024 fall, Complied by 卢殷文 物院



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 02733: 判断闰年

http://cs101.openjudge.cn/practice/02733/



思路：



##### 代码

```python

a=int(input())
if a%4!=0:
    print("N")
else:
    if a%100!=0:
        print("Y")
    else:
        if a%400==0:
            print("Y")
        else:
            print("N")
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240910163310919](https://raw.githubusercontent.com/lywlucas/img/main/img/image-20240910163310919.png)



### 02750: 鸡兔同笼

http://cs101.openjudge.cn/practice/02750/



思路：



##### 代码

```python

a=int(input())
mi=a//4+(a%4)//2
max=a//2
if a%2==1:
    print("0 0")
else:
    print(mi,max)

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240910163923448](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20240910163923448.png)



### 50A. Domino piling

greedy, math, 800, http://codeforces.com/problemset/problem/50/A



思路：



##### 代码

```python
m,n = map(int,input().split())
a = m*n//2
print(a)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240910164059216](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20240910164059216.png)



### 1A. Theatre Square

math, 1000, https://codeforces.com/problemset/problem/1/A



思路：



##### 代码

```python
def guass(x,y):
    if x%y==0:
        return x//y
    else:
        return x//y+1
n,m,a=map(int,input().split())
ans=guass(n,a)*guass(m,a)
print(ans)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240910164151792](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20240910164151792.png)



### 112A. Petya and Strings

implementation, strings, 1000, http://codeforces.com/problemset/problem/112/A



思路：



##### 代码

```python
s1=input().casefold()
s2=input().casefold()
if s1<s2:
    print("-1")
elif s1>s2:
    print("1")
else:
    print("0")

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240910164240416](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20240910164240416.png)



### 231A. Team

bruteforce, greedy, 800, http://codeforces.com/problemset/problem/231/A



思路：



##### 代码

```python
n = int(input())
num = 0
for i in range(n):
    a,b,c = map(int, input().split())
    if a + b + c >= 2:
        num += 1
print(num) 

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240910164528258](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20240910164528258.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

复习了形如casefold() 等的py内置函数

总的来说题目还是较简单的

额外联系：每日选做、CF的若干C级题

Ψ(￣∀￣)Ψ

