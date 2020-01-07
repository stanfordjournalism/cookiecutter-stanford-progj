# cookiecutter-stanford-progj

A cookiecutter template for Stanford's [Programming in Journalism course][] (Comm 177P/277P) in winter quarter 2020.

This template is intended for use with datakit, a command-line tool for   automating data analysis worfklows. It provides the following features:

* Creation of a standard file/directory structure
* Auto-generation of GitHub projects for code assignments
* Command-line tools to easily save code in git and push to GitHub
* Auto-adding of instructors as repo collaborators

[Programming in Journalism course]: https://github.com/stanfordjournalism/stanford-progj-2020

## Requirements & Setup

* Python 3.5 - 3.7
* pip
* Pipenv
* GitHub acount with your public ssh key
* GitHub API key -> datakit-github config file
* Locally configured git user name and email

After meeting the above requirements, download and install the `requirements.txt` in your system's global Python.

```
curl -s https://raw.githubusercontent.com/stanfordjournalism/cookiecutter-stanford-progj/master/requirements.txt | xargs pip install 
```

## Extra configuration

Environmental settings can be used to control template behavior.

* `PROGJ_GH_INTEGRATE` (default: true) - set to "false" to disable Github project generation
* `PROGJ_GH_ADD_COLLABS` (default: true) - set to "false" to disable adding collaborators. This is most useful when instructors are developing on the repo and want to avoid spamming other instructors.
* `PROGJ_GH_COLLABORATORS` - colon-separated list of GitHub usernames (e.g. user1:user2)

