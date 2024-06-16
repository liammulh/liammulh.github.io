"""Spits out my resume in Markdown, HTML, and PDF."""

# pylint: disable=consider-using-join
# Thanks, Pylint. I considered it.

import json
from string import Template


def read_json() -> dict:
    """Read JSON CV into a Python dictionary."""
    with open("cv.json", encoding="utf-8") as json_file:
        return json.load(json_file)


def write_file(filename: str, content: str):
    """Write a file to disk overwriting existing content."""
    with open(filename, encoding="utf-8", mode="w") as file:
        file.write(content)


def to_markdown():
    """Convert the JSON CV into Markdown."""
    json_cv = read_json()

    # Add basic info.
    # ==================================================================
    basic_info = Template(
        """# $name 

- Phone: $phone
- Email: $email
- Location: $location
"""
    )
    content = basic_info.substitute(json_cv["basic-info"])

    # Add experience.
    # ==================================================================
    content += "\n"
    content += "## Experience"
    content += "\n"
    for experience in json_cv["experience"]:

        # Create responsibilities string for the experience.
        responsibilities_string = ""
        for responsibility in experience["responsibilities"]:
            responsibilities_string += f"- {responsibility}\n"

        experience_template = Template(
            f"""### $title - $employer ($start-$end)

*$location*

{responsibilities_string}"""
        )

        content += "\n"
        content += experience_template.substitute(experience)

    # Add education.
    # ==================================================================
    content += "\n"
    content += "## Education"
    content += "\n"
    for education in json_cv["education"]:

        # Create notes string for the education.
        notes_string = ""
        for note in education["notes"]:
            notes_string += f"- {note}\n"

        education_template = Template(
            f"""### $degree - $institution ($start-$end)

{notes_string}"""
        )

        content += "\n"
        content += education_template.substitute(education)

    write_file("cv.md", content)


if __name__ == "__main__":
    to_markdown()
