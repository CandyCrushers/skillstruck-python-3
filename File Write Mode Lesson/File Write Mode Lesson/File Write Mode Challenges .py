# Never Mind

'''file = open("email.txt", "w")
file.write("Never mind")
file.close 


file = open("email.txt", "r")
print(file.read())
file.close() ''' 

# -----------------------------------------------------------------------

# Custom Greeting Cards 

answer = input("Enter a sentence")

file = open("report.txt", "w")
file.write(answer)
file.close()

file = open("report.txt", "r")
print(file.read())
file.close()
