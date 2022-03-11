#bitwise opertors
a=7        # 0 1 1 1
b=6        # 0 1 1 0
r=a&b      # 0 1 1 0
print(r)   # 8*0+ 4*1+ 2*1+0*1 =6
r=a|b
print(r)
r=a^b
print(r)

print(~a)   #7 converting into binary  0 1 1 1  for not we have to add 1 and -the whole
#    -(0 1 1 1
#           +1)
#    -(1 0 0 0)
#    -8 (decimal)

a=7
print(a<<1)    #7
print(a<<2)    #14
print(a<<3)    #28    # value double hojata hai
print(a<<4)

a=28
print(a>>1)    #14
print(a>>2)    #7
print(a>>3)    #3    # value divides  hojata hai
print(a>>4)  #1

