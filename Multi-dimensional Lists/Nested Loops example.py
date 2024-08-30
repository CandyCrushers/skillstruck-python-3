rows = [1,2,3]
cols = ["red", "green", "orange", "blood"]
list = []


for i in rows: # So we have rows which is 3 rows
    col = [] # The loop then makes 3 EMPTY ROWS
    for j in cols: # We then comes down to fill in the col LISTS
        col.append(j) # This appends J in COL's J is a placeholder, this code then fills all 3 empty lists with the colors because J is in cols
    list.append(col) # This then puts the coloums into a bigger list by calling in the list from up above and appending it or adding onto all 3 of them 