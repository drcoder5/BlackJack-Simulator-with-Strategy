''' 
BlackJack Player Guide
'''
import argparse
from strategy import strategy, strategy2
import itertools
import time

class BlackJack:
    ''' Create instances for every player '''

    BLACKJACK = 21
    Live_Count = 0
    Next_game = True
    Games = 0

    def __init__(self, name, is_dealer=False):
        self.name = name.capitalize()
        self.score = 0
        self.is_dealer = is_dealer
        self.cards = []
        self.has_ace = False
        self.move = None

    def hard_or_soft(self):
        ''' A function to get the needed datatype'''

        if self.has_ace:
            if not self.is_dealer:
                return tuple(["A",self.score - 11])
            else:
                return "A"
        else:
            return self.score


    def read_cards_and_get_score(self):
        ''' Gets the card numbers from input and calculates the corresponding score '''

        playing_cards = {
            "suits":["J","Q","K"],
            "ace":"A",
            "face_value":[x+1 for x in range(10)]
        }

        # Read cards(1)
        if self.__class__.__name__ == "BlackJack":
            literal_cards = input(f"Enter {self.name} cards: ").upper().split(" ")
        else:
            literal_cards = self.dealt_card()

        # Get score from cards(2)
        score = 0
        for card in literal_cards:
            if card in playing_cards["suits"]:
                score += 10
            elif card == playing_cards["ace"]:
                if card not in self.cards:
                    score += 11
                    self.has_ace = True
                else:
                    score += 1
            elif int(card) in playing_cards["face_value"]:
                score += int(card)
        self.score += score

        # Keep track of instance's dealt cards(3)
        for card in literal_cards:
            self.cards.append(card)

        # Reset Ace's value to 11 if going to bust(4)
        if self.has_ace and self.score > 21:
            self.score -= 10
            self.has_ace = False

        # Printing Scores and Cards(5)
        print(f"{self.name} score: {self.score}\n{self.name} cards: {self.cards}")
        # Keep a running count for all instances(6)
        print(f"Running count: {self.live_count(literal_cards):+}")


    def live_count(self, current_cards):
        ''' Count which depends on all the cards dealt on the table
        to see the worth of current session '''

        high = ["J","Q","K","A","10"]
        neutral = ["7","8","9"]
        low = ["2","3","4","5","6"]

        for card in current_cards:
            if card in high:
                BlackJack.Live_Count -= 1
            elif card in low:
                BlackJack.Live_Count += 1
            elif card in neutral:
                continue

        return BlackJack.Live_Count

    def is_bust(self):
        ''' Calculating win or loss or to keep going. '''

        blackjack_hands = ["A","J","Q","K","10"]
        if self.cards[0:2] in [list(x) for x in itertools.permutations(blackjack_hands, 2) if "A" in x]:
            self.move = "hit Blackjack"
            print(f"{self.name} {self.move}!")
            return True
        elif self.score > BlackJack.BLACKJACK:
            self.move = "goes bust"
            print(f"{self.name} {self.move}!")
            return True
        elif self.score == 21:
            self.move = "Stand"
            return True
        else:
            return False

    @staticmethod
    def new_game(players, dealer):
        ''' Clears score and cards in hand for next game. '''

        if input("Do you want to continue?(y/n) ").lower() == "y":
            for player in players:
                player.score = 0
                player.move = None
                player.cards.clear()
                player.has_ace = False

            dealer.score = 0
            dealer.move = None
            dealer.cards.clear()
            dealer.has_ace = False

        else:
            BlackJack.Next_game = False
            print("Game Over!")


    def next_action(self):
        ''' The move we made in the game '''

        move = input("Hit(H) or Stand(S) or Double(D)>> ").upper()
        if move == "S":
            self.move = "Stand"
        elif move == "D":
            self.move = "Double"
            print()
        else:
            self.move = "Hit"
            print()

    @classmethod
    def get_players_and_dealer(cls):
        ''' Get Number of players from args and instantiate players '''

        parser = argparse.ArgumentParser()
        parser.add_argument("-n", default=1, help="Number of Players at table", type=int)
        number_of_players = parser.parse_args().n
       #parser.add_argument("-r", default=10, help="Number of games to simulate", type=int)
       #BlackJack.Games = parser.parse_args().r

        dealer = cls(name="Dealer", is_dealer=True)

        players = []
        for i in range(number_of_players):
            players.append(cls(name=f"Player-{i+1}"))

        return dealer, players

    def deal_hand(self, the_dealer=None):
        ''' Simulating a player hand of Blackjack game'''

        while self.move != "Stand":
            self.read_cards_and_get_score()
            if self.is_bust():
                break
            else:
                if self.is_dealer:
                    if self.score >= 17:
                        self.move = "Stand"
                else:
                    if self.move == "Double Down":
                        self.move = "Stand"
                    else:
                        if self.__class__.__name__ == "BlackJack":
                            BlackJack.cheat_mode(self.hard_or_soft(), the_dealer.hard_or_soft())
                            self.next_action()
                        else:
                            self.move = BlackJack.cheat_mode(self.hard_or_soft(), the_dealer.hard_or_soft())


    # Can be abstracted into a standalone module
    @staticmethod
    def cheat_mode(player_hand, dealer_hand):
        '''Actual use of this script - Provides the appropriate action
        to play at the current score.'''

        if isinstance(player_hand, tuple):
            cheat_code = strategy2[str(dealer_hand)][player_hand]
            print(f"Play: {cheat_code}")
            return cheat_code
        else:
            if int(player_hand) > 17:
                print("Play: Stand")
                return "Stand"
            elif int(player_hand) < 8:
                print("Play: Hit")
                return "Hit"
            else:
                cheat_code = strategy[str(dealer_hand)][str(player_hand)]
                print(f"Play: {cheat_code}")
                return cheat_code

    @staticmethod
    def final_result(player, dealer):
        ''' Dealer vs Player '''

        if dealer.move == "goes bust":
            if player.move not in ("goes bust", "hit Blackjack"): 
                player.move = "wins"
        elif dealer.move == "hit Blackjack":
            if player.move == "hit Blackjack": 
                player.move = "push"
            else:
                player.move = "lost"

        # if player.move == dealer.move == "goes bust":
        #     player.move = "lost"
        # elif player.move == "goes bust":
        #     player.move = "lost"
        if player.move == "Stand":
            if 21 >= player.score > dealer.score :
                player.move = "wins"
            elif player.score == dealer.score:
                player.move = "push"
            else:
                player.move = "lost"


def main():
    ''' Main Workflow. '''

    print("Welcome to Classic BlackJack!")
    dealer, players = BlackJack.get_players_and_dealer()
    print(f"Players at table: {len(players)}")

    print(f"Running count: {BlackJack.Live_Count}\n")


    while BlackJack.Next_game:
        dealer.read_cards_and_get_score()
        print()

        for player in players:
            player.deal_hand(dealer)
            print()
        print()

        dealer.deal_hand()
        if dealer.move == "goes bust":
            for player in players:
                if player.move != "goes bust": 
                    player.move = "wins"
        elif dealer.move == "hit Blackjack":
            for player in players:
                if player.move != "hit Blackjack": 
                    player.move = "lost"
            
        print()

        for player in players:
            if player.move == dealer.move == "hit BlackJack":
                player.move = "push"
            elif player.move == dealer.move == "goes bust":
                player.move = "lost"
            elif player.move == "Stand":
                BlackJack.final_result(player, dealer)

        print(f"Final Results:\nDealer score: {dealer.score}\n")
        for player in players:
            if player.move == "hit BlackJack":
                print(f"{player.name} {player.move}!")
            else:
                print(f"{player.name} {player.move} with {player.score}!")

        print(f"\nRunning count: {BlackJack.Live_Count:+}")
        BlackJack.new_game(players, dealer)

if __name__ == "__main__":
    main()
