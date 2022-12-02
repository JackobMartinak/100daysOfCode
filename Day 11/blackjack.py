import art
import random


def deal_card(card):
    return card[random.randint(0, len(card) - 1)]


def calculate_score(cards):
    if sum(cards) == 21:
        return 0
    else:
        if sum(cards) > 21:
            if 11 in cards:
                cards.remove(11)
                cards.append(1)
                return 1
            else:
                return 2
        else:
            return sum(cards)


def compare(u_cards, c_cards):
    if sum(u_cards) > sum(c_cards):
        return 0
    elif sum(u_cards) == sum(c_cards):
        return 1
    else:
        return 2


print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
is_gameOver = False

user_cards = []
computer_cards = []


for _ in range(0, 2):
    user_cards.append(deal_card(cards))
    computer_cards.append(deal_card(cards))


while not is_gameOver:
    print(f"The dealer's first card is {computer_cards[0]}\n ")

    print(f"These are your cards {user_cards}")
    print(f"The sum of cards the is {calculate_score(user_cards)}")

    is_continuing = input("Do you want to draw another card? (y/n) ").lower()
    if is_continuing == "y":
        user_cards.append(deal_card(cards))
        if calculate_score(user_cards) == 2:
            print("You got BUST! ")
            print(f"The sum of cards {calculate_score(user_cards)}")
            break
        elif calculate_score(user_cards) == 0:
            print("You got a black jack! Congrats!")
            break
        else:
            continue
    if is_continuing == "n":
        if compare(user_cards, computer_cards) == 0:
            print(
                f"You've won! Your cards {user_cards} and their sum {calculate_score(user_cards)}"
            )
            print(
                f"Dealer's cards {computer_cards} and their sum {calculate_score(computer_cards)}"
            )
            break
        elif compare(user_cards, computer_cards) == 1:
            print(f"It's a tie with sum of {calculate_score(user_cards)}")
            break
        else:
            print(
                f"You lost! Your cards {user_cards} and their sum {calculate_score(user_cards)}"
            )
            print(
                f"Dealer had {computer_cards} with sum of {calculate_score(computer_cards)}"
            )
            break

    break
