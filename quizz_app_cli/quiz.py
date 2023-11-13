from questions import question

class quiz():
    """This is a class to manage the quizes"""
    def __init__(self, *args, **kwargs ) -> None:
        if args:
            self.__name = args[0]
            self.__questions = args[1]
            self.__duration = args[2]
            self.__high_score = 0
        if kwargs:
            for name

    def take_user_input(self):
        i = int(input("Input your choice: "))
        return i
    

    def calculate_score(self, question, index):
        """Calculate score"""
        if question.check_answer(index):
            return 1
        return 0
    
    @high_scoresetter
    def set_highscore(self, score):
        """set a high score"""
        if score > self.__high_score:
            self.__high_score = score
    
    def to_dict(self):
        """Returns dictionary representation of the object"""
        return self.__dict__
    
    def __str__(self) -> str:
        """the print string representation"""
        my_list = []
        my_list.append(self.__name)
        for question in self.__questions:
            my_list.append(question.question)
        return "\n".join(my_list)