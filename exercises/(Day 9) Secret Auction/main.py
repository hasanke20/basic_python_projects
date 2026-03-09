import art
print(art.gavel)
any_other_bidder = True
bids = {}
max = 0
winner = None
while any_other_bidder is True:
    new_bidder = input("What's your name?")
    new_bid = int(input("What's your bet? $"))
    bids[new_bidder] = new_bid
    wanna_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if wanna_continue == 'no':
        for i in bids:
            if bids[i] > max:
                winner = i
                max = bids[i]
        print(f"Your winner is {winner}! Highest bid was {max}.\n Everyone's bid:\n {bids}")
        any_other_bidder = False
    else:
        print("\n" * 100)