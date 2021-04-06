# Bunker Games
*You and your friends gathered together to play a new game called "Bunker Games" in your basement!*

*Your job is to help your teammates ration the supplies and medicine they have, so you can win the game!*

*You will be provided with a skeleton which includes all the folders and files that you will need.*

***Note: You are not allowed to change the folder and file structure and change their names!***

## Judge Upload
#### For the first 2 problems, create a zip file with the project folder and upload it to the judge system
#### For the last problem, create a zip file with the tests folder and upload it to the judge system

## Structure (Problem 1) and Functionality (Problem 2) - [Solution](https://github.com/borislavstoychev/exam_preparation/tree/main/exams_OOP/bunker_games/project)
Our first task is to implement the structure and functionality of all the classes (properties, methods, inheritance, etc.)
##    1. Class Supply
In the file supply.py the class Supply should be implemented:
### Structure
#### The class should be abstract, and should have the following attributes:
    • needs_increase: int – Private attribute, passed upon initialization (if it is a negative number raise ValueError with message "Needs increase cannot be less than zero.")
### Methods
### ```__init__(needs_increase: int)```
#### The __init__ method should receive a needs_increase: int
### apply(survivor: Survivor)
#### Method should increase the needs property of the given survivor with the supply's needs_increase value
##    2. Class FoodSupply
In the food_supply.py file the class FoodSupply should be implemented
### Structure
The class should inherit from the Supply class
### Methods
### ```__init__()```
***An instance of the FoodSupply class will have needs_increase of 20***
##    3. Class WaterSupply
In the water_supply.py file the class WaterSupply should be implemented
### Structure
The class should inherit from the Supply class
### Methods
###```__init__()```
***An instance of the WaterSupply class will have needs_increase of 40***
##    4. Class Medicine
In the medicine.py file the class Medicine should be implemented
### Structure
#### The class should be abstract, and should have the following attributes:
    • health_increase: int – Private attribute, passed upon initialization (if it gets less than zero, raise ValueError with message "Health increase cannot be less than zero.")
### Methods
### ```__init__(health_increase: int)```
#### The __init__ method should receive a health_increase: int
### apply(survivor: Survivor)
#### Method should increase the health property of the given survivor with the medicine's health_increase value
##    5. Class Painkiller
In the painkiller.py file the class Painkiller should be implemented
### Structure
The class should inherit from the Medicine class
### Methods
### ```__init__()```
***An instance of the Painkiller class will have health_increase of 20***
##    6. Class Salve
In the salve.py file the class Salve should be implemented
### Structure
The class should inherit from the Medicine class
### Methods
### ```__init__()```
***An instance of the Salve class will have health_increase of 50***
##    7. Class Survivor
The Survivor class will store the info of each survivor
### Structure
#### The class should have the following attributes:
    • name: str – passed upon initialization (if its set to an empty string, raise ValueError with message "Name not valid!")
    • age: int – passed upon initialization (if its set to a number less than zero, raise ValueError with message "Age not valid!")
    • health: int – 100 upon initialization (if its set to a number less than zero, raise ValueError with message "Health not valid!", its max value is 100)
    • needs: int – 100 upon initialization (if its set to a number less than zero, raise ValueError with message "Needs not valid!", its max value is 100)
    • needs_sustenance – bool property that returns if the survivors needs are less than 100
    • needs_healing – bool property that returns if the survivors health is less than 100
### Methods
### ```__init__(name: str, age: int)```
***Upon initialization all the needed attributes must be set.***
##    8. Class Bunker
The Bunker class will contain all the functionality of our project
### Structure
#### The Bunker class will have the following attributes:
    • survivors: list – empty list upon initialization that will contain all the survivors (objects)
    • supplies: list – empty list upon initialization that will contain all the supplies (objects)
    • medicine: list – empty list upon initialization that will contain all the medicine (objects)
    • food: list – property that returns only the food objects from the supplies (if there are no food supplies, raise IndexError with message "There are no food supplies left!")
    • water: list – property that returns only the water objects from the supplies (if there are no water supplies, raise IndexError with message "There are no water supplies left!")
    • painkillers: list – property that returns only the painkiller objects from the medicine (if there are no painkillers, raise IndexError with message "There are no painkillers left!")
    • salves: list – property that returns only the salve objects from the medicine (if there are no salves, raise IndexError with message "There are no salves left!")
### Methods
###  add_survivor(survivor: Survivor)
If a survivor already exists, raise ValueError with the message "Survivor with name {name} already exists.". Otherwise add the survivor to the survivors list
### add_supply(supply: Supply)
Adds the supply to the supplies list
### add_medicine(medicine: Medicine)
Adds the medicine to the medicine list
### heal(survivor: Survivor, medicine_type: str)
Remove the last medicine added to the medicine list from the given type (if the survivor needs it), apply it to him/her and return a message "{survivor_name} healed successfully with {medicine_type}"
### sustain(survivor: Survivor, sustenance_type: str)
Remove the last supply added to the supplies list from the given type (if the survivor needs it), apply it to him/her and return a message "{survivor_name} sustained successfully with {sustenance_type}"
### next_day()
    • First, the needs of each survivor get reduced by the result of multiplying his/her age by 2
    • Then we need to sustain each survivor by giving him/her one food and one water supply
## Problem 3. Unit Tests - [Solution](https://github.com/borislavstoychev/exam_preparation/tree/main/exams_OOP/survivor/tests)
### *You will be provided with another skeleton for this problem. Open the new skeleton as a new project and write tests for the PaintFactory class. The class will have some methods, fields and one constructor, which are working properly. You are NOT ALLOWED to change any class. Cover the whole class with unit tests to make sure that the class is working as intended. Submit only the test folder.*
