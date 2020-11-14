from cipher_ajz2123 import __version__
from cipher_ajz2123 import cipher_ajz2123

def test_version():
    assert __version__ == '0.1.0'

def test_cipher():
    example = 'abc'
    shift = 5
    expected = 'def'
    actual = cipher_ajz2123.cipher(example, shift)
    assert actual == expected
