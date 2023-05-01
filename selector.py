import random

def get_lucky_nums():
    result = random.sample(range(1,46), k=6)
    return result

if __name__ == '__main__':
    print(get_lucky_nums())

