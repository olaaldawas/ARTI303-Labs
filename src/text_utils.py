"""Utility functions for processing text and student names."""


def clean_name(raw):
    """Clean a name string by removing excess whitespace and applying title case."""
    words = raw.split()
    return " ".join(words).title()
