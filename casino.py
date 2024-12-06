import random
import tkinter as tk
from PIL import Image, ImageTk

# Blackjack Class for Card Data
class Blackjack:
    def __init__(self):
        self._dictionary = {
            "2H": {"image": "cards/2_of_hearts.png", "color": "red", "value": 2},
            "2D": {"image": "cards/2_of_diamonds.png", "color": "red", "value": 2},
            "2S": {"image": "cards/2_of_spades.png", "color": "black", "value": 2},
            "2C": {"image": "cards/2_of_clubs.png", "color": "black", "value": 2},
            "3H": {"image": "cards/3_of_hearts.png", "color": "red", "value": 3},
            "3D": {"image": "cards/3_of_diamonds.png", "color": "red", "value": 3},
            "3S": {"image": "cards/3_of_spades.png", "color": "black", "value": 3},
            "3C": {"image": "cards/3_of_clubs.png", "color": "black", "value": 3},
            "4H": {"image": "cards/4_of_hearts.png", "color": "red", "value": 4},
            "4D": {"image": "cards/4_of_diamonds.png", "color": "red", "value": 4},
            "4S": {"image": "cards/4_of_spades.png", "color": "black", "value": 4},
            "4C": {"image": "cards/4_of_clubs.png", "color": "black", "value": 4},
            "5H": {"image": "cards/5_of_hearts.png", "color": "red", "value": 5},
            "5D": {"image": "cards/5_of_diamonds.png", "color": "red", "value": 5},
            "5S": {"image": "cards/5_of_spades.png", "color": "black", "value": 5},
            "5C": {"image": "cards/5_of_clubs.png", "color": "black", "value": 5},
            "6H": {"image": "cards/6_of_hearts.png", "color": "red", "value": 6},
            "6D": {"image": "cards/6_of_diamonds.png", "color": "red", "value": 6},
            "6S": {"image": "cards/6_of_spades.png", "color": "black", "value": 6},
            "6C": {"image": "cards/6_of_clubs.png", "color": "black", "value": 6},
            "7H": {"image": "cards/7_of_hearts.png", "color": "red", "value": 7},
            "7D": {"image": "cards/7_of_diamonds.png", "color": "red", "value": 7},
            "7S": {"image": "cards/7_of_spades.png", "color": "black", "value": 7},
            "7C": {"image": "cards/7_of_clubs.png", "color": "black", "value": 7},
            "8H": {"image": "cards/8_of_hearts.png", "color": "red", "value": 8},
            "8D": {"image": "cards/8_of_diamonds.png", "color": "red", "value": 8},
            "8S": {"image": "cards/8_of_spades.png", "color": "black", "value": 8},
            "8C": {"image": "cards/8_of_clubs.png", "color": "black", "value": 8},
            "9H": {"image": "cards/9_of_hearts.png", "color": "red", "value": 9},
            "9D": {"image": "cards/9_of_diamonds.png", "color": "red", "value": 9},
            "9S": {"image": "cards/9_of_spades.png", "color": "black", "value": 9},
            "9C": {"image": "cards/9_of_clubs.png", "color": "black", "value": 9},
            "1H": {"image": "cards/10_of_hearts.png", "color": "red", "value": 10},
            "1D": {"image": "cards/10_of_diamonds.png", "color": "red", "value": 10},
            "1S": {"image": "cards/10_of_spades.png", "color": "black", "value": 10},
            "1C": {"image": "cards/10_of_clubs.png", "color": "black", "value": 10},
            "JH": {"image": "cards/jack_of_hearts2.png", "color": "red", "value": 10},
            "JD": {"image": "cards/jack_of_diamonds2.png", "color": "red", "value": 10},
            "JS": {"image": "cards/jack_of_spades2.png", "color": "black", "value": 10},
            "JC": {"image": "cards/jack_of_clubs2.png", "color": "black", "value": 10},
            "QH": {"image": "cards/queen_of_hearts2.png", "color": "red", "value": 10},
            "QD": {"image": "cards/queen_of_diamonds2.png", "color": "red", "value": 10},
            "QS": {"image": "cards/queen_of_spades2.png", "color": "black", "value": 10},
            "QC": {"image": "cards/queen_of_clubs2.png", "color": "black", "value": 10},
            "KH": {"image": "cards/king_of_hearts2.png", "color": "red", "value": 10},
            "KD": {"image": "cards/king_of_diamonds2.png", "color": "red", "value": 10},
            "KS": {"image": "cards/king_of_spades2.png", "color": "black", "value": 10},
            "KC": {"image": "cards/king_of_clubs2.png", "color": "black", "value": 10},
            "AH": {"image": "cards/ace_of_hearts.png", "color": "red", "value": 11},
            "AD": {"image": "cards/ace_of_diamonds.png", "color": "red", "value": 11},
            "AS": {"image": "cards/ace_of_spades2.png", "color": "black", "value": 11},
            "AC": {"image": "cards/ace_of_clubs.png", "color": "black", "value": 11}
        }

        self.deck = list(self._dictionary.keys())
        random.shuffle(self.deck)

    def deal_card(self):
        # Deal a single card from the deck.
        return self.deck.pop() if self.deck else None

    def get_card_info(self, key):
        # Get card details using its key.
        return self._dictionary[key]

# GUI Class for Display
class GUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Casino")
        self.window.attributes("-fullscreen", True)
        self.blackjack = Blackjack()  # Initialize Blackjack
        self.player_hand = []
        self.dealer_hand = []
        self.score = 0
        self.mainScreen()

    def mainScreen(self):
        # Clear current screen
        self.clear()

        # Add main screen content
        frame = tk.Frame(self.window)
        frame.grid()

        tk.Label(frame, text="Welcome to the Casino!", font=("Arial", 24)).grid(column=0, row=0)
        tk.Button(frame, text="Game Menu", command=self.gameSelector, width=20).grid(column=0, row=1, padx=20, pady=20)

    def gameSelector(self):
        # Clear current screen
        self.clear()

        # Add game selector content
        frame = tk.Frame(self.window)
        frame.grid()

        image = Image.open("blackjack.png").resize((300, 300))  # Replace with your image path
        photo = ImageTk.PhotoImage(image)

        tk.Label(frame, text="Select a Game", font=("Arial", 18)).grid(column=0, row=0)
        tk.Button(frame, text="Back", command=self.mainScreen, width=15).grid(column=0, row=1, padx=10, pady=10)
        tk.Label(frame, text="Blackjack", font=("Arial", 18)).grid(column=0, row=2)
        # Create a square button
        button = tk.Button(
            frame,
            text=" ",  # Empty text or space to avoid resizing
            command=self.startBlackjack,
            image=photo,
            width=300,  # Set width in pixels (matches image size)
            height=300  # Set height in pixels (matches image size)
        )
        button.image = photo  # Keep a reference to avoid garbage collection
        button.grid(column=0, row=2, padx=10, pady=10)

    def startBlackjack(self):
        # Initialize Blackjack hands and screen
        self.clear()
        self.player_hand = [self.blackjack.deal_card(), self.blackjack.deal_card()]
        self.dealer_hand = [self.blackjack.deal_card(), self.blackjack.deal_card()]

        self.blackjackFrame()

    def blackjackFrame(self):
        # Display Blackjack game
        self.clear()
        frame = tk.Frame(self.window)
        frame.grid()
        img = Image.open("cards/back_of_card.png")
        img = img.resize((100, 150))
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(frame, image=photo)
        label.image = photo
        label.grid(column=0, row=5, padx=5)

        # Score
        tk.Label(frame, text=f"Score : {self.score}", font=("Arial", 14)).grid(column=1, row=0, pady=10)

        # Display player's hand
        tk.Label(frame, text="Your Hand", font=("Arial", 18)).grid(column=0, row=2, pady=10)
        self.display_hand(frame, self.player_hand, 3)

        # Display dealer's hand (hide one card)
        tk.Label(frame, text="Dealer's Hand", font=("Arial", 18)).grid(column=0, row=0, pady=10)
        self.display_hand(frame, self.dealer_hand, 1, hide_first=True)

        # Player options
        tk.Button(frame, text="Hit", command=self.playerHit, width=10).grid(column=0, row=4, pady=10)
        tk.Button(frame, text="Stand", command=self.dealerTurn, width=10).grid(column=1, row=4, pady=10)
        
        cards_remain = self.cards_remaining()
        tk.Label(frame, text=f"Cards Remaining: {cards_remain}", font=("Arial", 14)).grid(column=1, row=5, pady=10)

        player_value = self.calculate_hand_value(self.player_hand)
        tk.Label(frame, text=f"Value: {player_value}", font=("Arial", 14)).grid(column=1, row=2, pady=10)

        # stops blackjack
        if cards_remain < 45 and self.score <= 300:
            self.clear()
            # Restart screen
            self.restart()
        elif self.score >= 300:
            self.clear()
            # Next screen : Bomb defusal screen


    def display_hand(self, frame, hand, row, hide_first=False):
        # Display a hand of cards.
        for i, card_key in enumerate(hand):
            card = self.blackjack.get_card_info(card_key)
            if hide_first and i == 0:
                img = Image.open("cards/back_of_card.png")  # Placeholder for hidden card
            else:
                img = Image.open(card["image"])
            img = img.resize((100, 150))
            photo = ImageTk.PhotoImage(img)
            label = tk.Label(frame, image=photo)
            label.image = photo
            label.grid(column=i, row=row, padx=5)

    def playerHit(self):
        # Handle player hitting.
        self.player_hand.append(self.blackjack.deal_card())
        if self.calculate_hand_value(self.player_hand) > 21:
            self.endGame("Dealer Wins! You Busted!")
        else:
            self.blackjackFrame()

    def dealerTurn(self):
        # Handle dealer's turn.
        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.blackjack.deal_card())
        self.determine_winner()

    def calculate_hand_value(self, hand):
        # Calculate the total value of a hand.
        value = 0
        aces = 0
        for card_key in hand:
            card = self.blackjack.get_card_info(card_key)
            value += card["value"]
            if card["value"] == 11:  # Ace
                aces += 1

        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def determine_winner(self):
        # Determine the winner.
        player_value = self.calculate_hand_value(self.player_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        if dealer_value > 21:
            self.endGame("You Win! Dealer Busted!")
            self.score += 100
        elif player_value > dealer_value:
            self.endGame("You Win!")
            self.score += 100
        elif player_value < dealer_value:
            self.endGame("Dealer Wins!")
            self.score -= 50
        else:
            self.endGame("It's a Draw!")
            self.score += 50

    def cards_remaining(self):
        return len(self.blackjack.deck)

    def endGame(self, message):
        #End the game and display the result.
        self.clear()
        tk.Label(self.window, text=message, font=("Arial", 24)).pack(pady=20)
        tk.Button(self.window, text="Play Again", command=self.startBlackjack).pack(pady=10)

    def restart(self):
        # Buttons
        tk.Label(self.window, text="Dealer wins!\n\nDefeat the dealer to defuse the Bomb!", font=("Arial", 24)).pack(pady=20)
        tk.Button(self.window, text="Back to Menu", command=self.gameSelector, width=20).pack(pady=20)


    def clear(self):
        # Clear the window.
        for widget in self.window.winfo_children():
            widget.destroy()

# MAIN PROGRAM
window = tk.Tk()
app = GUI(window)
window.mainloop()
