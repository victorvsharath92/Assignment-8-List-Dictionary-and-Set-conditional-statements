#1. List Creation:
#a.
age_list = [8, 33, 34, 60, 31]

#b.
name_list = ["Sreshta", "Amrutha", "Sharath", "Suni", "Krishna"]

#2. List Operations / Modifications:

#a.
name_list.append("Yazhini")

#b.
age_list.insert(2, 30)

#c.
name_list.remove("Yazhini")

#d.
age_list.pop()

#e.
age_list.extend([29, 30, 26])

#f.
age_list.sort(reverse=True)

#g.
max_age = max(age_list)

min_age = min(age_list)

sum_age = sum(age_list)

#3. Accessing List Elements:

#a.
first_element = name_list[0]

print(first_element)

#b.
last_element = name_list[-1]

print(last_element)

#c.
elements_by_index = name_list[2:5]

print(elements_by_index)

#d.
reverse_elements = name_list[::-1]

print(reverse_elements)

#3

#a.
student_marks = {"Sreshta": 85, "Amrutha": 90, "Sharath": 78, "Suni": 92, "Krishna": 88}

#b.
print(student_marks["Amrutha"])

#c.
student_marks["Janani"] = 80

print(student_marks)

#d.
student_marks["Sharath"] = 82

print(student_marks)

#e.
print(student_marks.keys())

print(student_marks.values())

print(student_marks.items())

#Sets(operations):
#a.
my_set = {'a','e','i','o','u','a','a','i'}

print(my_set)

#Explanation:Set does not allow duplicate values, so the repeated 'a' and 'i' are removed, also the order of elements is not guaranteed.

#b.
my_set[4] = 's'

print(my_set)

#Explanation: Sets are unordered collections of unique elements, and they do not support indexing or item assignment. Therefore, trying to assign a value to a specific index in a set will result in an error.

#c.
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

#d.
#Union of two sets

union = (set1.union(set2))

print("Union:", union)

# Intersection of two sets

intersection = (set1.intersection(set2))

print("Intersection:", intersection)

#Operators & Conditional Statements :
#(IF, ELIF, ELSE)

#Performance Category Program:
#1.
score = float(input("Enter a score (0 to 10): "))

#2.
if score > 7 and score <= 10:
    category = ("Above Average")

elif score >= 4 and score <= 7:
    category = ("Average")

elif score >= 0 and score < 4:
    category = ("Below Average")

else:
    category = ("Invalid score. Please enter a value between 0 and 10.")

#3.
print("Performance Category:", category)

#4.
if category == "Above Average":
    print("Great job! Keep up the good work.")

elif category == "Average":
    print("You are doing well, but there's room for improvement.")

elif category == "Below Average":
    print("You need to work harder and improve your performance.")