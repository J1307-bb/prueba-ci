# test_app.py
from app import greet

def test_greet():
    assert greet("World") == "Hello, World!"
    assert greet("GitHub Actions") == "Hello, GitHub Actions!"

def test_sumar():
    from app import sumar
    assert sumar(2, 3) == 5
    assert sumar(5, 7) == 12