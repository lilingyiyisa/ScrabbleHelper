class Scrabbler(object):

    # a scores dictionary that stores information of the score of a certain letter.
    score = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1, "m": 3,
             "n": 1, "o": 1, "p": 3, "q": 10, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8, "y": 4, "z": 10}

    # read the information in words dictionary and create a word list.
    def __init__(self):
        self.wordList = []
        fileIn = open("words.txt", "r")
        for line in fileIn:
            line = line.strip()
            self.wordList.append(line)
        fileIn.close()

    # Whenever you display possible words to the user, also display the point values.
    def returnScores(self, List):
        answerList = []
        for word in List:
            s = 0
            for letter in word:
                s += Scrabbler.score[letter]
            answerList.append(s)
        return answerList

    # Ask user for set of tiles and then show them the word that they can make that is worth the most points.
    def mostPoints(self, tiles):
        maxScore = 0
        answerlist = []
        for word in self.wordList:
            flag = 1
            for letter in word:
                if letter not in tiles:
                    flag = 0
            if flag == 1:
                s = 0
                for letter in word:
                    s += Scrabbler.score[letter]
                if s > maxScore:
                    maxScore = s
                    answerlist = [word]
                elif s == maxScore:
                    answerlist.append(word)
        return answerlist, self.returnScores(answerlist)

    # Ask user for set of tiles and then show all words that can be made with any of the letters.
    def allResults(self, tiles):
        answerlist = []
        for word in self.wordList:
            flag = 1
            for letter in word:
                if letter not in tiles:
                    flag = 0
            if flag == 1:
                answerlist.append(word)
        return answerlist, self.returnScores(answerlist)

    # Ask user for set of tiles and then show the anagrams (i.e. words made using all the letters).
    def anagrams(self, tiles):
        answerlist = []
        for word in self.wordList:
            flag = 1
            for letter in word:
                if letter not in tiles:
                    flag = 0
            if flag == 1:
                letterList = list(word)
                allIn = 1
                for letter in tiles:
                    if letter in letterList:
                        letterList.remove(letter)
                    else:
                        allIn = 0
                        break
                if allIn == 1:
                    answerlist.append(word)
        return answerlist, self.returnScores(answerlist)

    # List all words that start with a “Q” but are not followed by a “u”.
    def qWithoutU(self):
        answerList = []
        for word in self.wordList:
            if word[0] == "q" and word[1] != "u":
                answerList.append(word)
        return answerList, self.returnScores(answerList)

    # Display all 2-letter words.
    def twoLetter(self):
        answerList = []
        for word in self.wordList:
            if len(word) == 2:
                answerList.append(word)
        return answerList, self.returnScores(answerList)

    # Ask user for a letter and then show all the 3-letter words containing that given input tile.
    def threeLetter(self, tiles):
        answerlist = []
        for word in self.wordList:
            if tiles in word and len(word) == 3:
                answerlist.append(word)
        return answerlist, self.returnScores(answerlist)

    # Word verifier: Ask user for input and then verify that it exists within the Scrabble dictionary.
    def verifier(self, tiles):
        if tiles in self.wordList:
            return "Correct, the word is in our word list."
        else:
            return "Oops, the word is not in our word list."

    # Ask user to enter one or more letters and then show all words that end with that group of letters.
    def ending(self, tiles):
        answerList = []
        for word in self.wordList:
            i = 1
            flag = 1
            lenWord = len(word)
            lenTiles = len(tiles)
            while i <= lenWord and i <= lenTiles:
                if word[lenWord-i] != tiles[lenTiles-i]:
                    flag = 0
                i += 1
            if flag == 1:
                answerList.append(word)
        return answerList, self.returnScores(answerList)

    # Ask user to enter one or more letters and then show all words that begin with that group of letters.
    def beginning(self, tiles):
        answerList = []
        for word in self.wordList:
            i = 0
            flag = 1
            lenWord = len(word)
            lenTiles = len(tiles)
            while i < lenWord and i < lenTiles:
                if word[i] != tiles[i]:
                    flag = 0
                i += 1
            if flag == 1:
                answerList.append(word)
        return answerList, self.returnScores(answerList)

    # Ask user to enter a letter and then show all words containing the letters “X” or “Z” and the input tile.
    def xorz(self, tiles):
        answerlist = self.allResults(tiles+"x") + self.allResults(tiles+"z")
        return answerlist, self.returnScores(answerlist)