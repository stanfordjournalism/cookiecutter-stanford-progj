import argparse
import logging
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


do_github = input("\n\nWould you like to create a Github repo for this project? [y|n]: ")
if do_github.lower().strip() == "y":
    cmd = Integrate(None, None, cmd_name='github integrate')
    cmd.log = get_logger()
    cmd.run(argparse.ArgumentParser())
else:
    sys.stdout.write("No Github repo will be created.\n")

#TODO: Add instructors as collaborators
#TODO: Add closing Help with next steps (pipenv shell, docs link etc.)
