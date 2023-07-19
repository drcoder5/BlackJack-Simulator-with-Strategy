import random
import logging
import argparse
import time
from good_mode import BlackJack

logger = logging.getLogger("Loop")
logger.setLevel(logging.INFO)
# game = logging.FileHandler(filename="Game stats.log")
# logger.addHandler(game)

logging.basicConfig(filename="Probability.log", level=logging.INFO, format="%(message)s")

class Blackjacksim(BlackJack):
    CARDS = ["2","3","4","5","6","7","8","9","10","A","J","Q","K"]

    cards_per_deck = CARDS * 4
    GAME_DECK = cards_per_deck * 5
    True_count = 0
    Games = 0

    def __init__(self, name, is_dealer=False):
        super().__init__(name, is_dealer)
        self.bankroll = 1000
        self.betting_unit = 100
        self.earnings = []
        self.status = []
        self.record = {"wins":0, "lost":0, "goes bust":0, "hit Blackjack":0, "push":0}

    def dealt_card(self):

        if self.is_dealer:
            n = 1
        else:
            if not self.cards:
                n = 2
            else:
                n = 1

        cards = []
        for _ in range(n):
            x = random.choice(Blackjacksim.GAME_DECK)
            cards.append(x)
            Blackjacksim.GAME_DECK.remove(x)

        return cards

    def sim_deal_hand(self, n=0, dealer=None):
        if self.is_dealer:
            if n:
                self.read_cards_and_get_score()
            else:
                self.deal_hand()
        else:
            self.deal_hand(dealer)

    def winning_amount(self):
        moves = {"hit Blackjack": int(self.betting_unit * 1.5),
                    "wins": (self.betting_unit * 1),
                    "push": (self.betting_unit) ,
                    "lost": (- self.betting_unit),
                    "goes bust": (- self.betting_unit)}

        if self.move in moves:
            self.bankroll += moves.get(self.move)
            self.record[self.move] += 1
            self.earnings.append(moves.get(self.move))

    def set_bet_amount(self):
        if BlackJack.Live_Count > 0:
            Blackjacksim.True_count = round(BlackJack.Live_Count / len(Blackjacksim.GAME_DECK)/52)
            betting_unit_calc = Blackjacksim.True_count - 1
            self.betting_unit = self.betting_unit * betting_unit_calc

    @staticmethod
    def get_args():
        a_parser = argparse.ArgumentParser()
        a_parser.add_argument("-r", default=10, help="Number of games to simulate", type=int)
        Blackjacksim.Games = a_parser.parse_args().r

    @classmethod
    def new_game(cls, player, dealer):
        player.score = dealer.score = 0
        player.move = dealer.move =  None
        player.cards.clear()
        dealer.cards.clear()
        player.has_ace = dealer.has_ace = False

sim_dealer = Blackjacksim(name="Dealer", is_dealer=True)
sim_player = Blackjacksim(name="Player-1")
Blackjacksim.get_args()

def main():
    for game in range(Blackjacksim.Games):
        print("New Game!")
        print()

        #sim_player.set_bet_amount()

        sim_dealer.sim_deal_hand(1)
        print()

        sim_player.sim_deal_hand(dealer=sim_dealer)
        print()

        sim_dealer.sim_deal_hand()
        print()

        BlackJack.final_result(sim_player, sim_dealer)

        print(f"Final Results:\nDealer score: {sim_dealer.score}\n")
        if sim_player.move == "hit BlackJack":
            print(f"{sim_player.name} {sim_player.move}!")
        else:
            print(f"{sim_player.name} {sim_player.move} with {sim_player.score}!")

        sim_player.winning_amount()
        sim_player.status.append(sim_player.move)

        logger.info(f"\nGame-{game+1}\nPlayer cards: {sim_player.cards}\nPlayer score: {sim_player.score}")
        logger.info(f"Dealer cards: {sim_dealer.cards}\nDealer score: {sim_dealer.score}")
        logger.info(f"Status: {sim_player.move}")

        print(f"\nRunning count: {BlackJack.Live_Count:+}")
        print("Game Over!") 
        print('*' * 25)
        time.sleep(1)
        Blackjacksim.new_game(sim_player, sim_dealer)

    logging.info(f"\nRecords:\nWins = {sim_player.record['wins'] + sim_player.record['hit Blackjack']}\nLost = {sim_player.record['lost'] + sim_player.record['goes bust']}\nPush = {sim_player.record['push']}")
    logging.info(f"\nBlackjack = {sim_player.record['hit Blackjack']}\nBusted = {sim_player.record['goes bust']}\n")
    logging.info(f"Bankroll = {sim_player.bankroll}\nP&L = {sim_player.earnings}\n")
    logging.info(f"Status = {sim_player.status}\n")


if __name__ == "__main__":
    main()
