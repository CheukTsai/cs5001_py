class Card:
    """A playing card"""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        """Return a user friendly string for the card"""
        return self.value + " of " + self.suit

    def __repr__(self):
        """Return an informative string for debugging"""
        return (f"{self.__class__.__name__}"
                f"(suit: {self.suit}, value: {self.value})")

    def __eq__(self, other):
        """Return a boolean representing equality of the cards"""
        return (self.num_value() == other.num_value())

    def __lt__(self, other):
        """Return a boolean for the less than relationship"""
        return (self.num_value() < other.num_value())

    def __gt__(self, other):
        """Return a boolean for the greater than relationship"""
        return (self.num_value() > other.num_value())

    def __hash__(self):
        """Define the object's hash function so that
        the object can be used as a dictionary key"""
        return hash((self.suit, self.value))

    def num_value(self):
        """Return the numerical value for the card"""
        ACE_VALUE = 11
        FACE_CARD_VALUE = 10
        if self.value == "ace":
            return ACE_VALUE
        elif (self.value == "jack" or
              self.value == "queen" or
              self.value == "king"):
            return FACE_CARD_VALUE
        else:
            return int(self.value)
