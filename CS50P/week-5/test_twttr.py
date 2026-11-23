from twttr import shorten

def test_basic():
    assert shorten("hello") == "hll"
    assert shorten("Twitter") == "Twttr"



def test_uppercase():
    assert shorten("HELLO") == "HLL"
    assert shorten("APPLE") == "PPL"


def test_numbers():
    assert shorten("CS50") == "CS50"
    assert shorten("H3LL0") == "H3LL0"


def test_punctuation():
    assert shorten("hello, world!") == "hll, wrld!"


def test_no_vowels():
    assert shorten("rhythm") == "rhythm"

def test_empty_string():
    assert shorten("") == ""


