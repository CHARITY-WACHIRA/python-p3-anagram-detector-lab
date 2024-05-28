
#defination of the anagram class
class Anagrams:
    def _init_(self,word):
        self.word = word.lower()

 #defination of the match method
    def match (self,possible_anagrams):
        matches =[]        
        sorted_word=sorted(self.word)

        for anagram in possible_anagrams:
            sorted_anagrams =sorted (anagram.lowe())
            if sorted_anagrams ==sorted_word:
                matches.append(anagram)

            return matches    



