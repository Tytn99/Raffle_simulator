import random
print('Welcome to raffle simulator')
W = f'''Won - Invoice from __ #({random.randint(1, 4000)})
Congrats on your w! check your email and you will see your invoice!!'''
L = ("Another L")
i = input('-Enter raffle entry number- (between 1 and 1600): ')
entries = list(range(1, 1600))
print()
your_number = int(i)
numbers_generated = random.choices(entries, k=10)
if your_number in numbers_generated:
    print(W)
else:
    print(L)
print()
print(f'Resulting numbers : {numbers_generated}')

