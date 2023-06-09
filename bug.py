import itertools

blackjack_hands = ["A","J","Q","K","10"]

cards = ["A","K"]

print([x for x in itertools.permutations(blackjack_hands, 2) if "A" in x])

if cards[0:2] in [list(x) for x in itertools.permutations(blackjack_hands, 2) if "A" in x]:
    print("hit Blackjack")
else:
    print("Problem")