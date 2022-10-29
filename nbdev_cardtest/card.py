# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_card.ipynb.

# %% auto 0
__all__ = ['Card']

# %% ../nbs/00_card.ipynb 10
class Card:
    "A playing card created by passing in `rank` from `ranks` and `suit` from `suits`"
    def __init__(self, 
                 suit:int, #An index into suits
                 rank:int): #An index into ranks
        self.suit,self.rank = suit,rank
    def __str__(self): return f"{ranks[self.rank]}{suits[self.suit]}"
    __repr__ = __str__
