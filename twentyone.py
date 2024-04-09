import random
_cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def _next_card():
    return random.choice(_cards)

def _hand_total(hand):
     """
     This function calculates the sum of two cards. The cards are represented as a list of two elements.
     Cards from 2 to 10 are represented by their respective numbers. J, Q, K, A are represented as 'J', 'Q', 'K', 'A'.
     'J' is treated as 11, 'Q' as 12, 'K' as 13 and 'A' as 1.
     """
     # Create a dictionary to map face cards to their respective numerical values
     face_cards = {'J': 11, 'Q': 12, 'K': 13, 'A': 1}
 
     # Initialize sum to 0
     sum_of_cards = 0
 
     # Iterate over each card in the hand
     for card in hand:
         # If the card is a face card (J, Q, K, A), add the corresponding numerical value to the sum
         if card in face_cards:
             sum_of_cards += int(face_cards[card])
         # If the card is a number card (2-10), add its value to the sum
         else:
             sum_of_cards += int(card)
     print(f"sum of cards is {sum_of_cards}")
     return sum_of_cards


class Dealer:
   def __init__(self):
      self.hand = []

   def new_round(self):
      self.hand = [_next_card(), _next_card()]
      print(self.hand)

   def get_hand_total(self):
    return _hand_total(self.hand)




