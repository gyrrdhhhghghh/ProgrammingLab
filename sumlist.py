lista = [1,1,1,1]

def sum_list(my_list):
    if not my_list:
        return None
    else:
        return sum(my_list)

print(sum_list(lista))