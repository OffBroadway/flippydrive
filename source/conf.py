# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'flippydrive'
copyright = '2024, ChrisPVille RadicalPlants'
author = 'ChrisPVille RadicalPlants'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.todo']

templates_path = ['_templates']
exclude_patterns = []

todo_include_todos = True
todo_emit_warnings = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

html_theme_options = {
    "announcement": "<em>IMPORTANT:</em> docs are still a work in progress!",
}

html_title = 'Flippydrive Docs'
html_show_sphinx = False
show_copyright = False
