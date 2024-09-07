# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self,list_of_words):
        new_list_of_anagrams=[]
        for word in list_of_words:
            if sorted(word.lower()) == sorted(self.word)and word.lower() !=self.word:
                new_list_of_anagrams.append(word)
                
        return new_list_of_anagrams
                