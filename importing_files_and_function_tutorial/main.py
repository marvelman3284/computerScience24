from random import randint
from list_ops import list_average

def generate_list(a, b):
    return [randint(a, b) for _ in range(20)]

# before refactor
new_list = generate_list(0, 10)
avg = list_average(new_list)
print(avg)

# after refactor
def main():
    new_list = generate_list(0, 10)
    avg = list_average(new_list)
    print(avg)

if __name__ == "__main__":
    main()
