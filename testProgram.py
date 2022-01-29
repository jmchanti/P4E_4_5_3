import io
from random import randint
import random
from unittest.mock import Mock
import monkeyCalculator

def test_monkeyCalculator_noSmiles_prints_correct_result(capfd, monkeypatch):
    one = "n"
    two = "n"
    input = [one, two]
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    monkeyCalculator.calculateTime()

    out, err = capfd.readouterr()
    expected = "Uh Oh! We're in trouble!\n"
    assert out == expected
def test_monkeyCalculator_allSmiles_prints_correct_result(capfd, monkeypatch):
    one = "y"
    two = "y"
    input = [one, two]
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    monkeyCalculator.calculateTime()

    out, err = capfd.readouterr()
    expected = "Uh Oh! We're in trouble!\n"
    assert out == expected

def test_monkeyCalculator_firstSmiles_prints_correct_result(capfd, monkeypatch):
    one = "y"
    two = "n"
    input = [one, two]
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    monkeyCalculator.calculateTime()

    out, err = capfd.readouterr()
    expected = "Yay! We're going to have a good day!\n"
    assert out == expected
def test_monkeyCalculator_secondSmiles_prints_correct_result(capfd, monkeypatch):
    one = "n"
    two = "y"
    input = [one, two]
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    monkeyCalculator.calculateTime()

    out, err = capfd.readouterr()
    expected = "Yay! We're going to have a good day!\n"
    assert out == expected