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