# 1
print("Answer 1: ")
def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
         
# Driver code
n = 3
TowerOfHanoi(n,'A','B','C')
# A, C, B are the name of rods


# 2
print("\nAnswer 2: ")
print("Pascal's triangle using recursion: ")
n=int(input("Enter the number of rows in pascal's triangle:"))
def pascal(n, originaln=n):
    if n == 0:
        return

    pascal(n - 1, originaln)

    # printing the spaces
    print('  ' * (originaln - n), end='')

    # first number is always 1
    entry = 1
    for i in range(1, n + 1):
        print(entry, end='   ')

        # using Binomial Coefficient
        entry = entry * (n - i) // i
    print()


pascal(n)

print("Pascal's triangle using iteration: ")
 
for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(' ', end='')
 
    # first element is always 1
    C = 1
    for j in range(1, i+1):
 
        # first value in a line is always 1
        print(' ', C, sep='', end='')
 
        # using Binomial Coefficient
        C = C * (i - j) // j
    print()


# 3
print("\nAnswer 3: ")

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the first integer: "))
rem = num1 % num2
quot = num1 // num2
print("Remainder is: ", rem)
print("Quotient is: ", quot)
if (rem != 0):
    if (quot != 0):
        print("Both values are non zero")
    else:
        print("One value is zero")
else:
    if (quot != 0):
        print("One value is zero")
    else:
        print("Both values are zero")
# (c)
set1 = set()
for i in range(4, 7):
    a = rem + i
    b = quot + i
    if (a > 4):
        set1.add(a)
        print(set1)
    if (b > 4):
        set1.add(b)
        print(set1)

print(set1)
# (d)
set2 = frozenset(set1)
print("Immutable set: ", frozenset(set1))
# (e)
print("Largest value in the set: ", max(set2))
k = max(set2)
print("Hash value: ", hash(k))

# 4
print("\nAnswer 4: ")
print("")

class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid

    def __del__(self):
        print("Object destroyed")


# creating object
student_1 = Student("Gautam", 21105052)
print("Object created")

# printing the assigned values
print(f"The name of the student it {student_1.name} and SID is {student_1.sid}.")

# deleting object
del student_1


# 5
print("\nAnswer 5: ")


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __del__(self):
        print(f"Employee {self.name} record deleted")


# creating employee records
employee_1 = Employee("Mehak", 40000)
employee_2 = Employee("Ashok", 50000)
employee_3 = Employee("Viren", 60000)

# (a) updating the salary of Mehak
employee_1.salary = 70000
print(f"(a) The updated salary of the employee {employee_1.name} is {employee_1.salary}")

# (b) deleting the record of employee Viren
print("(b) ", end='')
del employee_3

print("\nAnswer 6: ")

# word uttered by the first person(George)
word = input("Enter the first word: ")

# new meaningful word formed by the exact same letters(by Barbie)
new_word = input("\nEnter a new meaningful word to test your friendship: ")


def count_in_dict(word):
    count = {}
    list_1 = list(word)

    for i in range(len(list_1)):
        if list_1[i] in count:
            count[list_1[i]] += 1
        else:
            count[list_1[i]] = 1
    return count


# test to verify the letters of the new word
if count_in_dict(word) != count_in_dict(new_word):
    print("The letters aren't exact,your friendship is fake!")


# shopkeeper's input to verify the word's meaning
def userinput():
    ans = input("\nDoes the word makes sense?(y or n)\n")

    if ans == 'y':
        print("Your friendship is real!\n\n")
    elif ans == 'n':
        print("The word doesn't have a meaning,your friendship is fake!\n\n")
    else:
        print("Invalid input, try again")
        userinput()

userinput()
print("")