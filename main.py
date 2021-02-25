import random
import unittest

class FizzBuzz:

    def __init__(self, value = random.randint(-15,100)):
        self.value = value
        self.verifyValue()

    def getResult(self):
        return self.result

    def getValue(self):
        return self.value

    def verifyValue(self):
        if(self.value <= 0):
            self.result = Exception("le nombre ne peut pas etre inférieur ou égal à 0 "+ str(self.value))
        elif(self.value % 5 == 0):
            result = "Buzz"
            if(self.value % 3 == 0):
                result = "FizzBuzz"
            self.result = result
        elif(self.value % 3 == 0):
            self.result = "Fizz"
        else:
            self.result = "Le nombre était " + str(self.value)



class Tests(unittest.TestCase):
    def modulo3(self):
        self.assertEqual(FizzBuzz(36).getResult(), "Fizz")

    def modulo5(self):
        self.assertEqual(FizzBuzz(65).getResult(), "Buzz")

    def below0(self):
        self.assertRaises(Exception, FizzBuzz(5 - random.randint(5, 100)).getResult())

if __name__ == '__main__':
   test = Tests()
   test.modulo3()
   test.modulo5()
   test.below0()

