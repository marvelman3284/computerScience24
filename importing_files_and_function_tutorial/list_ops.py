def count_fives(l):
    return len([i for i in l if i % 5 == 0])

def list_to_binary(l):
    return list(map(lambda x: (f'{x:08b}'), l))

def reverse_list(l):
    return l[::-1]

def sliced_list(l, a, b):
    return l[a:b] if a > 0 and b < len(l) else l

def list_average(l):
    return sum(l)/len(l)

def list_product(l):
    prod = 1
    for i in l:
        prod *= i

    return prod

# before refactor
print("hello world")
print(__name__)

# after refactor
def main():
    print("hello world")
    print(__name__)

if __name__ == "__main__":
    main()
