# Python Test - KarHub

We want to put a set of data in a standard format.
The data is composed of car maker, car model, car year and car type.
Here is an example:
Audi A6 1997 2.8 4p
We have a comprehensive list *A* of car submodels with the names in a standard way.
Here is a sample:
Audi A6 2015 2.0 Tfsi Ambiente S-tronic 4p
Audi A6 1997 2.8 4p
BMW Serie 3 1995 1.9 3p
BMW Serie 3 1995 1.9 Aut. 3p
BMW Serie 3 1996 1.9 3p
BMW Serie 3 1996 1.9 Aut. 3p
Chevrolet Blazer 1996 2.2 Std 5p
Chevrolet Blazer 1996 2.5 Dlx Turbo 5p
We have a list *B* of car submodels with the names organised in another way.
Here is a sample:
AUDI 80 1982@#1.8
AUDI 80 1983@#1.8
VOLKSWAGEN PASSAT 1990@#SURF 1.8 8V
VOLKSWAGEN PASSAT 1992@#VR6 2.8 12V
VOLKSWAGEN PASSAT 1993@#VR6 2.8 12V
(“@#” was added to help to parse or finding the year)
We need to associate each item in the B list to one item in the A list, or vice versa.
