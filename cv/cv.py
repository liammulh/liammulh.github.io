"""Spits out my resume in Markdown, HTML, and PDF."""

# Built-in libraries:
import json

# Third-party dependencies:
from dotenv import load_dotenv
from jinja2 import Environment, PackageLoader, select_autoescape
from weasyprint import HTML  # type: ignore

# Set environment variables.
load_dotenv()

# We ask Jinja (the templating library) to look for a templates
# directory in the same directory as our cv.py Python module.
env = Environment(loader=PackageLoader("cv"), autoescape=select_autoescape())


def read_json(filename: str) -> dict:
    """Read JSON into a Python dictionary."""
    with open(filename, encoding="utf-8") as json_file:
        return json.load(json_file)


def write_file(filename: str, content: str):
    """Write a file to disk overwriting existing content."""
    with open(filename, encoding="utf-8", mode="w") as file:
        file.write(content)


def write_markdown():
    """Convert the JSON CV into a Markdown file."""
    cv = read_json("cv.json")
    template = env.get_template("cv.md")
    markdown = template.render(cv=cv)
    write_file("cv.md", markdown)


def write_html():
    """Convert the JSON CV into an HTML file."""
    cv = read_json("cv.json")
    template = env.get_template("cv.html")
    html = template.render(cv=cv)
    write_file("cv.html", html)


def write_pdf():
    """Convert the JSON CV into a PDF."""
    write_html()
    HTML("cv.html").write_pdf("cv.pdf")


if __name__ == "__main__":
    write_markdown()
    write_html()
    write_pdf()
