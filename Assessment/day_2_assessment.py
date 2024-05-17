# str1 = "PyThOnIndIA"

# lower=[]
# upper=[]
# exceptionChar=[]

# for char in str1:
#     if char.islower():
#         lower.append(char)
#     elif char.isupper():
#         upper.append(char)
#     else:
#         exceptionChar.append(char)

# print(''.join(lower + upper + exceptionChar))



###### 2 #######
# testtext="1. checking the number of different char in string.####!!!!"

# digit=[]
# aplpha=[]
# exceptionChar=[]

# for char in testtext:
#     if char.isdigit():
#         digit.append(char)
#     elif char.isalpha():
#         aplpha.append(char)
#     else:
#         exceptionChar.append(char)

# print("".join("Digits : " + str(len(digit)) + " "))
# # print(digit)
# print("".join("Alpha : " + str(len(aplpha)) + " "))
# # print(aplpha)
# print("".join("Special : " + str(len(exceptionChar)) + " "))
# # print(exceptionChar)



###### 3 #######

# strarr=["Ram", "Shyam", "Tulsi", "", "RAghavendra", "Kishore ", ]

# for i in range(len(strarr)-1, 0, -1):
#     print("index", i)
#     if len(strarr[i].strip()) != 0:
#         strarr[i] = strarr[i].strip()
#         print(strarr[i])
#     else:
#         del strarr[i]
#         print("index", i)
#     print(strarr)
#     i=-1
#     print("index", i)
# print("Final", strarr)


###### 4 ######

# First and last number are same?

# num1=[10,20,30,45,29,10]
# num2=[14,18,19,20,23,6,30]
# def checkSame1stlast(num):
#     if num[0] == num[len(num)-1]:
#         print("same") 
#     else:
#         print("Not same")
    
# checkSame1stlast(num1)
# checkSame1stlast(num2)


###### 5 ######

# list=[10,20,30,23,45]
# divisible=[]
# for i in list:
#     if i%5 == 0:
#         divisible.append(i)

# print(divisible)

###### 6 ######

# subsctring count

# str="""india is my country all indian are my brothers and sisters
# except one who's my spuoce, hahaha
# It a pleasure to learn python from scratch
# I've 10years of experience in programming with multiple languages and frameworks
# """

# count=0
# start=0
# substr="indian"

# while True:
#     i = str.find(substr, start)
#     if i == -1:
#         break
#     count +=1
#     start = i + len(substr)

# print(count)


###### 7 ######

# strtext=124121
# print((str(strtext)) == (str(strtext))[::-1])


##### 8 ######

digit1 = 7947129
txt=(str(digit1)[::-1])
# print(int(txt))
for char in txt: print(int(char))
# print(txt)
