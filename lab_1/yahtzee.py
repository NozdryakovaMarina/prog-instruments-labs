from typing import List


class Yahtzee:
    @staticmethod
    def chance(dice1: int, dice2: int, dice3: int, dice4: int, dice5: int) -> int:
        total: int = 0
        total += dice1
        total += dice2
        total += dice3
        total += dice4
        total += dice5

        return total

    @staticmethod
    def yahtzee(dice: List[int]) -> int:
        counts = [0] * (len(dice) + 1)

        for i in dice:
            counts[i - 1] += 1

        for i in range(len(counts)):
            if counts[i] == 5:
                return 50

        return 0
    
    @staticmethod
    def ones(dice1: int, dice2: int, dice3: int, dice4: int, dice5: int) -> int:
        score: int = 0
        if (dice1 == 1):
            score += 1
        if (dice2 == 1):
            score += 1
        if (dice3 == 1):
            score += 1
        if (dice4 == 1):
            score += 1
        if (dice5 == 1): 
            score += 1

        return score
    
    @staticmethod
    def twos(dice1: int, dice2: int, dice3: int, dice4: int, dice5: int) -> int:
        score: int = 0
        if (dice1 == 2):
            score += 2
        if (dice2 == 2):
            score += 2
        if (dice3 == 2):
            score += 2
        if (dice4 == 2):
            score += 2
        if (dice5 == 2):
            score += 2

        return score
    
    @staticmethod
    def threes(dice1: int, dice2: int, dice3: int, dice4: int, dice5: int) -> int:
        score: int = 0
        if (dice1 == 3):
            score += 3
        if (dice2 == 3):
            score += 3
        if (dice3 == 3):
            score += 3
        if (dice4 == 3):
            score += 3
        if (dice5 == 3):
            score += 3

        return score
    
    def __init__(self, dice1: int, dice2: int, dice3: int, dice4: int, dice5: int) -> None:
        self.dice: List[int] = [0] * 5
        self.dice[0] = dice1
        self.dice[1] = dice2
        self.dice[2] = dice3
        self.dice[3] = dice4
        self.dice[4] = dice5
    
    def fours(self) -> int:
        score: int = 0
        for i in range(5):
            if (self.dice[i] == 4): 
                score += 4
        return score
    
    def fives(self) -> int:
        score: int = 0
        for i in range(len(self.dice)): 
            if (self.dice[i] == 5):
                score = score + 5
        return score
    
    def sixes(self) -> int:
        score: int = 0
        for i in range(len(self.dice)): 
            if (self.dice[i] == 6):
                score = score + 6
        return score
    
    @staticmethod
    def one_pair(dice1: int, dice2: int, dice3: int, dice4: int, dice5: int) -> None:
        counts: List[int] = [0] * 6
        counts[dice1 - 1] += 1
        counts[dice2 - 1] += 1
        counts[dice3 - 1] += 1
        counts[dice4 - 1] += 1
        counts[dice5 - 1] += 1

        for i in range(6):
            if (counts[6 - i - 1] == 2):
                return (6 - i) * 2

        return 0
    
    @staticmethod
    def two_pair(dice1: int, dice2: int, dice3: int, dice4: int, dice5: int) -> int:
        counts: List[int] = [0] * 6
        counts[dice1 - 1] += 1
        counts[dice2 - 1] += 1
        counts[dice3 - 1] += 1
        counts[dice4 - 1] += 1
        counts[dice5 - 1] += 1

        n: int = 0
        score: int = 0
        for i in range(6):
            if (counts[6 - i - 1] == 2):
                n = n + 1
                score += (6 - i)

        if (n == 2):
            return score * 2
        else:
            return 0
    
    @staticmethod
    def four_of_a_kind(dice1: int, dice2: int, dice3: int, dice4: int, dice5: int) -> int:
        tallies: List[int] = [0] * 6
        tallies[dice1 - 1] += 1
        tallies[dice2 - 1] += 1
        tallies[dice3 - 1] += 1
        tallies[dice4 - 1] += 1
        tallies[dice5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 4):
                return (i + 1) * 4

        return 0
    
    @staticmethod
    def three_of_a_kind(dice1: int, dice2: int, dice3: int, dice4: int, dice5: int) -> int:
        tallies: List[int] = [0] * 6
        tallies[dice1 - 1] += 1
        tallies[dice2 - 1] += 1
        tallies[dice3 - 1] += 1
        tallies[dice4 - 1] += 1
        tallies[dice5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 3):
                return (i + 1) * 3

        return 0
    
    @staticmethod
    def small_straight(dice1: int, dice2: int, dice3: int, dice4: int, dice5: int) -> int:
        tallies: List[int] = [0] * 6
        tallies[dice1 - 1] += 1
        tallies[dice2 - 1] += 1
        tallies[dice3 - 1] += 1
        tallies[dice4 - 1] += 1
        tallies[dice5 - 1] += 1

        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15

        return 0
    
    @staticmethod
    def large_straight(dice1: int, dice2: int, dice3: int, dice4: int, dice5: int) -> int:
        tallies: List[int] = [0] * 6
        tallies[dice1 - 1] += 1
        tallies[dice2 - 1] += 1
        tallies[dice3 - 1] += 1
        tallies[dice4 - 1] += 1
        tallies[dice5 - 1] += 1

        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1 and 
            tallies[5] == 1):
            return 20

        return 0

    @staticmethod
    def full_house(dice1: int, dice2: int, dice3: int, dice4: int, dice5: int) -> int: 
        has_pair = False 
        pair_value = 0
        has_triplet = False
        triplet_value = 0

        tallies: List[int] = [0] * 6
        tallies[dice1 - 1] += 1
        tallies[dice2 - 1] += 1
        tallies[dice3 - 1] += 1
        tallies[dice4 - 1] += 1
        tallies[dice5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                has_pair = True
                pair_value = i + 1

        for i in range(6):
            if (tallies[i] == 3): 
                has_triplet = True
                triplet_value = i + 1

        if (has_pair and has_triplet):
            return pair_value * 2 + triplet_value * 3
        else:
            return 0