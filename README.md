# cookiecutter-stanford-progj

A [cookiecutter][] template for Stanford's *Programming in Journalism course* (Comm 177P/277P).

The template is designed to introduce standardized development workflows and code hygiene to students.

We encourage you to fork and modify our code and [send us feedback][]!

[cookiecutter]: https://cookiecutter.readthedocs.io/en/latest/
[send us feedback]: https://github.com/stanfordjournalism/cookiecutter-stanford-progj/issues

## Features

This template is intended for use with [datakit][], a command-line tool for   automating data analysis worfklows. It provides the following features:

* Generates a standard file/directory structure
* Simplifies sharing of source data by saving it in git
* Encourages use of virtual environments via [Pipenv][]
* Auto-generates GitHub projects
* Provides command-line tools to easily save code in git and push to GitHub
* Automatically adds instructors as repo collaborators


[datakit]: https://datakit.ap.org/
[Pipenv]: https://pipenv.readthedocs.io/en/latest/

## Requirements & Setup

* [Python][] >= 3.7
* Follow the [datakit-github install docs][]. **Skip the section called "Install DataKit libraries"** (these are handled in the step below).
* Download and install `requirements.txt` in your system Python.

```
curl -s https://raw.githubusercontent.com/stanfordjournalism/cookiecutter-stanford-progj/master/requirements.txt | xargs pip install 
```

[Python]: https://docs.python-guide.org/starting/installation/
[datakit-github install docs]: https://datakit-github.readthedocs.io/en/latest/install.html

## Usage

This cookiecutter template will be installed locally after creating your first project:

```
datakit project create --template gh:stanfordjournalism/cookiecutter-stanford-progj
```

If it's your only cookiecutter template (or the default), on subsequent runs you can simply use:

```
datakit project create
```

For more details on using cookiecutter templates with datakit, see the [datakit-project docs][].

[datakit-project docs]: https://datakit-project.readthedocs.io/en/latest/templates.html

## Project structure

Projects generated using this template include a README.md with important reminders on the standard workflow, such as using `pipenv shell` when running code or tasks for the project.

The template builds out the below project structure:

```
├── Pipfile
├── README.md
├── data
│   ├── processed (Raw data that has been transformed)
│   └── raw  (Copy of original source data)
├── lib (Re-usable Python code in .py files)
│   ├── __init__.py
│   └── utils.py
├── notebooks (Jupyter notebooks)
├── scripts (Number-prefixed data processing scripts)
│   └── 1-etl.py
└── tasks (invoke task definitions)
    ├── __init__.py
    └── code.py

```

## Saving/pushing code

Projects generated with this template include [invoke][] command-line tasks designed to simplify the use of version control for new programmers.

```
# activate the project environment
cd your-project
pipenv shell

# save code changes in local git
invoke code.save

# push commits to GitHub
invoke code.push
```

These commands are limited by design. Most notably, they require students to be on the `main` branch of the repo, and do not provide a way to pull upstream changes.

More advanced students who want to branch, pull code from GitHub, etc. should use the standard git command-line tools or a Desktop client of their choice.

> Note, we do **not** recommend GitHub's official desktop client for this template since it is designed for https-based interactions rather than ssh.

[invoke]: https://www.pyinvoke.org/

## Instructors

Students who use invoke commands to save and push work to GitHub should generally be following a unidirectional workflow (save on `main` and push). If an instructor needs to suggest code changes or alternative implementations as part of the feedback process, we recommend one of the below strategies:

* Add comments on files on GitHub
* Use GH issues
* Create a branch with changes and push to GitHub for discussion
* Push changes to `main` branch and pair program with the student to guide them through use of lower-level git commands to pull down changes

## Extra configuration

Environment settings can be used to control template behavior. These can be useful when testing the template to avoid spamming collaborators.

* `PROGJ_GH_INTEGRATE` (default: true) - set to "false" to disable GitHub project generation
* `PROGJ_GH_ADD_COLLABS` (default: true) - set to "false" to disable adding collaborators. This is most useful when instructors are developing on the repo and want to avoid spamming other instructors.
* `PROGJ_GH_COLLABORATORS` - colon-separated list of GitHub usernames (e.g. user1:user2)

