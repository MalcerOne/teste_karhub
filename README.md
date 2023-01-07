# Python Test - KarHub

We want to put a set of data in a standard format.<br><br>
The data is composed of car maker, car model, car year and car type.<br>
Here is an example:<br>
Audi A6 1997 2.8 4p<br><br>
We have a comprehensive list *A* of car submodels with the names in a standard way.<br>
Here is a sample:<br>
Audi A6 2015 2.0 Tfsi Ambiente S-tronic 4p<br>
Audi A6 1997 2.8 4p<br>
BMW Serie 3 1995 1.9 3p<br>
BMW Serie 3 1995 1.9 Aut. 3p<br>
BMW Serie 3 1996 1.9 3p<br>
BMW Serie 3 1996 1.9 Aut. 3p<br>
Chevrolet Blazer 1996 2.2 Std 5p<br>
Chevrolet Blazer 1996 2.5 Dlx Turbo 5p<br><br>
We have a list *B* of car submodels with the names organised in another way.<br>
Here is a sample:<br>
AUDI 80 1982@#1.8<br>
AUDI 80 1983@#1.8<br>
VOLKSWAGEN PASSAT 1990@#SURF 1.8 8V<br>
VOLKSWAGEN PASSAT 1992@#VR6 2.8 12V<br>
VOLKSWAGEN PASSAT 1993@#VR6 2.8 12V<br><br>
(“@#” was added to help to parse or finding the year)<br>
We need to associate each item in the B list to one item in the A list, or vice versa.

# How to execute
* First, you need to git clone this repository into a directory of your choice.
* Then, run this command on the terminal, to create a virtual enviroment of the project `python3 -m venv env`
* A directory /env will be created. Execute this command on console: `source env/bin/activate`
* Now, you can see that you are already into the enviroment. Execute the next command to install all dependencies of the project: `pip install -r requirements.txt`
* Finally, download [this](https://docs.google.com/spreadsheets/d/1UQwiCNfocyT_RmETH73EGCKthtKgmrdJ/edit#gid=964486320 "First file") and [this](https://drive.google.com/file/d/1gMzbKAgrJFJ4CQYoE-HkBaXMlLKeBlhL/view "Second file") file, and put inside a directory in the main project called 'files'.
* Then, you can execute the command: `python3 main.py` to run the program. A file named "final.csv" should pop in the main directory at the end of execution.

