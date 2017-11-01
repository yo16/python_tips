# -*- coding: utf-8 -*-

list1 = [5,2,3,1,4]
list1 = sorted(list1)
print('list1')
print(list1)

list2 = [5,2,3,1,4]
list2.sort()
print('list2')
print(list2)

student_tuples = [		\
    ('john', 'A', 15),	\
    ('jane', 'B', 12),	\
    ('dave', 'B', 10),	\
]
list3 = sorted(student_tuples, key=lambda student: student[2])   # sort by age
print('list3')
print(list3)

# 逆順
list4 = sorted(list1, reverse=True)
print('list4')
print(list4)


