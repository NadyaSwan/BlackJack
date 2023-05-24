from Deck import Deck
from constants import  values


class Game:
    def __init__(self):
        deck = Deck()

        self.shuffled_deck = deck.get_shuffled_deck()
        self.dealer_cards = []
        self.player_cards = []
        self.players_count = 0
        self.bet = 0
        self.balance = 100

    def make_bet(self):
        while True:
            try:
                current_bet = int(input('Please make your bet: '))
            except:
                print('Given input is not a number. Please try again')
            else:
                while current_bet > self.balance:
                    print(f'Your bet exceeds current balance {self.balance}. Access closed')
                    try:
                        current_bet = int(input('Please make your bet: '))
                    except:
                        print('Given input is not a number. Please try again')
                    else:
                        break

                self.bet = current_bet
                print(f'Your bet {self.bet} accepted. Your current balance is {self.balance}')
                break

    def get_first_pair(self):
        self.dealer_cards.append(self.shuffled_deck.pop(0))
        self.dealer_cards.append(self.shuffled_deck.pop(0))

        self.player_cards.append(self.shuffled_deck.pop(0))
        self.player_cards.append(self.shuffled_deck.pop(0))

        self.players_count = values[self.player_cards[0].rank] + values[self.player_cards[1].rank]

        print(f'Here is a dealer card: {self.dealer_cards[0]}. Another one will be discovered on last move')
        print(f'Here are your two cards: {self.player_cards[0]} and {self.player_cards[1]}')
        print(f'Your current total is {self.players_count}')

    def give_card(self):
        new_card = self.shuffled_deck.pop(0)
        self.player_cards.append(new_card)
        self.players_count += values[self.player_cards[-1].rank]

        print(f'Here is one more card: {new_card}')
        print(f'Your current total is {self.players_count}')

    def check_winner(self):
        dealers_count = values[self.dealer_cards[0].rank] + values[self.dealer_cards[1].rank]

        print(f'Dealers second card is {self.dealer_cards[1]}')

        while dealers_count < 17:
            self.dealer_cards.append(self.shuffled_deck.pop(0))
            dealers_count += values[self.dealer_cards[-1].rank]
            print(f'Dealer takes a card {self.dealer_cards[-1]}. His total count is {dealers_count}')

        print(f'Dealer finished his move. His total count is {dealers_count}')

        if dealers_count > 21:
            self.balance += self.bet
            print(f'Dealer is busted. Player won. You current balance is {self.balance}')

        else:
            if dealers_count > self.players_count:
                self.balance -= self.bet
                print(f'Dealer is a winner. You lost your bet {self.bet}. Your current balance is {self.balance}')

            elif dealers_count == self.players_count:
                print(f'It is a tie!')
            else:
                self.balance += self.bet
                print(f'You are a winner. You won your bet {self.bet}. Your current balance is {self.balance}')

    def play(self):
        print(f'Hello, player. Please make your bet. Your current balance is {self.balance}')
        self.make_bet()
        self.get_first_pair()

        while True:
            one_more_card = input('Do you want one more card? (Y/N)')

            if one_more_card == 'N':
                self.check_winner()
                break

            self.give_card()

            if self.players_count > 21:
                self.balance -= self.bet
                print(f'You are busted. You lost your bet {self.bet}. Your current balance is {self.balance}')
                break
