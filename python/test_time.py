import time

start_gener = time.time()
list_gener = (el**5 for el in range(100000))    
_max = max(list_gener)
finish_gener = time.time()

print("first------",finish_gener-start_gener)

start_list = time.time()

list_compr = [el**5 for el in range(100000)]    

_max = max(list_compr)

finish_list = time.time()

print("second------",finish_list-start_list)