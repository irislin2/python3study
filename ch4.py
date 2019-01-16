"""
1.1 分別寫出四個function可以印出字元'K', 'D', 'A', 'Y', 請使用迴圈寫, 不是直接把答案印出
*       *
*     *
*   *
* * *
*     *
*       *
*        *

1.2 多加一個function可以印出一棵聖誕樹, 使用上面的 function 印出 KKDAY 跟聖誕樹
           *
           |
          ***
           |
         *****
           |
        *******
           |
       *********
           |
      ***********
           |
     *************
           |
    ***************
           |
   *****************
           |
  *******************
           |
 *********************
           |
1.3 印個花樣多一點的聖誕樹
          []
         [~~]
        [~~~~]
       [~~~~~~]
      [~~~~~~~~]
     [~~~~~~~~~~]
    [~~~~~~~~~~~~]
   [~~~~~~~~~~~~~~]
  [~~~~~~~~~~~~~~~~]
 [__________________]
          []
          []
"""

#1.1
def printStar(a):
 s=a
 print("\n")
 for i in s:
  for i2 in range(1,10):
   if i2 in i:
    print('*',end='')
   else:
    print(' ',end='')
  print("")

def printK():
 s=[[1,9],[1,7],[1,5],[1,3,5],[1,5],[1,7],[1,9]]
 printStar(s)

def printD():
 s=[[1,3,5],[1,7],[1,9],[1,9],[1,9],[1,7],[1,3,5]]
 printStar(s)

def printA():
 s=[[5],[4,6],[3,7],[2,8],[1,3,5,7,9],[1,9],[1,9]]
 printStar(s)

def printY():
 s=[[1,9],[2,8],[3,7],[4,6],[5],[5],[5]]
 printStar(s)

printK()
printK()
printD()
printA()
printY()

#1.2
def printTree1():
 star_list=[number for number in range(1,22) if number %2== 1]
 for i in range(1,23):
  if i % 2 ==1:
   print(str('*' * i).center(30,' '))
  else:
   print(str('|').center(30,' '))

printTree1()
print('\n')

#1.3
def printTree2():
 #star_list = [number for number in range(0,10) if number % 2==0]
 for i in range(0,13):
  if i <10:
   print(str('['+'~'*i*2+']').center(30,' '))
  elif i == 10:
   print(str('['+'_'*i*2+']').center(30,' '))
  else:
   print(str('[]').center(30,' '))

printTree2()
print('\n')

"""
2. 使用迴圈找出 300 以下的質數
"""
#2
for i in range(2,300):
 for j in range(2,i):
  if i%j ==0:
   break
 else:
  print(i,end=',')

print(' ')

"""
3. 費氏數列, f(0)=0, f(1)=1, f(n)=f(n-1)+f(n-2)
列出f(20)的完整費氏數列
0 1 1 2 .... f(20)
"""
#3

a3=list()
a3=[0,1]
for i in range(2, 20):
  a3.append(a3[i-1]+a3[i-2])

print('\n'+str(a3))
print('\n')

"""
4. 四位數中，使用迴圈找出 0 ~ 7 所能組成的奇數個數
"""
#4
num_a=[1,3,5,7]
odd_list=list()

for d in range(0,8):
 for c in range(0,8):
  for b in range(0,8):
   for a in num_a:
    odd7777=int(str(d)+str(c)+str(b)+str(a))
    odd_list.append(odd7777)

print(len(set(odd_list)))
