from docutils import nodes
from docutils.parsers.rst import roles
from docutils.parsers.rst import Directive
from docutils.statemachine import StringList

class BaseStatusDirective(Directive):
    has_content = True
    status_type = 'status'
    prefix_text = 'Status'  # Default text, overridden in subclasses

    def run(self):
        # Create a new list of strings from the content with the prefixed text
        content_with_prefix = StringList([self.prefix_text] + self.content.data, source='')

        # Create a paragraph node to contain the content
        paragraph_node = nodes.paragraph()
        
        # Nested parsing to handle the full content including RST syntax
        self.state.nested_parse(content_with_prefix, self.content_offset, paragraph_node)
        
        # Apply the specific class to all nodes in the paragraph
        for node in paragraph_node.traverse(nodes.TextElement):
            node['classes'].append('status')
            node['classes'].append(f'status-{self.status_type}')
        
        return [paragraph_node]

class OkDirective(BaseStatusDirective):
    status_type = 'gok'
    prefix_text = 'OK'
    
class ProblemsDirective(BaseStatusDirective):
    status_type = 'gprob'
    prefix_text = 'ISSUES'
    
class BadDirective(BaseStatusDirective):
    status_type = 'gbad'
    prefix_text = 'BAD'
    
def setup(app):
    app.add_directive("gok", OkDirective)
    app.add_directive("gprob", ProblemsDirective)
    app.add_directive("gbad", BadDirective)
    app.add_css_file('custom.css')
    
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

html_title = 'FlippyDrive Docs'
html_show_sphinx = False

html_css_files = [
    'https://cdn.datatables.net/2.0.8/css/dataTables.dataTables.min.css',
]

html_js_files = [
    'https://code.jquery.com/jquery-3.7.1.min.js',
    'https://cdn.datatables.net/2.0.8/js/dataTables.min.js',
    'main.js',
]
