<h1>My simple quiz app </h1>
<p>I created this quiz app to practice my oop programming concepts</p>
<h2>working methodology</h2>
<h3>classes</h3>
<p>These are the classes to be used in the project </p>
<h3>quiz</h3>
<p>
This is a quiz class, it is used to manage the set of questions to be used in a quiz
<br>

**Attributes and methods**
1.questions - a list containing instances from question class
2. name - a string containing the name of the quiz
3. Duration - duration for the quiz
3. High score - calculates the high score of the quiz

**methods**
1. add - adds a question to the quiz
2. score - returns the score of the user in the quiz
3. save - saves a quiz to the storage
4. run - runs the quiz till the quesstions are over or  no time is left
5. display - how the quiz will be displayed in the command line
6. user input - accepts user input
7. set high score -  sets the highscore
</p>

<h3>Questions</h3>
<p>This is a question class, it has some attributes and methods relating to questions </p>

**attributes**
1. question - a text containing the question
2. answer - The answer to the question
3. options - the options of the answer
4. check answer - checks whether an answer  is correct

**methods**
check answer - checks whether the answer is correct and returns zero

<h3>Filestorage</h3>
<p>this is a class that we will use its instance to save all the classes and objects to storage using json</p>

**variables**
the variables defined here are:
1. file_path
    this is the path where the json file will be stored
2. objects
    this is the list of the object dictionaries, to be used to store and reload the data

**methods**
the methods to be defined here are:
1. save
    saves the object to the storage as a json file
2. new
    adds a new dictionary to the objects
3. reload
     this method reloads the obects stored in file to the object

Up to this stage, i have only managed  to save the tasks to storage, as a json file, i have not yet implemented the reload from storage and implement work with the saved data. However i will try and implement that when ill be working with actual json from an api

## Example of working

```
mordecai@pappi:~/Personal-Python-Projects/quizz_app_cli$ python3 cli.py
---reloaded objects---
{'test task': {'name': 'test task', 'questions': [{'question': 'Who was The first penyan president?', 'answer': 'Kenyatta', 'options': ['kibaki', 'uhuru', 'Kenyatta', 'moi']}, {'question': 'Do you love red?', 'answer': 'yes', 'options': ['I dont know', 'yes', 'yes', 'no']}, {'question': 'Who is Ruto?', 'answer': 'president', 'options': ['conman', 'hustler', 'president', 'thief']}, {'question': 'who is Mordecai?', 'answer': 'Senior Backend Developer', 'options': ['Senior Backend Developer', 'child', 'hustler', 'it guy', 'student']}], 'duration': 5, 'high_score': 0}}
{'name': 'test task', 'questions': [{'question': 'Who was The first penyan president?', 'answer': 'Kenyatta', 'options': ['kibaki', 'uhuru', 'Kenyatta', 'moi']}, {'question': 'Do you love red?', 'answer': 'yes', 'options': ['I dont know', 'yes', 'no', 'yes']}, {'question': 'Who is Ruto?', 'answer': 'president', 'options': ['thief', 'president', 'conman', 'hustler']}, {'question': 'who is Mordecai?', 'answer': 'Senior Backend Developer', 'options': ['child', 'Senior Backend Developer', 'student', 'hustler', 'it guy']}], 'duration': 5, 'high_score': 0}
<class 'dict'>
MnM  run_tasks
*** Unknown syntax: run_tasks
MnM  run_quiz
Who was The first penyan president?
         0. kibaki
         1. uhuru
         2. Kenyatta
         3. moi
Input your choice: 2
Do you love red?
         0. I dont know
         1. yes
         2. no
         3. yes
Input your choice: 1
Who is Ruto?
         0. thief
         1. president
         2. conman
         3. hustler
Input your choice: 1
who is Mordecai?
         0. child
         1. Senior Backend Developer
         2. student
         3. hustler
         4. it guy
Input your choice: 1
High score 4
Your score is:  4
MnM  quit
thanks for participating
MnM  mordecai@pappi:~/Personal-Python-Projects/quizz_app_cli$ 
```