import array as ary
str="Atharva college"
list1=[1,"Welcome",4.5,(2+3j)]
array1=ary.array("i",[1,2,3,4,5,6])
dic={'Name':"XYZ",'Age':15,'Email': "xyz@gmail.com",'class':'12th'}
set1={"phthon","c++","HTML",".NET"}
tuple1=('A','B','C','D',1,2,3,5)

print("This is %s Datatype" % type(str) , "andd string is", str)
print("This is %s Datatype" % type(list1) , "andd string is", list1)
print("This is %s Datatype" % type(array1) , "andd string is",array1)
print("This is %s Datatype" % type(dic) , "andd string is", dic)
print("This is %s Datatype" % type(set1) , "andd string is", set1)
print("This is %s Datatype" % type(tuple1) , "andd string is",tuple1)

print("\n \n Print all list items using for loop")
for i in list1:
    print(i)


print("\n \n Print all tuple items using a while loop")
i =0
while i < len(tuple1):
    print(tuple1[i])
    i=i+1

print("\n \n Check if C++ is present in the set1 set. ")

if "C++" in set1:
    print("Yes, C++ is present in set1")
else:
    print("No, C++ is not pesent in set1")

print("\n\n Print first 3 Key value pair of Dictionary")
a = list(dic.items())
for i in range(len(a)):
    print(i)
    if i==3:
        break
    else:
        print(a[i])

