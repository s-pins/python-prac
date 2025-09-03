def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    return False
print(large_power(2, 13))  # True
print(large_power(2, 12))  # False