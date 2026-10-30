import math



def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("sides must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("not a valid triangle")
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "scalene"



def course_result(coursework, final, attendance):
    for v in (coursework, final, attendance):
        if not 0 <= v <= 100:
            raise ValueError("values must be between 0 and 100")
    if attendance < 75:
        return "Fail"
    if final < 40:
        return "Fail"
    total = coursework * 0.4 + final * 0.6
    if total >= 85:
        return "Distinction"
    elif total >= 50:
        return "Pass"
    else:
        return "Fail"



def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result



def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True



def primes_below(n):
    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)
    return result



def first_repeated(values):
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] == values[j]:
                return values[i]
    return None



def count_pairs(n):
    if n < 2:
        return 0
    return n * (n - 1) // 2


def count_pairs_loop(n):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            count += 1
    return count



def calculator(command):
    match command:
        case ["add", a, b]:
            return a + b
        case ["sub", a, b]:
            return a - b
        case ["mul", a, b]:
            return a * b
        case ["div", a, b]:
            if b == 0:
                raise ValueError("division by zero")
            return a / b
        case ["neg", a]:
            return -a
        case ["sum", *nums]:
            return sum(nums)
        case _:
            raise ValueError(f"unknown command: {command}")



def parse_int(text, default=None):
    try:
        return int(text)
    except ValueError:
        return default



def stats(*numbers):
    if not numbers:
        raise ValueError("stats() needs at least one number")
    lo = hi = numbers[0]
    for x in numbers[1:]:
        if x < lo:
            lo = x
        if x > hi:
            hi = x
    return lo, hi
