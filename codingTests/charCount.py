import math

class CharacterCounter:
    @staticmethod
    def countCharacters(inputValue):
        count = 0
        for i in range(int(inputValue)+1):
            count += len(str(i))

        return count


print(CharacterCounter.countCharacters(21))