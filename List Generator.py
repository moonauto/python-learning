list (range(1,11)) #生成一个list
[x*x for x in range(1,11)] #一个list
[x*x for x in range(1,11) if x % 2 == 0]  #生成一个list
[m + n for m in 'ABC' for n in 'XYZ'] #两层循环

import os #导入os模块
[d for d in os.listdir('.')]  #os.listdir 可以列出文件及内容


g = (x*x for x in range(10))
if n in g:
    print (g)

