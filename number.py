class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return self.value % 2 == 1

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return not self.is_odd()

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        for i in range(2, self.value):
            if self.value % i:
                return False

        return True

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        divisors = []
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                divisors.append(i)

        return divisors

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        a = self.get_digits()
        return len(a)
        

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        a = self.get_digits()
        return sum(a)

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        
        return str(self.value)[::-1] 

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        a = self.get_digits()
        return a[0]==[-1]

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        a = []
        s = str(self.value)
        for i in s:
         a.append(int(i))
        return a
     

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        a  = self.get_digits()
        return max(a)

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        a  = self.get_digits()
        return min(a)

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        a = self.get_digits()
        return sum(a)/len(a)

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        s = sorted(self.get_digits())
        a  = len(s) // 2
        return s[a]

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        a = self.get_digits()
        s = range(a[0],a[-1]+1)
        return list(s)
        


    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        pass


# Create a new instance of Number
number = Number(12534)
print(number.get_median())
