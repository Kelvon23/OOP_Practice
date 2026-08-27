#Understand:

class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity,int)or capacity < 0:
            raise ValueError("Only Non-Negative Numbers Allowed")
        self._capacity = capacity
        self._cookies=0

    def __str__(self):
        curr_cookie = "🍪"*self._cookies
        return curr_cookie
        

    def deposit(self, n):
        if not isinstance(n,int)or n < 0:
            raise ValueError("Only Non-Negative Numbers Allowed")


        if self._cookies + n > self._capacity:
            raise ValueError()
        else:
            self._cookies+=n
    

    def withdraw(self, n):
        if not isinstance(n,int)or n < 0:
            raise ValueError("Only Non-Negative Numbers Allowed")

        if n > self._cookies:
            raise ValueError()
        else:
            self._cookies -= n 

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies
    


def main():
    jar = Jar(20)
    jar.deposit(10)
    print(jar.__str__())
    jar.withdraw(5)
    print(jar.__str__())




if __name__ == "__main__":
    main()