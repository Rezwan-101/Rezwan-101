from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("heLLo") == 0
    assert value("hello there") == 0


def test_h():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("how are you?") == 20
    assert value("hi there") == 20


def test_other():
    assert value("Good Morning") == 100
    assert value("What's Up?") == 100
    assert value("Welcome") == 100
    assert value("bye") == 100


