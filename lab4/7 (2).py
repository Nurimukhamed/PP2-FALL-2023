n = int(input())
all_nums = set(range(1, n + 1))
while True:
    guess = input()
    if guess == "HELP":
        break
    guess = {int(x) for x in guess.split()}
    answer = input()
    if answer == 'YES':
        all_nums &= guess
    else:
        all_nums -= guess
 
print(*all_nums)
