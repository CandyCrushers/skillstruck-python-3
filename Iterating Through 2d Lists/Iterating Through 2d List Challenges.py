# Multiply List Values


'''number = int(input("Enter a number!"))
my_list = [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]
rows = 4 
col = 3 

for i in range(rows):
    for j in range(col):
        my_list[i][j] = my_list[i][j] * number 


print(my_list)'''


# ----------------------------------------------------------------------


# Find The Largest

x = int(input("What is the first number?"))

y = int(input("What is the second number?"))

z = int(input("What is the third number?"))

my_list = [[0, 1, x], [10, 15, y], [100, 200, 300], [5, 6, z]]

rows = 4 
cols = 3 

maxval = my_list[0][0]

for i in range(rows): 
    for j in range(cols): 
        if my_list[i][j] > maxval:
            maxval = my_list[i][j]
           

print(maxval)