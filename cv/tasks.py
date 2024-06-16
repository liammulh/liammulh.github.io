"""Script for running any/all command line tasks.

All command line tasks should be defined in this file. The only
exception to this is managing dependencies via Pipenv.
"""

from invoke import task


@task
def fmt(c):
    """Format JSON and code."""
    # See https://unix.stackexchange.com/a/244947.
    c.run("jq . cv.json | sponge cv.json")
    c.run("black cv.py")


@task
def lint(c):
    """Run the linter."""
    c.run("pylint cv.py")


@task
def types(c):
    """Check types."""
    c.run("mypy cv.py")


# Invoke requires us to have a context parameter, even though it is
# unused.
# pylint: disable=unused-argument
@task(pre=[fmt, lint, types])
def check(c):
    """Run all code checks."""


@task
def run(c):
    """Run the script."""
    c.run("python cv.py")