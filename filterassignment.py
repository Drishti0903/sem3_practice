
#1
list1=[1,0,-1,-2,-3]
negative_no=list(filter(lambda x:x<0,list1))
print(negative_no)

#2
number=[1,2,3,4,5,6,7,8,9,11,12,13,14]
odd_no=list(filter(lambda x:x%2!=0,number))
print(odd_no)

#3
str="my name is drishti jain from software development"
str1=list(filter(lambda x:True if x.lower()in "aeiou" else False,str))
print(str1)

#4
str2="i was born in 2003 and my age presently is 19 years"
str3=list(filter(lambda x:True if x in "0123456789" else False,str2))
print(str3)

#5
list2=[10,-10,-20,-30,-40,-50,-60,100]
list3=list(filter(lambda x:True if x>0 else False,map(lambda x:x*-1,list2)))
print(list3)