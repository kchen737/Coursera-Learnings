print("hello world")

x = input('Please enter a number: ')
if int(x) >5 :{
    print('correct')
}


#format
str1 = 'hello'
str2 = 'world'
print('{} {}'  .format(str1, str2))


#type searching
age = input('How old are you')
print(f"Type of age variable is: {type(int(age))}. It should be <class 'int'>")


#match, using cases:
status = input('what is the status')
match status:
    case 1:
        print('case 1 is met')
    case 2:
        print('case 2 is met') 
        
        
#string loop
name = input('enter a string')

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    print('One of my favorite desserts is', dessert)
    
    
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

for x,num in enumerate(num_list):
    if num == 36:
        print('Number found at ', x)
        
#list:

list1 = [1,2,3,"hello",5,]
print(list1, sep=" ")
list1.insert(len(list1), 6)
del list1[2]

for x in list1:
        print("List: ", x)
        
#Tuple could be number, strings, float and boolean
    #everthing is tuple is immutable
my_tuple = 1, 'strings', 5.5, True


#sets
set_a = {1,2,3,4,5,5}
set_b = {4,5,6,7,8}
print(set_a.union(set_b)) # or use symbols like | for union

#dictionary
sample_dict = {1: 'Coffee', 2: 'Tea'}
del sample_dict[3]

#args
def sum_of(*args):
    sum = 0
    for x in args:
        sum+=x
    return sum
print(sum_of(2,3,4))

#kwargs
def sum_of(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)
print(sum_of(coffee=2.99, cake =4.55, juice=2.99))

#file handling
file = open('test.txt',  mode = 'r')
data = file.readline()
print(data)

with open('newfile.txt', 'a') as file:
    file.writelines("\nThis is a new file created")
    
    
# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination):
    # Base Condition
    if (disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        return

    # Recursive calls in which function calls itself
    hanoi(disks - 1, source, destination, helper)
    print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
    hanoi(disks - 1, helper, source, destination)
    
disks = int(input('Number of disks to be displaced: '))

#map and filter
menu = ["espresso", "cappuccino", "cortado"]

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee
    
map_coffee = map(find_coffee, menu)
for x in map_coffee:
    print(x)
#print out everything in the list, if it does not match the condition, it will print none

filter_coffee = filter(find_coffee, menu)
for x in filter_coffee:
    print(x)
    
