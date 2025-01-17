def format_string(name, age):
    return f"My name is {name} and I am {age} years old"

def conditional_check(number):
    if number == 10:
        return "Equal"
    elif number > 10:
        return "Greater"
    else:
        return "Lesser"

def loop_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def list_operations(numbers):
    total_sum = sum(numbers)
    max_number = max(numbers)
    min_number = min(numbers)
    return (total_sum, max_number, min_number)

def dict_operations(students_dict):
    top_students = [name for name, score in students_dict.items() if score > 80]
    return top_students

def set_operations(list1, list2):
    common_elements = list(set(list1).intersection(set(list2)))
    return common_elements

def arithmetic_ops(a, b):
    result = { 
        'sum': a + b, 
        'difference': a - b, 
        'product': a * b, 
        'quotient': a / b if b != 0 else 'Division by zero error' } 
    return result

def logical_ops(x, y):
    result = { 
        'and': x and y, 
        'or': x or y, 
        'not_x': not x 
        } 
    return result

def bitwise_ops(a, b):
    result = { 
        'and': a & b, 
        'or': a | b, 
        'xor': a ^ b 
        } 
    return result