#Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func():
    v_1 = int(input())
    v_2 = int(input())
    v_3 = int(input())
    v_4 = (v_1 + v_2 + v_3) - min(v_1, v_2, v_3)
    return v_4

my_func_1 = my_func()
print(my_func_1)