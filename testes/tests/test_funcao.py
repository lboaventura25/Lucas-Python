from funcao import *

def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False

def test_is_odd():
    assert is_odd(2) is False
    assert is_odd(3) is True

def test_is_even_different_from_is_odd():
    assert is_even(2) != is_odd(2)
    assert is_even(3) != is_odd(3)

def test_sqrt():
    tol = 1e-6
    assert abs(sqrt(0)) < tol
    assert abs(sqrt(1) - 1) < tol
    assert abs(sqrt(2) - 1.4142135) < tol
    assert abs(sqrt(9) - 3) < tol

def test_fibo():
    assert fibo(5) == [0, 1, 1, 2, 3]
    assert fibo(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fibo(20) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

def test_is_prime():
    assert is_prime(11) == True
    assert is_prime(4) == False
    assert is_prime(41) == True
    assert is_prime(5) == True

def test_have_vowel():
    assert have_vowel("Nataliaei") == True
    assert have_vowel("Igor") == False
    assert have_vowel("Lucasaieou") == True
    assert have_vowel("Danielo") == False
    assert have_vowel("Lucas sssss ssss llll") == False
    assert have_vowel("Lucas fera mbfgh") == False

def test_squared_list():
    assert squared_list([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
    assert squared_list([10, 11, 12, 13, 14, 15]) == [100, 121, 144, 169, 196, 225]
    assert squared_list([5, 6, 7, 8]) == [25, 36, 49, 64]
    assert squared_list([0, 0, 1, 0, 1]) == [0, 0, 1, 0, 1]

def test_add_of_squared_list():
    assert add_of_squared_list([1, 2, 3, 4, 5]) == 55
    assert add_of_squared_list([10, 11, 12, 13, 14, 15]) == 955
    assert add_of_squared_list([5, 6, 7, 8]) == 174
    assert add_of_squared_list([0, 0, 1, 0, 1]) == 2

def test_check():
    assert check(10254, 8) == False
    assert check(18808, 8) == True
    assert check(10000, 1) == True
    assert check(225483, 3) == True
    assert check(99999, 9) == True
    assert check(212135, 4) == False

def test_popular_words():
    assert popular_words('When I was One I had just begun When I was Two I was nealy new', ['i', 'was', 'three', 'near'])  == {'i': 4, 'was': 3, 'three': 0, 'near': 0}
    assert popular_words('O Bruno esta doente', ['o', 'Bruno', 'joao', 'arthur'])  == {'o': 2, 'Bruno': 1, 'joao': 0, 'arthur': 0}

def test_find_message():
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
    assert find_message("hello world!") == ""
    assert find_message("Lucas Is so SmArT!!!!!") == "LISAT"

def test_checkio():
    assert checkio(1, 2, 3) == 2
    assert checkio(5, -5) == 10
    assert checkio(10.2, -2.2, 0, 1.1, 0.5) == 12.4
    assert checkio() == 0
    assert checkio(5, -5.5, 0, 6, 10, 20, 100, 50) == 105.5

def test_count_digits():
    assert count_digits(52648) == {5: 1, 2: 1, 6: 1, 4: 1, 8: 1}
    assert count_digits(10000) == {1: 1, 0: 4}
    assert count_digits(151551) == {5: 3, 1: 3}
    assert count_digits(9589985) == {5: 2, 9: 3, 8: 2}