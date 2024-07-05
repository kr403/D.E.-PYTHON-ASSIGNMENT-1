# 1. Data Types and Variables
int1 = 5
float1 = 0.5
string1 = "It's a string."
bool1 = True

print(type(int1))
print(type(float1))
print(type(string1))
print(type(bool1))

iplicitCasting1 = int1 + float1
print(iplicitCasting1)
iplicitCasting2 = int1 - float1
print(iplicitCasting2)

# 2. Control Flow (if/else)
try:
    input1 = int(input("Please enter a whole number: "))
    if (input1 % 2 == 0): print("Entered number is an even number.")
    else: print("Entered number is an odd number.")
except:
    print("Entered input isn't a whole number!!!")

# 3. Strings and Manipulation
string2 = "This is a sentence."
print(string2.upper())
print(string2.lower())
string2List = string2.split(' ')
print(string2List)
print(len(string2List))
string2Update = string2.replace("sentence", "string", 1) # case specific
print(string2Update)

# 4. Loops (for/while)
numberList1 = []
for i in range(1, 11):
    numberList1.append(i)
for i in numberList1:
    print(i*2)
startInteger1 = 1
endInteger1 = 10
sum1 = 0
while(True):
    if (startInteger1 <= endInteger1): 
        sum1 += startInteger1
        startInteger1 += 1
    else: break
print(sum1)

# 5. Lists and List Comprehensions
favoriteFruit1 = ["watermelon", "mango", "apple"]
favoriteFruit1sLength = [len(fruit) for fruit in favoriteFruit1]
print(favoriteFruit1sLength)
favoriteFruit1.append("grape")
favoriteFruit1.sort()
print(favoriteFruit1)

# 6. Dictionaries
bookDictionary = {
    "title": "A Tale of Two Cities", 
    "author": "Charles Dickens", 
    "year": 1859
}
print(bookDictionary["title"])
print(bookDictionary["author"])
print(bookDictionary["year"])
bookDictionary["genre"] = "Novel"
for details in bookDictionary:
    print(bookDictionary[details])