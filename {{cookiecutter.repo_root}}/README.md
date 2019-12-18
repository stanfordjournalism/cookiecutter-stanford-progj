# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Pre-flight check

Your system must have the following installed:

* Python >= 3.5 ([install help for Python][])
* [pipenv][] ([install help for pipenv][]) install intructions)

[install help for Python]: https://docs.python-guide.org/starting/installation/
[install help for pipenv]: https://docs.python-guide.org/dev/virtualenvs/#installing-pipenv

## Setup

After creating this project:

* `cd {{ cookiecutter.repo_root }}`
* `pipenv intsall`

### Automating workflow

The above installs [invoke][], a task execution library.
This project ships with a few pre-created commands that assist
with the daily workflow of our class.

```
TK invoke examples
```

You can also add your own commands to the `tasks.py` file
for any project.

### Installing other libraries

Depending on the type of project you're working on,
you may want to install additional Python packages.
Below are some useful librariers for common tasks
such as interacting with APIs, scraping web pages,
and data analysis:

* APIs and web scraping - [requests][], [BeautifulSoup][], [selenium][]
* data analysis - jupyter, pandas, matplotlib

The standard workflow is:

```

```

## Files & Directories

```
└── {{cookiecutter.repo_root}}
    ├── README.md
    ├── data
    │   ├── processed
    │   └── raw
    ├── notebooks
    ├── scripts
    └── src
        └── __init__.py
```

[BeautifulSoup]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
[invoke]: https://www.pyinvoke.org/
[pipenv]: https://pipenv.readthedocs.io/en/latest/
[requests]: https://2.python-requests.org/en/master/
[selenium]: https://selenium-python.readthedocs.io/


## Reference

* [Hitchhiker's Guide to Python](https://docs.python-guide.org/)
* Python Standard Library. A few especially useful libraries:
  * csv
  * etree
  * json
  * os
