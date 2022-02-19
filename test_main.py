import pytest
from main import pairs_of_players

def test_pairs_of_players():
    assert pairs_of_players(139) == "- Brevin Knight    Nate Robinson\n- Nate Robinson    Mike Wilks\n"