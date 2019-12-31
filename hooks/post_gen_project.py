import argparse
import logging
import os
import sys

from datakit_github.commands import Integrate
import github

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

create_github_repo = os.environ.get('PROGJ_GH_INTEGRATE', 'true')
if create_github_repo == 'true':
    sys.stdout.write("\n\n~~ Create a Github repo for this project ~~\n\n")
    cmd = Integrate(None, None, cmd_name='github integrate')
    cmd.log = get_logger()
    integrate_choices = cmd.run(argparse.ArgumentParser())

    # Add instructors as collaborators
    api_key = cmd.configs.get('github_api_key')
    g = github.Github(api_key)
    gh_user = integrate_choices['account']
    repo = g.get_repo("{}/{{ cookiecutter.repo_root }}".format(gh_user))
    add_collabs = os.environ.get('PROGJ_GH_ADD_COLLABS', 'true')
    if add_collabs == 'true':
        try:
            collaborators = os.environ['PROGJ_GH_COLLABORATORS'].split(':')
        except KeyError:
            collaborators = ['zstumgoren', 'dilcia19']
        for collaborator in collaborators:
            # Handle when repo owner adds self as collaborator
            try:
                repo.add_to_collaborators(collaborator, 'admin')
            except github.GithubException:
                pass

sys.stdout.write("\n\nTo wrap up:\n")
sys.stdout.write("  $ cd {{ cookiecutter.repo_root }}/\n")
sys.stdout.write("  $ pipenv install\n")
sys.stdout.write("Check out the README.md for more help\n")
