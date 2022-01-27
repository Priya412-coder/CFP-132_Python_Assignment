import random

class FlipCoin:
    def find_percent(self, number):
        heads = 0
        tails = 0
        heads_percent = 0
        tails_percent = 0
        if number < 0:
            return "please enter a valid number"
        for count in range(number):
            toss = random.randint(1,10)/10
            if toss < 0.5:
                heads += 1
            else:
                tails += 1
        heads_percent = (heads/number)*100
        tails_percent = (tails/number)*100
        return (f"total head percent is {heads_percent} and tail percent is {tails_percent}")

flip_coin = FlipCoin()
count = int(input("How many times you want to flip the coin?\n"))
print(flip_coin.find_percent(count))