# Sudoku Solver

Ever get stuck on a tough sudoku and want to see the solution? This small application will solve it and give you the solution.

## Getting Started



### Prerequisites

Things you need to install to use the app

```
Homebrew
Python 3.x.x
```

### Installing

Installing on Mac:
Install Homebrew
Check python version
Install python version if below 3.0
Check python version

Install Homebrew: open terminal on your mac, paste in the following and press enter
```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Install Python 3
```
$ brew install python
```

Check if your python version is 3 or higher. This should come back with something like: 'Python 3.7.1'
```
$ python --version
```

## Deployment

To use this application download the files from the main repo then:
1) Open the text file named "sudokus_start.txt
2) It contains a long list of unsolved sample sudoku boards. If you do not modify this file, the program will simply attempt to solve all sudokus in this file. WARNING:::This will take a veeery long time as some of the sudokus are very complicated.

It is recommended that you clear the contents of this file and input your own sudoku in the same format. The format is as follows:
Each line should contain 81 digits comprising a single sudoku puzzle, written from left to right, top to bottom, where zero's are empty spaces.

3) Once you have entered one or more 81-digit sudoku code in the sudokus-start.txt file, in the mac terminal, type in:
```
$ python3 driver_3.py
```
4) If your sudoku is solvable, there will be a solution board printed into your terminal.

## Built With

* [Python3](https://docs.python.org/3/) - The programming language used


## Authors

* **Dan Sendik** - *Initial work*

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project does not require any licenses

## Acknowledgments

* Hat tip to me, since I did the development work
