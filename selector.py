import random

def get_lucky_nums():
    return random.sample(range(1,46), k=6)
   
if __name__ == '__main__':
    times = int(input('Enter num(1-100): '))
    for i in range(times):
        print(sorted(get_lucky_nums()))

