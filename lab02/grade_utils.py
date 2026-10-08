"""Module for converting numeric GPAs to letter grades on a 5.0 scale."""


def letter_grade(gpa):
    """Return the letter grade corresponding to a 5.0 GPA scale."""
    if gpa >= 4.50:
        return "A"
    elif gpa >= 3.50:
        return "B"
    elif gpa >= 2.50:
        return "C"
    elif gpa >= 1.50:
        return "D"
    else:
        return "F"
