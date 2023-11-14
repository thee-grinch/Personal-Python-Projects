import cmd
from quiz import quiz
from questions import question


question1 = question("Who was The first penyan president?", "Kenyatta", ["uhuru", "moi", "kibaki"])
question2 = question("Do you love red?", "yes", ["no", "yes", "I dont know"])
question3 = question("Who is Ruto?" ,"president", ["conman", "hustler", "thief"])
question4 = question("who is Mordecai?", "Senior Backend Developer", ["hustler", "student", "child", "it guy"])
my_list = [question1, question2, question3, question4]
quiz1 = quiz("test task", my_list, 5)
class commandPrompt(cmd.Cmd):
    prompt = "MnM  "

    def do_quit(self, arg):
        """quits the cmd"""
        print("thanks for participating")

    def do_EOF(self, arg):
        """this function quits the cmd"""
        return True
    
    # def new_quiz(self):
    #     """This method initializes a new quiz"""

    #     item = int(input("Enter the number of questions: "))
    #     for i in range(item):
    #         quiz_name = input("Enter a quiz name: ")

    def do_run_quiz(self, arg):
        score = 0
        for question in quiz1.questions:
            print(question.question)
            for idx, value in enumerate(question.options):
                print(f"\t {idx}. {value}")
            i = question.take_user_input()
            score += question.check_answer(i)
        quiz1.highscore = score
        print(f"High score {quiz1.highscore}")
        print(f"Your score is:  {score}")
        
    

if __name__ == "__main__":
    my_cmd = commandPrompt()
    my_cmd.cmdloop()