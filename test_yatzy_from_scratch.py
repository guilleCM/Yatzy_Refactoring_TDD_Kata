import pytest
from yatzy import Yatzy

# Chance
# The player scores the sum of all dice, no matter what they read.


def test_chance():
    # iterar sobre *args evita codigo cableado a 5 argumentos
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)


def test_yatzyScore():
    '''
    If all dice have the same number,
    the player scores 50 points. 
    For example:
        1,1,1,1,1 placed on "yatzy" scores 50
        1,1,1,2,1 placed on "yatzy
    '''
    assert 50 == Yatzy.yatzyScore(1, 1, 1, 1, 1)
    assert 0 == Yatzy.yatzyScore(1, 1, 1, 2, 1)


def test_ones():
    '''
    # Ones: 
    The player scores the sum of the dice that reads one.
    For Example:
    -   1,1,1,4,4 placed on "ones" scores 3 (1+1+1)
    '''
    assert 3 == Yatzy.ones(1, 1, 1, 4, 4)


def test_twos():
    '''
    # Twos: 
    The player scores the sum of the dice that reads two.
    For Example:
    -   2,2,2,4,4 placed on "twos" scores 6 (2+2+2)
    '''
    assert 6 == Yatzy.twos(2, 2, 2, 4, 4)


def test_threes():
    '''
    # Three: 
    The player scores the sum of the dice that reads three.
    For Example:
    -   2,2,3,3,3 placed on "threes" scores 9 (3+3+3)
    '''
    assert 9 == Yatzy.threes(2, 2, 3, 3, 3)


def test_score_pair():
    '''
    ### Pair: 
    The player scores the sum of the two highest matching dice.
    For example, when placed on "pair":
    -   3,3,3,4,4 scores 8 (4+4)
    -   1,1,6,2,6 scores 12 (6+6)
    -   3,3,3,4,1 scores 6 (3+3)
    -   3,3,3,3,1 scores 6 (3+3)
    '''
    assert 8 == Yatzy.score_pair(3, 3, 3, 4, 4)
    assert 12 == Yatzy.score_pair(1, 1, 6, 2, 6)
    assert 6 == Yatzy.score_pair(3, 3, 3, 4, 1)
    assert 6 == Yatzy.score_pair(3, 3, 3, 3, 1)


def test_two_pair():
    '''
    ### Two pairs: 
    If there are two pairs of dice with the same number, the
    player scores the sum of these dice. 
    For example, when placed on "two pairs":

    -   1,1,2,3,3 scores 8 (1+1+3+3)
    -   1,1,2,3,4 scores 0
    -   1,1,2,2,2 scores 6 (1+1+2+2)
    '''
    assert 8 == Yatzy.two_pair(1, 1, 2, 3, 3)
    assert 0 == Yatzy.two_pair(1, 1, 2, 3, 4)
    assert 6 == Yatzy.two_pair(1, 1, 2, 2, 2)


def test_three_of_a_kind():
    '''
    If there are three dice with the same number, the player
    scores the sum of these dice. 
    For example, when placed on "three of a kind": 
    -    3,3,3,4,5 scores 9 (3+3+3)
    -    3,3,4,5,6 scores 0
    -    3,3,3,3,1 scores 9 (3+3+3)
    '''
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 4, 5)
    assert 0 == Yatzy.three_of_a_kind(3, 3, 4, 5, 6)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 1)


def test_four_of_a_kind():
    '''
    If there are four dice with the same number, the player
    scores the sum of these dice. 
    For example, when placed on "four of a kind":
    -    2,2,2,2,5 scores 8 (2+2+2+2)
    -    2,2,2,5,5 scores 0
    -    2,2,2,2,2 scores 8 (2+2+2+2)
    '''
    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 5)
    assert 0 == Yatzy.four_of_a_kind(1, 1, 2, 3, 4)
    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 2)


def test_small_straight():
    '''
    When placed on "small straight", if the dice read
    "1,2,3,4,5" the player scores 15 (the sum of all the dice).
    -   1,2,3,4,5 scores 15 (1+2+3+4+5)
    '''
    assert 15 == Yatzy.small_straight(1, 2, 3, 4, 5)
    assert 15 == Yatzy.small_straight(5, 4, 3, 2, 1)
    assert 15 == Yatzy.small_straight(2, 1, 5, 4, 3)
    assert 0 == Yatzy.small_straight(4, 2, 3, 4, 5)


def test_large_straight():
    '''
    When placed on "large straight", if the dice read 2,3,4,5,6, 
    the player scores 20 (the sum of all the dice).
    -   2,3,4,5,6 scores 20 (2+3+4+5+6)
    '''
    assert 20 == Yatzy.large_straight(2, 3, 4, 5, 6)
    assert 20 == Yatzy.large_straight(6, 5, 4, 3, 2)
    assert 20 == Yatzy.large_straight(2, 3, 5, 6, 4)
    assert 0 == Yatzy.large_straight(3, 3, 4, 5, 6)


def test_full_house():
    '''
    If the dice are two of a kind and three of a kind, the
    player scores the sum of all the dice. 
    For example, when placed on "full house":
    -    1,1,2,2,2 scores 8 (1+1+2+2+2) 
    -    2,2,3,3,4 scores 0
    -    4,4,4,4,4 scores 0
    '''
    assert 8 == Yatzy.full_house(1, 1, 2, 2, 2)
    assert 0 == Yatzy.full_house(2, 2, 3, 3, 4)
    assert 0 == Yatzy.full_house(4, 4, 4, 4, 4)
    assert 11 == Yatzy.full_house(3, 3, 1, 1, 3)


@pytest.fixture
def inyector():
    # Es el setup de unittest o de JUnit
    tirada = Yatzy(1, 2, 3, 4, 5)
    return tirada


def test_fours(inyector):
    # Es necesario un objeto ya creado
    # No puedo testear con fixtures = inyeccion de dependencias
    # los metodos estaticos como chance()
    assert 4 == inyector.fours()


def test_fives(inyector):
    '''
    # Fives: 
    The player scores the sum of the dice that reads five.
    For Example:
    -   1,2,3,4,5 placed on "fives" scores 5 (5)
    '''
    assert 5 == inyector.fives()


def test_sixs(inyector):
    '''
    # Sixs: 
    The player scores the sum of the dice that reads six.
    For Example:
    -   1,2,3,4,5 placed on "sixs" scores 0 (0)
    '''
    assert 0 == inyector.sixs()
