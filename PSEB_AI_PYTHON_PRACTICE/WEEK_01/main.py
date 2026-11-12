import string

# 1. [Beginner] Personal Introduction Card

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

# 2. [Beginner] Simple Calculator

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


# 3. [Beginner] Even or Odd Number Checker

# Ask the user to enter an integer. Use a conditional statement and the modulus operator (%) to determine whether the number is even or 
# odd. Display the number along with the result.

# num1= int(input("enter num1 : "));
# if num1%2 ==0:
#     print("even");
# else: 
#     print("odd");


# 4. [Beginner] Student Marks and Grade Calculator

# Ask the user to enter marks for five subjects. Calculate the total marks and percentage, assuming each subject is out of 100. Use 
# if-elif-else conditions to assign a grade: A for 80% or above, B for 70–79%, C for 60–69%, D for 50–59%, and F below 50%. Display the 
# total, percentage, and grade.

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




# 5. [Beginner] Multiplication Table Generator

# Ask the user to enter a number and generate its multiplication table from 1 to 10 using a loop. Display each calculation in a 
# readable format, such as 5 x 1 = 5.

# num= int(input("enter num "));
# for i in range(1,11):
#     print(num," x ",i," = ",num*i )

# 6. [Beginner] Guess the Secret Number

# Create a simple number-guessing game. Store a secret number in your program and repeatedly ask the user to guess it. If the guess is 
#  too high or too low, give a helpful hint. Continue until the user guesses correctly, then display how many attempts were taken.

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


# 7. [Beginner] Vowel and Consonant Counter

# Ask the user to enter a sentence. Count how many vowels and consonants it contains. Treat uppercase and lowercase letters equally, 
# and ignore spaces, numbers, and punctuation when counting letters. Display both counts.

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

# 8. [Beginner] Find the Largest and Smallest Number

# Ask the user to enter five numbers and store them in a list. Without using the built-in max() and min() functions, find and display 
# the largest and smallest values. Use a loop to compare the numbers.

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

# 9. [Intermediate] Word and Character Analyzer

# Ask the user to enter a sentence or short paragraph. Analyze the text and display the total number of words, characters excluding 
# spaces, vowels, and consonants. Uppercase and lowercase letters should be counted equally, while digits and punctuation should not be 
# treated as letters.

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

# 10. [Intermediate] Remove Duplicate Values from a List

# Given a list of numbers entered by the user, create a new list in which each value appears only once. Preserve the order in which 
# values first appeared. For example, [4, 2, 4, 7, 2, 9] should become [4, 2, 7, 9]. Do not use set() to solve this task.

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

# 11. [Intermediate] Second-Largest Unique Number

# Ask the user to enter several numbers separated by spaces. Find the second-largest distinct value. For example, if the input is 10 20 
# 20 15, the answer should be 15 because the largest distinct value is 20 and the second-largest is 15. If fewer than two distinct 
# values are provided, display a helpful message.

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

# 12. [Intermediate] Word Frequency Counter

# Ask the user to enter a paragraph. Count how many times each word appears. Treat uppercase and lowercase versions of a word as the 
# same, and remove basic punctuation before counting. Store the results in a dictionary and display the words from highest frequency to 
# lowest frequency.

paragraph=input("enter the para : ").lower()
words=paragraph.split();
frequency = {};
for element in words:
    clean_word=element.strip(string.punctuation);
    if clean_word == "":
        continue
    if clean_word not in frequency:
        frequency[clean_word]=1;
    else:
        frequency[clean_word] +=1;
print(frequency);
# print(frequency.items())
sorted_words=sorted(frequency.items(),key=lambda item: item[1],reverse=True)
for elements in sorted_words:
    print(elements[0],":",elements[1]);