from numpy import random

player = list(random.randint(1,11,2)) #GIVES PLAYER'S CARDS
bot = list(random.randint(1,11,2)) #GIVES BOT'S CARDS

print(f"The dealer has these cards [x,{bot[1]}]")

while True:
    print(f"you're at {sum(player)} with these cards {player}")
    hit_or_stay = input("you wanna hit or stay?(hit/stay) ""\n").lower()

    #BASIC GAME RULES

    if hit_or_stay == "hit":
        player.append(random.randint(1,11)) #ADDING RANDOM CARD TO PLAYER'S DECK
    elif hit_or_stay == "stay":
        print(f"the dealer has {bot} which sum up to {sum(bot)}")
        if sum(bot) > sum(player): #CHECKING WINNER
            print("the dealer won!")
            break
        else:
            while True:
                bot.append(random.randint(1,11)) #ADDING RANDOM CARD TO BOT'S DECK
                print(f"the dealer has {bot} which sum up to {sum(bot)}")

                if sum(bot) > sum(player) and sum(bot) <= 21: #CHECKING WINNER
                    print("The dealer won!")
                    break
                elif sum(bot) >21: #CHECKING WINNER
                    print("you won!")
                    break
            break


    if sum(player) == 21: #CHECKING WINNER
        print(f"you have {sum(player)} with these cards {player}")
        print("you win")
        break
    elif sum(player)>21: #CHECKING WINNER
        print(f"you lost! your cards {player} which sum up to {sum(player)}")
        print(f"the dealer had {bot} which sum up to {sum(bot)}")
        break