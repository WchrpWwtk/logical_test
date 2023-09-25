# เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial ด้วย Python โดยห้ามใช้ math.factorial เช่น 7! = 5040
# มีเลข 0 ต่อท้าย 1 ตัว, 10! = 3628800 มีเลข 0 ต่อท้าย 2 ตัว


def factorial(num: int) -> int:
    if num == 0:
        return 1

    return num * factorial(num - 1)


def count_last_zero(num: int) -> int:
    count: int = 0

    while num > 0:
        if num % 10 == 0:
            count += 1
            num = num // 10
        else:
            return count

    return count


if __name__ == "__main__":
    try:
        num_input: int = int(input("Enter number: ")) or 0
    except ValueError as error:
        raise error
    
    factorial_number = factorial(num_input)
    
    print("Factorial:", factorial_number)
    
    print("Total last zero:", count_last_zero(factorial_number))
