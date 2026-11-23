from plates import is_valid

def test_valid_plates():
    assert is_valid("cs50") == True
    assert is_valid("AAA222") == True
    assert is_valid("AB") == True
    assert is_valid("ABC123") == True


def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFGH") == False
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True

def test_first_two_letters():
    assert is_valid("1ABC") == False
    assert is_valid("A1") == False
    assert is_valid("AB12") == True

def test_invalid_characters():
    assert is_valid("PI3.14") == False
    assert is_valid("CS-50") == False
    assert is_valid("CS 50") == False
    assert is_valid("AB@12") == False

def test_numbers():
    assert is_valid("CS05") == False
    assert is_valid("CS0") == False
    assert is_valid("CS50") == True
    assert is_valid("AB123") == True
    assert is_valid("AB12CD") == False
    assert is_valid("ABC") == True



