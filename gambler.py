import random


class GamblingProb:


    def Gambler(stake,goal):
        stake = 100
        goal = 200
        bet = 1
        win = loss = num_of_bet = 0
        while stake <= goal:
            betCheck = random.randint(0, 1)
            if betCheck == 1:
                win += 1
                print("Total win is ", win)
                stake += bet
                if (stake == goal):
                    break
                else:
                    loss += 1
                    stake -= bet
                    print("total loss is ", loss)
                    if (stake == 0):
                        break

            num_of_bet = num_of_bet + 1
            print("Win percentage:", (win / num_of_bet) * 100)
            print("Loss percentage", (loss / num_of_bet) * 100)
            break

obj = GamblingProb()
gambler_percent = obj.Gambler()
print(" Gambler win or loss percent is ", gambler_percent)

