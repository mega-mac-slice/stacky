# stacky [![pipeline status](https://gitlab.com/mega-mac-slice/stacky/badges/master/pipeline.svg)](https://gitlab.com/mega-mac-slice/stacky/commits/master)[![pypi](https://img.shields.io/pypi/v/mms-stacky.svg?maxAge=86400)](https://pypi.org/project/mms-stacky/)

A service management tool for local development.

## Requirements
- `python 3`
- `pipenv`

## Installation
### Development
```bash
git clone git@gitlab.com:mega-mac-slice/stacky.git
cd stacky
make install

stacky --help
```
### Brew
```bash
brew tap mega-mac-slice/tap && brew install stacky
```

## Configuration 
A "Stacky File" is a json file in a project directory typically named _.stacky.json_ that looks like:
```json
{
  "name": "dev-application",
  "commands": {
    "start": "make start",
    "status": "make status"
  },
  "stack": [
    "git@gitlab.com:mega-mac-slice/dev-postgres.git",
    "git@gitlab.com:mega-mac-slice/dev-redis.git",
    "git@gitlab.com:mega-mac-slice/dev-elasticsearch.git"
  ],
  "extra": {
    "kafka": [
       "git@gitlab.com:mega-mac-slice/dev-fast-data-dev.git"
    ]
  }
}
```
Where we defined some commands for the project itself and also the project's dependencies on postgres, redis and elasticsearch.

## Usage
### Start
```bash
stacky start
```
This will do the following:
- Iterate through each dependency defined in stack and retrieve it if it doesn't already exist locally.
- For each dependency, check if it also has a .stacky.json and retrieve those dependencies defined in stack locally.
- For each dependency, check it's status and start it if needed.

With our example .stacky.json we would begin with:
```text
dev-application \
    .stacky.json
    Makefile
```
And after running `stacky start` would have the dependencies checked out locally adjacent to the project.
```text
dev-application \
    .stacky.json
    Makefile
dev-postgres \
    .stacky.json
dev-redis \
    .stacky.json
dev-elasticsearch \ 
    .stacky.json
```

### Status
```bash
stacky status
```
This will iterate through the dependencies and check it's status. Letting you know if the stack for your application is running.
```bash
> stacky status
[INFO] dev-application - ok
[INFO] dev-postgres - ok
[INFO] dev-redis - ok
[INFO] dev-elasticsearch - ok
```

### Stop
```text
stacky stop
```
This will iterate through the dependencies and stop them.
```bash
> stacky stop
[INFO] stopping | dev-elasticsearch
[INFO] stopping | dev-redis
[INFO] stopping | dev-postgres
```

### Run
```bash
stacky run command-name
```
Additional commands can be defined in _commands_ and invoked with run.
```bash
> stacky run reset
[INFO] dev-postgres - ok
[INFO] dev-redis - ok
[INFO] dev-elasticsearch - ok
```
With the following possible results:
- `ok` - command existed and ran successfully.
- `fail` - command existed and ran unsuccessfully.
- `skip` - command did not exist.

###  Paths
```text
stacky paths
```
Provides porcelain output of dependency paths intended for usage with external tools.
```bash
> stacky paths
/dev/src/dev-elasticsearch
/dev/src/dev-redis
/dev/src/dev-postgres

> stacky paths | xargs rm -rf
```


## Command Lifecycle
### install - TODO
### start
### status
### stop

## Supported Dependencies
### git ssh/https
- _ssh_ - `git@gitlab.com:mega-mac-slice/dev-postgres.git`
- _https_ - `https://gitlab.com/mega-mac-slice/dev-postgres.git`

### local 


