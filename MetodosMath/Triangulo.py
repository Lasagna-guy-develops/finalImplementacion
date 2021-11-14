def area(l1, l2, l3):
    p = perimetro(l1, l2, l3)
    s = p / 2
    return (s * (s - l1) * (s - l2) * (s - l3)) ** 0.5

def perimetro(l1, l2, l3):
    return l1+l2+l3
