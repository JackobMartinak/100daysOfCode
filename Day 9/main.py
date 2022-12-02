bidders = {}
next_one = True

while next_one:
    bidder = input("What's your name? ")
    bid = float(input("What's your bid? "))
    bidders[bidder] = bid
    is_next_bidder = input("is there someone who want's to bid? (y/n) ").lower()
    if is_next_bidder == "y":
        continue
    elif is_next_bidder == "n":

        break

max = 0.0
for i in bidders:
    if bidders.get(i) > max:
        max = bidders.get(i)

winner = [k for k, v in bidders.items() if v == max]

print(f"{winner[0]} is the winner with ${max} bid")