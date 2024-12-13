
'''n = 6

result_list = [0]*6

for i in range(1,n+1) :
    result_list[i-1] = i**2

print(result_list)'''


'''////////'''


'''list_numb = [12,13,43,18,17]

result_list =[i%3 == 0 for i in list_numb]

print(list_numb)'''



'''//////////'''

'''n = 5
result_list = [1 for x in range(n)]

print(result_list)'''

'''////////'''



'''list_numb = [12,13,43,18,17]

result_list =[2*i-1 for i in list_numb if i%3 == 0]

print(result_list)'''

'''//////'''

'''print('p y t h o n'.split(' '))'''

'''/////////'''

'''//////'''

'''numb = input(' input your numbers with spacese:')

print(numb)'''

'''/////////'''


'''numb = input(' input your numbers with spacese:')


result_list = [i for i in numb.split(' ')]


print(result_list)'''

'''/////////////////'''

'''text = 'python'
result = [el.upper() for el in text]


print(result)'''

'''///////////////'''

'''result = [x for x in range(100,200)if x%2 == 0 or x%3 == 0]

print(result)'''

'''/////////////...'''

'''names = ['ia', 'goga', 'putbca']
result = [n.capitalize() for n in names if len(n)>4]

print(result)'''

'''numb = [12, 22, 34, 6, 7, 89, 0]

result = [f'{x} is even' if x%2 == 0 else f'{x} is odd' for x in numb]

print(result)


x = {x**2 for x in range(1,5)}

print(x)


ls = [1,2,3,4,10]

s = {x**2 for x in ls}

print(s)

ls = [1,2,3,4,4,5,2,]

s = {int(x) for x in ls}

print(s)

import time
start = time.time() 

print(start)

import time

start = time.time() 

s = {x**2 for x in range(10000)}

finish = time.time()

print(finish - start)
import time
start_for = time.time()
ls = []
for n in range(1000) :
    ls.append(n**2)
    finish_for = time.time()
    print(finish_for - start_for)


di = {
    'gela' : 3,
    'nugzari' : 2,
    'jemali' : 1,
    'madulo' : 4,
    'zaka' : 5
}

dict_transf = {x for x in di}

print(dict_transf)

di = {
    'gela' : 3,
    'nugzari' : 2,
    'jemali' : 1,
    'madulo' : 4,
    'zaka' : 5
}

dict_transf = di.items()

print(dict_transf)

di = {
    'gela' : 3,
    'nugzari' : 2,
    'jemali' : 1,
    'madulo' : 4,
    'zaka' : 5
}

dict_transf = {key.upper() : value for key,value in di.items()}

print(dict_transf)

ls = [10,11,12,13,14]

ite = iter(ls)

print(next(ite))
print(next(ite))
print(next(ite))
print(next(ite))
print(next(ite))'''


ls = [10,11,12,13,14]

gen = (x**2 for x in ls)

print(next(gen))