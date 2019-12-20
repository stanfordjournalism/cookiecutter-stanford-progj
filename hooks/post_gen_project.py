import argparse
import logging
import os
import sys

from datakit_github.commands import Integrate

# HACK: Need to direct logging calls to stdout
# to ensure user prompts display when hook is run
# by cookiecutter in a subprocess.
def get_logger():
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger

create_github_repo = os.environ.get('DKIT_GITHUB_INTEGRATE', True)
if create_github_repo:
    sys.stdout.write("\n\n~~ Create a Github repo for this project ~~\n\n")
    cmd = Integrate(None, None, cmd_name='github integrate')
    cmd.log = get_logger()
    cmd.run(argparse.ArgumentParser())

#TODO: Add instructors as collaborators
sys.stdout.write("\n\nTo wrap up:\n")
sys.stdout.write("  $ cd {{ cookiecutter.repo_root }}/\n")
sys.stdout.write("  $ pipenv install\n")
sys.stdout.write("Check out the README.md for more help\n")
