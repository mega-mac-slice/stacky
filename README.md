# stacky 
A service management tool for local development.

- [![pipeline status](https://gitlab.com/mega-mac-slice/stacky/badges/master/pipeline.svg)](https://gitlab.com/mega-mac-slice/stacky/commits/master)

## Requirements
- `python 3`
- `pipenv`

## Installation
```bash
git clone git@gitlab.com:mega-mac-slice/stacky.git
cd stacky
make install

stacky --help
```

## Configuration 
A "Stacky File" is a json file in a project directory typically named _.stack.json_ that looks like:
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
  ]
}
```
Where we defined some commands for the project itself and also the project's dependencies on postgres, redis and elasticsearch.

## Usage
### Start
```bash
stacky start
```
This will do the following:
- Iterate through each dependency and retrieve it if it doesn't exist locally.
- For each dependency, check if it also has a .stacky.json and retrieve those dependencies locally.
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


## Command Lifecycle
### install
### start
### status
### stop

## Supported Dependencies
### git
### http/https
### local
