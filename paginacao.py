items = list(range(1,101))
items_per_page = 49

# print(items)

if (len(items) % items_per_page) > 0:
    qtd_group_rest = (len(items) % items_per_page)
    num_div = int((len(items) - qtd_group_rest) / items_per_page)
    
    array_final = []
    array_temp = items[:]
    
    i = 0
    while i < num_div:
        array_final = array_final + [array_temp[:items_per_page]]
        array_temp = array_temp[items_per_page:]
        i += 1
        
    array_final = array_final + [items[-qtd_group_rest:]]
else:
    num_div = int(len(items) / items_per_page)
    
    array_final = []
    array_temp = items[:]
    
    i = 0
    while i < num_div:
        array_final = array_final + [array_temp[:items_per_page]]
        array_temp = array_temp[items_per_page:]
        i += 1
        
# print(len(array_final), array_final)
