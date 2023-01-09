import random
from tqdm import tqdm

dice = [1, 2, 3, 4, 5, 6]
winner = []

for i in tqdm(range(10000000)):
    bank_score = 0
    player_score = 0
    actPlayer = "bank"

    while True:
        # find legit roll
        while True:
            roll = sorted(random.choices(dice, k=3))
            if roll[0] != roll[1] != roll[2] and roll not in [[1, 2, 3], [4, 5, 6]]:
                continue
            else:
                break

        # check for auto win
        if roll in [[4, 5, 6], [1, 1, 6], [2, 2, 6], [3, 3, 6], [4, 4, 6], [5, 5, 6], [6, 6, 6]] or len(set(roll))==1:
            if actPlayer == "bank":
                winner.append('bank')
            else:
                winner.append('player')
            actPlayer = 'bank'
            break

        # check for auto loss
        elif roll in [[1, 2, 3], [1, 1, 1], [1, 2, 2], [1, 3, 3], [1, 4, 4], [1, 5, 5], [1, 6, 6]]:
            if actPlayer == "bank":
                winner.append('player')
            else:
                winner.append('bank')
            actPlayer = 'bank'
            break

        # take score
        elif len(set(roll)) == 2:
            pair_sum = []
            for x in range(2):
                if roll[x] == roll[x+1]:
                    pair_sum = roll[x] + roll[x + 1]
            act_score = sum(roll) - pair_sum
            if actPlayer == "bank":
                bank_score = act_score
            else:
                player_score = act_score

        # check bank scored
        if player_score == 0 and bank_score != 0:
            actPlayer = "player"
            continue

        # check player scored
        elif player_score != 0:
            actPlayer = "bank"
            # check draw
            if player_score == bank_score:
                bank_score = 0
                player_score = 0
                continue
            # check gg
            else:
                if player_score > bank_score:
                    winner.append('player')
                if player_score < bank_score:
                    winner.append('bank')
                break

bank_wins = sum(1 for i in winner if i=='bank')
player_wins = sum(1 for i in winner if i=='player')
bankroll_bank = bank_wins - player_wins
bankroll_player = player_wins - bank_wins

print(f"TOTAL GAMES: {len(winner)}")
print("")

print("BANK:")
print(f"  > wins {100*bank_wins / len(winner)}% of the Rolls")
print(f"  > total wins: {bank_wins}")
print(f"  > bankroll: {bankroll_bank}$")
print(f"  > ExpValue: {100*bankroll_bank/ len(winner)}%")
print("")

print("PLAYER:")
print(f"  > wins {100*player_wins / len(winner)}% of the Rolls")
print(f"  > total wins: {player_wins}")
print(f"  > bankroll: {bankroll_player}$")
print(f"  > ExpValue: {100*bankroll_player/ len(winner)}%")
