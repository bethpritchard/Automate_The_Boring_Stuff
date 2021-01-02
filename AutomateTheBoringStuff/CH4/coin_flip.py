import random as rand
streak_count = 0
n_runs = 10000
flips_per_run = 100
streak_length = 6


for experimentNumber in range(n_runs):

    # Code that creates a list of 100 'heads' or 'tails' values.
    coin_flips = []
    for i in range(flips_per_run):
        flip = rand.randint(0, 1)
        if flip == 0:
            coin_flips.append('H')
        elif flip == 1:
            coin_flips.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(coin_flips)-6):
        current_streak = 0
        for j in range(6):
            if coin_flips[i] == coin_flips[i+j]:
                current_streak +=1
            else:
                break
        if current_streak == 6:
            streak_count += 1
    print(streak_count)

print("The odds are " + str((streak_count / n_runs)) + '%')