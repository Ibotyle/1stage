import requests
    
def is_prime(n):
    """check if number is prime."""
    for i in range(2, n):
        if n%i == 0:
            return False
    return True if n > 1 else False


def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if(n % i == 0):
            sum = sum + i
    if (sum == n):
        return True
    else:
        return False


def properties(n):
    properties = []
    order = len(str(abs(n)))
    sum = 0

    temp = abs(n)
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if abs(n) == sum:
        properties.append("armstrong")
        
    if n%2 == 0:
        properties.append("even")
    
    if n%2 == 1:
        properties.append("odd")
    
    return properties


def digit_sum(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def fun_fact(n):
    url = "http://numbersapi.com/" + str(n) + "/math"
    return requests.get(url).text