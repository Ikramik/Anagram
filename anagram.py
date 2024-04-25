x= input ("your 1st word is ")
y= input ("your 2nd word is ")
x=list (str(x))
y=list (str(y))
a=len(x)
b=len(y)
d= True
if a!=b :
    d=False
else:
    for i in range (0,a):
        e=False
        for j in range(0,b):
            if x[i]==y[j]:
                y.remove(y[j])
                b=b-1
                e=True
                break
        if e==False :
            d=False
            break
if d== True:
    print("anagram")
else:
    print("not anagram")
