from numtoword.numtoword import num_to_word


def test_get_1_show_one():
    assert "one" == num_to_word(1)


def test_get_2_show_two():
    assert "two" == num_to_word(2)


def test_get_3_show_three():
    assert "three" == num_to_word(3)


def test_get_4_show_four():
    assert "four" == num_to_word(4)


def test_get_5_show_five():
    assert "five" == num_to_word(5)


def test_get_6_show_six():
    assert "six" == num_to_word(6)

def test_get_100_show_hundred():
    assert "onehundred" == num_to_word(100)

def test_1234():
    assert "onethousandtwohundredthirtyfour" == num_to_word(1234)

def test_200():
    assert "twohundred" == num_to_word(200)
    
def test_300():
    assert "threehundred" == num_to_word(300)

def test_2000():
    assert "twothousand" == num_to_word(2000)
