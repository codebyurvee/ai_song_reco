import math   

# DOT PRODUCT
def dot_product(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result


# MAGNITUDE 
def magnitude(a):
    result = 0
    for i in range(len(a)):
        result += a[i] ** 2
    return math.sqrt(result)


# COSINE SIMILARITY
def cosine(a, b):
    mag_a = magnitude(a)
    mag_b = magnitude(b)

    # safety check 
    if mag_a == 0 or mag_b == 0:
        return 0

    return dot_product(a, b) / (mag_a * mag_b)
