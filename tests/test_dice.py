from unittest.mock import patch
from dndgame.dice import roll, roll_with_advantage, roll_with_disadvantage


def test_roll():
    """Test basic dice rolling with mocked random values."""
    with patch(
        "random.randint", return_value=4
    ):  # random.randint will return 4 when called in this context
        result = roll(6, 1)
        assert result == 4

    with patch(
        "random.randint", return_value=3
    ):  # random.randint will return 3 when called in this context
        result = roll(20, 2)
        assert result == 6  # 3 + 3 = 6

    with patch(
        "random.randint", side_effect=[1, 2]
    ):  # random.randint will first return 1, then 2 when called in this context
        result = roll(6, 1)
        assert result == 1

        result = roll(20, 1)
        assert result == 2


def test_roll_with_advantage():
    """Test advantage rolls (take highest of two)."""
    with patch(
        "random.randint", side_effect=[3, 5]
    ):  # random.randint will first return 3, then 5 when called in this context
        result = roll_with_advantage(20)
        assert result == 5  # 5 is the highest of the two rolls

    with patch(
        "random.randint", side_effect=[6, 2]
    ):  # random.randint will first return 6, then 2 when called in this context
        result = roll_with_advantage(6)
        assert result == 6  # 6 is the highest of the two rolls


def test_roll_with_disadvantage():
    """Test disadvantage rolls (take lowest of two)."""
    with patch(
        "random.randint", side_effect=[3, 5]
    ):  # random.randint will first return 3, then 5 when called in this context
        result = roll_with_disadvantage(20)
        assert result == 3  # 3 is the lowest of the two rolls

    with patch(
        "random.randint", side_effect=[6, 2]
    ):  # random.randint will first return 6, then 2 when called in this context
        result = roll_with_disadvantage(6)
        assert result == 2  # 2 is the lowest of the two rolls
