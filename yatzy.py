class Yatzy:

    @staticmethod
    def chance(*dice):
        score = 0
        for die in dice:
            score+=die
        return score

    @staticmethod
    def yatzyScore(*dice):
        for die in dice:
            if die != dice[0]:
                return 0
        return 50
    
    @staticmethod
    def ones(*dice):
        score = 0
        for die in dice:
            if die==1:
                score+=die
        return score
    
    @staticmethod
    def twos(*dice):
        score = 0
        for die in dice:
            if die==2:
                score+=die
        return score
    
    @staticmethod
    def threes(*dice):
        score = 0
        for die in dice:
            if die==3:
                score+=die
        return score
    
    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5
    
    def fours(self):
        score = 0
        for die in self.dice:
            if die==4:
                score+=die
        return score
    
    def fives(self):
        score = 0
        for die in self.dice:
            if die==5:
                score+=die
        return score

    def sixs(self):
        score = 0
        for die in self.dice:
            if die==6:
                score+=die
        return score
    
    @staticmethod
    def score_pair(*dice):
        PAIR = 2
        for number in range(6,0,-1):
            if dice.count(number)>=PAIR:
                return PAIR * number
        return 0

    @staticmethod
    def two_pair(*dice):
        score = 0
        pairsFound = 0
        for number in range(1, 7):
            if pairsFound == 2:
                return score
            if dice.count(number) >= 4:
                return number * 4
            elif dice.count(number) >= 2:
                score += number * 2
                pairsFound += 1
        return 0
    
    @staticmethod
    def three_of_a_kind(*dice):
        THREE = 3
        for number in range(6,0,-1):
            if dice.count(number)>=THREE:
                return THREE * number
        return 0

    @staticmethod
    def four_of_a_kind(*dice):
        FOUR = 4
        for number in range(6,0,-1):
            if dice.count(number)>=FOUR:
                return FOUR * number
        return 0
    
    @staticmethod
    def small_straight(*dice):
        for number in range (1,6):
            if dice.count(number) != 1:
                return 0
        return 15

    @staticmethod
    def large_straight(*dice):
        for number in range (2,7):
            if dice.count(number) != 1:
                return 0
        return 20    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
