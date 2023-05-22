# Задача 2: Найдите сумму цифр трехзначного числа

numbers = input("Введите трех значное число: ")
sum = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
print(numbers, " -> ", sum, f" ({numbers[0]} + {numbers[1]} + {numbers[2]})")
