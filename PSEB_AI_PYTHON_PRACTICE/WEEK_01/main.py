# 1 [Beginner] Personal Introduction Card

# Ask the user for their name, age, city, and favorite programming language. Display the 
# information as a neat personal introduction card, with each detail on a separate line. Use 
# meaningful variable names and clear output labels.

# name=input("enter your name");
# age_text=input("enter your age")
# age=int(age_text);
# course=input("enter your course");
# # print("my name is "+name+" and my age is "+ age +" currently I am doing "+ course);
# print("my name is",name);
# print("my age is", age);
# print("my course is", course);

# 2 [Beginner] Simple Calculator

# Ask the user to enter two numbers. Calculate and display their addition, subtraction, 
# multiplication, and division. Before dividing, check whether the second number is zero and 
# display a suitable message instead of attempting an invalid division.

# num1= int(input("enter num1 "));
# num2= int(input("enter num2 "));
# print(num1+num2);
# print(num1-num2);
# print(num1*num2);

# if num2 == 0:
#     print("wrong no")
# else:
#     print(num1 / num2);


# 3
# num1= int(input("enter num1 : "));
# if num1%2 ==0:
#     print("even");
# else: 
#     print("odd");


# # 4
# total_marks=500;
# num1= int(input("enter num1 :"));
# num2= int(input("enter num2 :"));
# num3= int(input("enter num3 :"));
# num4= int(input("enter num4 :"));
# num5= int(input("enter num5 :"));

# obtain_marks=(num1+num2+num3+num4+num5);

# percentage=((obtain_marks/total_marks)*100);

# if percentage >=80:
#     print(percentage)
#     print("A")
# elif percentage >=70:
#     print(percentage)
#     print("B")
# elif percentage >=60:
#     print(percentage)
#     print("C")
# elif percentage >=50:
#     print(percentage)
#     print("D")
# else:
#     print(percentage)
#     print("Fail")




#5
# num= int(input("enter num "));
# for i in range(1,11):
#     print(num," x ",i," = ",num*i )

# 6
# num  = 36
# attempts= 0;


# while(True):
#     Usernum= int(input("enter the number : "))
#     attempts += 1;

#     if Usernum == num:
#         print("correct answer the number is :",num)
#         print(attempts);
#         break;
#     elif Usernum>num:
#         print("enter smaller numver")
#     else:
#         print("enter bigger number")


# 7
# sentence = input("enter sentence :").lower()
# vovels=0
# consonants=0
# variable="aeiou"
# for character in sentence:
#     if(character in variable):
#         vovels +=1;
#     elif character.isalpha():
#         consonants +=1;
# print("there are ",vovels," vovels");
# print("there are ",consonants," consonants");

# 8
# number=[];
# for addnumber in range(5):
#     number.append(int(input("enter the number : ")))
# print(number)
# largest=number[0]
# smallest=number[0]
# for element in number:
#     if element > largest:
#         largest = element
#     if element < smallest:
#         smallest = element
# print(largest);
# print(smallest);

# 9
# paragraph=input("enter the para : ").lower()
# words=paragraph.split();
# words_count=len(words);
# print("total words in para are : ",words_count);
# characters_count = 0;
# vovels=0
# consonants=0
# variable="aeiou"
# for characters in paragraph:
#     if(characters != " "):
#         characters_count += 1;
#     if(characters in variable):
#         vovels +=1;
#     elif characters.isalpha():
#         consonants +=1;
# print("total characters in papare : ",characters_count);
# print("there are ",vovels," vovels");
# print("there are ",consonants," consonants"); 

# 10
# num=[]
# count=int(input("enter how many times to run loop : "))
# for i in range(count):
#     num.append(int(input("enter the number : ")))
# print(num);
# newlist=[]
# for i in num:
#     if i not in newlist:
#         newlist.append(i);
# print(newlist);

# 11
# num=input("enter number list : ").split()
# numbers=[];
# for i in num:
#     numbers.append(int(i));
# print(numbers);
# newlist=[]
# for i in numbers:
#     if i not in newlist:
#         newlist.append(i);
# print(newlist);
# if len(newlist) >= 2:
#     print("two distinct numbers avaible")

#     largest=newlist[0];
#     for element in newlist:
#         if element>largest:
#             largest=element;
#     print(largest);#if you want to check largest number
    
#     # method 1
# #     remaining=[];
# #     for i in newlist:
# #         if i != largest:
# #             remaining.append(i);
# #     print(remaining);
# #     second_largest=remaining[0];
# #     for element in remaining:
# #         if element>second_largest:
# #             second_largest=element;
# #     print(second_largest);


#     # method 2
#     newlist.remove(largest);
#     second_largest=newlist[0];
#     for element in newlist:
#         if element>second_largest:
#             second_largest=element;
#     print(second_largest);
# else:
#     print("At least two distinct numbers are required");