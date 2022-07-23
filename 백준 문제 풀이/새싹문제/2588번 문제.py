#세자릿수 곱셈
a=input()
b=input()
c=list(a)
d=list(b)

e=int(a)*int(d[2])
f=int(a)*int(d[1])
g=int(a)*int(d[0])
print(e,f,g,e+f*10+g*100,sep='\n')