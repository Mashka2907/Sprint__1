num = int(input('Введите число для вычисления цифрового корня: '))

def digit_root(num):
    while num > 9:
        sum_num = 0
        while num > 0:
            sum_num += num % 10
            num //= 10
        num = sum_num
    return num


print(digit_root(num))