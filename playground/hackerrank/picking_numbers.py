a = [1,1,2,2,4,4,5,5,5]

counter_dict = dict()

for elem in a:
    if elem not in counter_dict:
        counter_dict[elem] = 1
    else:
        counter_dict[elem] += 1

max_set_count = 0
for elem in sorted(counter_dict.keys()):
    if elem+1 in counter_dict:
        current_set_count = counter_dict[elem] + counter_dict[elem+1]
    else:
        current_set_count = counter_dict[elem]
    if current_set_count > max_set_count:
            max_set_count = current_set_count
        

# %%