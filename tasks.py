"""Script for running any/all command line tasks.

All command line tasks should be defined in this file. The only
exception to this is managing dependencies via Pipenv.
"""

# Third-party dependencies:
from invoke import task


@task
def fmt(c):
    """Format JSON and code."""
    # See https://unix.stackexchange.com/a/244947.
    c.run("jq . cv/cv.json | sponge cv/cv.json")
    c.run("black cv/cv.py")


@task
def lint(c):
    """Run the linter."""
    c.run("pylint cv/cv.py")


@task
def types(c):
    """Check types."""
    c.run("mypy cv/cv.py")


# Invoke requires us to have a context parameter, even though it is
# unused.
# pylint: disable=unused-argument
@task(pre=[fmt, lint, types])
def check(c):
    """Run all code checks."""


@task
def cv(c):
    """Run the script that generates the CV files."""
    c.run("cd cv && python cv.py")
