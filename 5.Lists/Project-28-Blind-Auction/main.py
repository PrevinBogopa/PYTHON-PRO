from replit import clear
# Clear function can be used to clear everything from the console
from ascii_art import logo
import os

print(logo)

bidders = {}
bidding_finished = False


def find_highest_bidder(bidders_record):
    highest_bid = 0
    winner = ""
    for bidder in bidders_record:
        bid_amount = bidders_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    bid_price = int(input("What is your bid amount?: $"))
    bidders[name] = bid_price
    should_continue = input("Are there any other bidder? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bidders)
    elif should_continue == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')

