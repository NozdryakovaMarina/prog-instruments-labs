from typing import List


class Yahtzee:
    """
    This class is used to represent the Yahtzee game and the scoring methods in it.

     Static Methods
    --------------
    chance(dice1, dice2, dice3, dice4, dice5)
        Returns the total score of the given dice.

    yahtzee(dice)
        Returns the score for a Yahtzee (all five dice are the same).

    ones(dice1, dice2, dice3, dice4, dice5)
        Returns the score for ones in the given dice.

    twos(dice1, dice2, dice3, dice4, dice5)
        Returns the score for twos in the given dice.

    threes(dice1, dice2, dice3, dice4, dice5)
        Returns the score for threes in the given dice.

    one_pair(dice1, dice2, dice3, dice4, dice5)
        Returns the score for one pair in the given dice.

    two_pair(dice1, dice2, dice3, dice4, dice5)
        Returns the score for two pairs in the given dice.

    four_of_a_kind(dice1, dice2, dice3, dice4, dice5)
        Returns the score for four of a kind in the given dice.

    Instance Methods
    ----------------
    __init__(dice1, dice2, dice3, dice4, dice5)
        Initializing the dice for the instance.

    fours()
        Returns the score for fours in the given dice.

    fives()
        Returns the score for fives in the given dice.

    sixes()
        Returns the score for sixes in the given dice.
    """
    
    @staticmethod
    def chance(dice1: int, dice2: int, dice3: int, dice4: int, dice5: int) -> int:
        """
        This method calculates the sum of the given dice.

        Parametrs:
        -----------
        dice1, dice2, dice3, dice4, dice5: int
            Values of the five dice rolls.

        Returns:
        --------
        total: int
            Total score of the given dice.
        """
        total: int = 0
        total += dice1
        total += dice2
        total += dice3
        total += dice4
        total += dice5

        return total

    @staticmethod
    def yahtzee(dice: List[int]) -> int:
        """
        This method calculates the score for a Yahtzee (all five dice are the same).

        Parametrs:
        -----------
        dice : List[int]
            List of dice values rolls.

        Returns:
        --------
        int
            Score for a Yahtzee or 0 if not all five dice are the same. Otherwise 50.
        """
        counts = [0] * (len(dice) + 1)

        for i in dice:
            counts[i - 1] += 1

        for i in range(len(counts)):
            if counts[i] == 5:
                return 50

        return 0
    
    @staticmethod
    def ones(dice1: int, dice2: int, dice3: int, dice4: int, dice5: int) -> int:
        """
        This method calculates the sum of the dice showing ones.

        Parametrs:
        -----------
        dice1, dice2, dice3, dice4, dice5: int
            Values of the five dice rolls.

        Returns:
        --------
        score: int
            Score for ones in the given dice.
        """
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
        """
        This method calculates the sum of the dice showing twos.

        Parametrs:
        -----------
        dice1, dice2, dice3, dice4, dice5: int
            Values of the five dice rolls.

        Returns:
        --------
        score: int
            Score for twos in the given dice.
        """
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
        """
        This method calculates the sum of the dice showing threes.

        Parametrs:
        -----------
        dice1, dice2, dice3, dice4, dice5: int
            Values of the five dice rolls.

        Returns:
        --------
        score: int
            Score for threes in the given dice.
        """
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
        """
        Initializing the dice for the instance.

        Parametrs:
        -----------
        dice1, dice2, dice3, dice4, dice5: int
            Values of the five dice rolls.

        Returns:
        --------
        None
        """
        self.dice: List[int] = [0] * 5
        self.dice[0] = dice1
        self.dice[1] = dice2
        self.dice[2] = dice3
        self.dice[3] = dice4
        self.dice[4] = dice5
    
    def fours(self) -> int:
        """
        This method calculates the sum of the dice showing fours.

        Returns:
        --------
        score: int
            Score for fours in the given dice.
        """
        score: int = 0
        for i in range(5):
            if (self.dice[i] == 4): 
                score += 4
        return score
    
    def fives(self) -> int:
        """
        This method calculates the sum of the dice showing fives.

        Returns:
        --------
        score: int
            Score for fives in the given dice.
        """
        score: int = 0
        for i in range(len(self.dice)): 
            if (self.dice[i] == 5):
                score = score + 5
        return score
    
    def sixes(self) -> int:
        """
        This method calculates the sum of the dice showing sixes.

        Returns:
        --------
        score: int
            Score for sixes in the given dice.
        """
        score: int = 0
        for i in range(len(self.dice)): 
            if (self.dice[i] == 6):
                score = score + 6
        return score
    
    @staticmethod
    def one_pair(dice1: int, dice2: int, dice3: int, dice4: int, dice5: int) -> int:
        """
        This method calculates the score for one pair in the given dice.

        Parametrs:
        -----------
        dice1, dice2, dice3, dice4, dice5: int
            Values of the five dice rolls.

        Returns:
        --------
        int
            Score for one pair in the given dice or 0 if no pair found.
        """
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
        """
        This method calculates the score for two pairs in the given dice.

        Parameters:
        -----------
        dice1, dice2, dice3, dice4, dice5: int
            Values of the five dice rolls.

        Returns:
        --------
        int
            Score for two pairs in the given dice or 0 if no two pairs found.
        """
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
        """
        This method calculates the score for four of a kind in the given dice.

        Parameters:
        -----------
        dice1, dice2, dice3, dice4, dice5: int
            Values of the five dice rolls.

        Returns:
        --------
        int
            Score for four of a kind in the given dice or 0 if no four of a kind found.
        """
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
        """
        This method calculates the score for three of a kind in the given dice.

        Parameters:
        -----------
        dice1, dice2, dice3, dice4, dice5: int
            Values of the five dice rolls.

        Returns:
        --------
        int
            Score for three of a kind in the given dice or 0 if no three of a kind found.
        """
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
        """
        This method determines whether there is a small sequence (1-2-3-4-5) 
        in the given dice roll results.

        Parameters:
        -----------
        dice1, dice2, dice3, dice4, dice5: int
            Values of the five dice rolls.

        Returns:
        --------
        int
            15 if a small sequence is present. Otherwise 0.
        """
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
        """
        This method determines whether there is a large sequence (2-3-4-5-6) 
        in the given dice roll results.

        Parameters:
        -----------
        dice1, dice2, dice3, dice4, dice5: int
            Values of the five dice rolls.

        Returns:
        --------
        int
            20 if a large sequence is present. Otherwise 0
        """
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
        """
        This method determines whether there is a full house combination 
        (one pair and one three) in the given dice roll results.

        Parameters:
        -----------
        dice1, dice2, dice3, dice4, dice5: int
            Values of the five dice rolls.

        Returns:
        --------
        int
            The sum of the points for the full house combination. Otherwise 0.
        """
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