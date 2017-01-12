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
    assert 50 == Yatzy.yatzyScore(1,1,1,1,1)
    assert 0 == Yatzy.yatzyScore(1,1,1,2,1)

def test_ones():
    '''
    # Ones: 
    The player scores the sum of the dice that reads one.
    For Example:
    -   1,1,1,4,4 placed on "ones" scores 3 (1+1+1)
    '''
    assert 3 == Yatzy.ones(1,1,1,4,4)

def test_twos():
    '''
    # Twos: 
    The player scores the sum of the dice that reads two.
    For Example:
    -   2,2,2,4,4 placed on "twos" scores 6 (2+2+2)
    '''
    assert 6 == Yatzy.twos(2,2,2,4,4)

def test_threes():
    '''
    # Three: 
    The player scores the sum of the dice that reads three.
    For Example:
    -   2,2,3,3,3 placed on "threes" scores 9 (3+3+3)
    '''
    assert 9 == Yatzy.threes(2,2,3,3,3)


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
