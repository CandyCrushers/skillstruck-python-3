# Secret Agent Name Generator 


name = ["Java", "Python", "JavaScript", "Lua"]
last = ["py", "ja", "js", "l"]
list = []

for i in name: 
    for y in last: 
        full_name = i + " " + y
        list.append(full_name)



print(list) 


