from nfe_parser.money import brl
def test_round():
    assert str(brl('10.555')) == '10.56'
