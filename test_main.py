import pytest
from main import pairs_of_players

def _testing_pairs_of_players(my_dict,expected):
    comparision = [(i in expected.items() or i in dict((y,x) for x,y in expected.items()).items()) for i in my_dict.items()]
    if all(comparision) and (len(comparision) == len(my_dict)) and (len(comparision) == len(expected)):
        return(True)
    else:
        return(False)

def test_pairs_of_players():
    assert _testing_pairs_of_players(my_dict = pairs_of_players(139), expected = {"Brevin Knight":"Nate Robinson", "Nate Robinson":"Mike Wilks"}) == True