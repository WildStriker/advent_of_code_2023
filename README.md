# Advent of Code 2023


[Advent of Code 2023](https://adventofcode.com/2023)


## Description

This advent of code project is a python `Command Line Interface (CLI)` application, complete with example unit tests 

## Getting Started


### Prerequisites

This project uses [pipenv](https://pipenv.pypa.io/en/latest/) to manage python packages.

ensure you have that installed with whichever package manager you use.

e.g. with pip
```bash
pip install pipenv
```

### Installation

To install use:
```bash
pipenv sync
```

add the `--dev` flag if you wish to run unit tests / install over dev dependencies

### Unit Tests

[pytest](https://docs.pytest.org/en/7.4.x/) is used for the unit tests, you can run the tests simply by calling:
```bash
pytest
```

Or directly in your code editor of choice (if supported)

## Usage

This is a `CLI` application.

The python library [click](https://click.palletsprojects.com/en/8.1.x/) was used to build the `CLI`

  - python also has a `stdlib` [argparse](https://docs.python.org/3/library/argparse.html) that is really good as well

You can list all available commands with the `--help` flag

```bash
python -m advent_of_code --help
```

e.g. for day one part one:
```bash
python -m advent_of_code day-01 part-01
```


You can also add the `--help` flag to the subcommands to see all available options (e.g. to change the puzzle input file)