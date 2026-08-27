from jar import Jar
import pytest 

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar1=Jar(10)
    assert jar1.capacity == 10 

    with pytest.raises(ValueError):
        Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(-10)
    with pytest.raises(ValueError):
        jar.deposit("ABC")
    
    jar.deposit(10)
    assert jar.size == 10

    with pytest.raises(ValueError):
        jar.deposit(5)




def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(-10)
    with pytest.raises(ValueError):
        jar.withdraw("ABC")
    
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.withdraw(7)
