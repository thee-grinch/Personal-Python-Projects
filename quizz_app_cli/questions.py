import random


class question():
    """This is a class to initialize questions"""
    def __init__(self, question="", answer="", options="") -> None:
        """this method initializes the class question """
        self.__question = question
        self.__answer = answer
        self.__options = list(set(answer + options))
    
    def check_answer(self, index):
        """This method checks whether the selected """
        if self.__answer == self.__options[index]:
            return True
        return False

    @property
    def answer(self):
        return self.__answer
    
    @answersetter
    def answer(self, ans):
        self.__answer = ans
    
    @property
    def question(self):
        return self.__question
    
    @questionsetter
    def question(self, question):
        self.__question = question
    
    @property
    def options(self):
        return ", ".join(self.__options)
    
    @optionssetter
    def options(self, *args):
        opt = list(set(args))
        random.shuffle(opt)
        self.__options = opt
