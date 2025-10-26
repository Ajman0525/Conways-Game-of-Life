# Conway's Game of Life: Implemented with Test-Driven Development Approach
A simulation of Conway’s Game of Life built using Python and developed following the Test-Driven Development (TDD) approach. 
The project demonstrates the application of automated testing and Python-based visualization using Pygame.

## Project Description
The Conway’s Game of Life Program is our entry for the TDD Programming Competition.
It simulates the behavior of a grid of cells that evolve over multiple generations based on Conway’s famous rules of life and death.

The user can specify the number of generations, and the program will run and display the simulation results using Pygame.
All logic was implemented and tested through a TDD approach, writing tests first then implementing code to pass those tests.

The project also includes automated unit tests using Pytest, ensuring each rule of the game behaves as expected.

# Getting Started
Before running the program, make sure you have the following installed:

- Windows 10 / macOS / Linux
- Python 3.13 or higher
- pip (Python package manager)
- pipenv (for managing virtual environments and dependencies)

Main Python Libraries:
- `pygame` — for graphical simulation
- `pytest` — for automated testing


## Installing 
#### 1. Clone the repository from GitHub
```bash 
git clone https://github.com/mxncsn/Conways-Game-of-Life .git
cd Conways-Game-of-Life
```
#### 2. Install pipenv (if not already installed)
```bash 
pip install pipenv
```
#### 3. Install all dependencies
```bash 
pipenv install
```
#### 4. Activate the virtual environment
```bash 
pipenv shell
```



## Executing Program
To run the Game of Life simulation, follow these steps:

#### 1. Open the project folder in VS Code or your preferred IDE.

#### 2. Activate the pipenv environment:
```bash 
pipenv shell
```
#### 3. Run the main simulation program:
```bash 
pipenv run python -m src.main
```
#### 4. To run automated tests using Pytest:
```bash 
pipenv run python -m pytest
```

# Help
If you encounter issues with pipenv not being recognized, ensure that it is installed correctly and added to your PATH.
You can verify installation with:

```bash 
pip show pipenv
```

If dependencies fail to install, try running:
```bash 
pipenv --rm
pipenv install
```


## Authors

Contributors:
- Ajman Mocsana       
- Ryan Nichole Recososa    
- Amin Casan               

Developed for the TDD Programming Competition using Python and Visual Studio Code.
