 #1
 for i in range (10):
    print("Hello, World")
#2
Indentaion error
#3
 python3 userargument.py
python userargument.py
#4
k="""Hi, Alice, Bob, Carol"""
x=k.split("\n")
x=k["".join(i.split()[::-1])for i in x]
k="\n".join(x)
print(k)