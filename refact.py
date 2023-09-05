import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer = []
user = []


def user_getcard(cards):
    x = 1
    while x <= cards:
        random_card = random.randint(0, len(deck) - 1)
        user.append(deck[random_card])
        x += 1


def dealer_getcard(cards):
    y = 1
    while y <= cards:
        random_card = random.randint(1, len(deck) - 1)
        dealer.append(deck[random_card])
        y += 1


game_over = False
r = 2

while not game_over:
    user_getcard(r)
    dealer_getcard(r)

    user_score = 0
    dealer_score = 0

    for i in user:
        user_score += i

    for i in dealer:
        dealer_score += i

    lento = len(dealer)
    print(f"Your cards: {user}")
    print(f"Dealer's cards: {dealer[1:lento]}")

    # nuevo
    if 11 in dealer and dealer_score > 21:
        index_dealer = dealer.index(11)
        dealer[index_dealer] = 1
        dealer_score = 0
        for i in user:
            dealer_score += i

    if user_score > 21:
        if 11 in user:
            index = user.index(11)
            user[index] = 1
            user_score = 0
            for i in user:
                user_score += i
        else:
            game_over = True
    else:
        question = input("Do you want more cards? Y or N ").lower()
        if question == "y":
            game_over = False
            r = 1
        elif question == "n":
            game_over = True

print(f"Dealer's hand: {dealer}")
print(f"Dealer score is: {dealer_score}")

# nuevo
while dealer_score < 17:
    print("Dealer does not have enough cards")
    random_card = random.randint(0, len(deck) - 1)
    dealer.append(deck[random_card])
    dealer_score = 0
    for i in dealer:
        dealer_score += i
    print(f"Dealer's hand: {dealer}")
    print(f"Dealer score is: {dealer_score}")

print(f"Your score is: {user_score}")

if user_score == 21:
    if dealer_score == 21:
        print("Tie!")
    else:
        print("You Win!")

elif user_score > dealer_score and user_score < 21:
    print("You win!")

elif user_score > 21:
    print("You lose!")

elif user_score < 21 and dealer_score > 21:
    print("You win!")
