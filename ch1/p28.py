#logical operator
m=(2>1) and (4>2)
n=(2>1) and (4<2)
o=(2<1) and (4>2)
p=(2<1) and (4<2)
print(m,n,o,p,sep='\n')

#second example
input1=5
input2=6
input3=12

condition1=input1>input2
condition2=input1>input3

print("input1=",input1)
print("input2=",input2)
print("input3=",input3)

print("condition1=",condition1) #false
print("condition2=",condition2) #false

a=condition1 and condition2
print(a)

a=condition1 or condition2
print(a)

b=not(condition1 and condition2)
print(b)