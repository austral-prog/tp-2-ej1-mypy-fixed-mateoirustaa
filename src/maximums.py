def max_of_two(x: int, y: int) -> int:
    biggest: int = x
    if x >= y:
        return biggest
    else:
        biggest = y
        return biggest
print(max_of_two(5,4))
print(max_of_two(-2,-3))
print(max_of_two(0,0))

def max_of_three(x: int, y: int, z: int) -> int:
    if y < x > z:
        return x
    elif x < y > z:
        return y
    else:
        return z
print(max_of_three(5,4,7))

print(max_of_three(-2,-3,-1))

print(max_of_three(0,0,0))