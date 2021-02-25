import random
import unittest

class FizzBuzz:

    def __init__(self, value = random.randint(-15,100)):
        self.value = value
        self.verifyValue()

    def getResult(self):
        return self.result

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
            self.result = self.value

class Tests(unittest.TestCase):
    def modulo3(self):
        self.assertEqual(FizzBuzz(36).getResult(), "Fizz")

    def modulo5(self):
        self.assertEqual(FizzBuzz(65).getResult(), "Buzz")

    def belowOrEqual0(self):
        self.assertRaises(Exception, FizzBuzz(5 - random.randint(5, 100)).getResult())

    def noCase(self):
        self.assertEqual(FizzBuzz(64).getResult(), 64)

    def modulo5et3(self):
        self.assertEqual(FizzBuzz(15 * random.randint(1,10)).getResult(), "FizzBuzz")

if __name__ == '__main__':
   test = Tests()

   test.modulo3()
   test.modulo5()
   test.belowOrEqual0()
   test.noCase()
   test.modulo5et3()
