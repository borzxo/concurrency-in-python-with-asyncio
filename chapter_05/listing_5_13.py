def pos_int(until: int):
    for i in range(until):
        yield i


pos_it = pos_int(10)

print(next(pos_it))
print(next(pos_it))
print(next(pos_it))
print(next(pos_it))
print(next(pos_it))
print(next(pos_it))
print(next(pos_it))