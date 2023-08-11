import os
os.system("clear")
print("DHX")
print ("""
 ____  _   ___  __
|  _ \| | | \ \/ /
| | | | |_| |\  /\n| |_| |  _  |/  \\
|____/|_| |_/_/\_\\


"""
)
print ("________________________")
print ("the best tool fur install library python end tools end pkg")
print ("____&&&&__$_____________")

print ("[ 1 ] install librarys")
print ("")
print ("[ 2 ] install tools end pkg")
print ("")
print ("[ 00 ] exit")


while True :

    y = input(">>")
    if y == "2" :
        os.system("clear")
        print ("[ 00 ] exit")
        u = input ("what,s the name tool >>")
        if u == "00":

            os.system("clear")
            os.system("exit")
            os.system("python tooolxx.py")    
        os.system("pkg install " + u)

    if y == "1":
        os.system("clear")
        print ("[ 00 ] exit")
        r = input ("what,s yr name library >> ")
        if r == "00":
            os.system("exit")
            os.system("python tooolxx.py")
        os.system("pip install "+ r)
    if y == "00":
        break
        os.system("exit")
