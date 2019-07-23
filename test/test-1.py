# -*- coding: UTF-8 -*- 
import time
tm1 = time.localtime(time.time())
tm2 = time.time()
systime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))  
print (tm1)
print (tm2)
print (systime+'\nGood Luck! lujs')

#"\n\n"在结果输出前会输出两个新的空行。一旦用户按下键时，程序将退出。 raw_input 函数需要加装
#raw_input("\n\nPress the enter key to exit.")

#同一行显示多条语句
#import sys; x = 'w3cschool'; sys.stdout.write(x + '\n')



