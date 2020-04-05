# Simple service

This is an excersise written in python.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* `make`
* `python` > 3.6
* `docker` (optional)


### Installing

Run a following command in the terminal:

```bash
make init
```

This will setup a virtualenv and install pip packages. Then, activate the virtualenv:

```
source venv/bin/activate
```

... and run a build command which will run a linter against the code:

```bash
make build
```

Alternatively, build a docker image:

```bash
make docker
```

... or build a .tar.gz package:

```bash
make package
```

## Running the tests

Run a following command in the terminal:

```bash
make test
```

## Deployment

Run a following command in the terminal:

```bash
python -m simple_serice ARG1 ARG2 ARG3 ARG4 ARG5 ARG6
```

Where ARGs is a list of integers.

Alternatively, run a docker image, if previously had been built:

```bash
docker run ARG1 ARG2 ARG3 ARG4 ARG5 ARG6
```

### Cleaning up

This command will remove built packages and clean up the working directory.

```bash
make clean
```
