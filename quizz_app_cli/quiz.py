from questions import question

class quiz():
    """This is a class to manage the quizes"""
    def __init__(self, *args, **kwargs ) -> None:
        if args:
            self.__name = args[0]
            self.__questions = args[1]
            self.__duration = args[2] or 5
            self.__high_score = 0
            from __init__ import storage
            dictionary_rep = self.to_dict()
            print(dictionary_rep)
            storage.new(dictionary_rep)
            storage.save()
        if kwargs:
            self.__name = kwargs.get("name")
            self.__questions = kwargs.get("questions")
            self.__duration = kwargs.get("duration")
            self.__high_score = kwargs.get("high_score")

    def take_user_input(self):
        i = int(input("Input your choice: "))
        return i
    

    @property
    def questions(self):
        """questions getter"""
        return self.__questions
    
    def calculate_score(self, question, index):
        """Calculate score"""
        if question.check_answer(index):
            return 1
        return 0
    
    @property
    def highscore(self):
        return self.__high_score
    
    @highscore.setter
    def highscore(self, score):
        """set a high score"""
        if score > self.__high_score:
            self.__high_score = score
    
    def to_dict(self):
        """Returns dictionary representation of the object"""
        value = {}
        value.update({"name": self.__name})
        quest_dict = []
        for question in self.__questions:
            new_dict = {}
            new_dict.update({"question": question.question})
            new_dict.update({"answer": question.answer})
            new_dict.update({"options": question.options})
            quest_dict.append(new_dict)
        value.update({"questions": quest_dict})
        value.update({"duration": self.__duration})
        value.update({"high_score": self.__high_score})
        return value
    def __str__(self) -> str:
        """the print string representation"""
        my_list = []
        my_list.append(self.__name)
        for question in self.__questions:
            my_list.append(question.question)
        return "\n".join(my_list)