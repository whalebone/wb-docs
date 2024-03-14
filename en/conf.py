# -*- coding: utf-8 -*-
#
# Whalebone documentation build configuration file, created by
# sphinx-quickstart on Wed Jan  4 17:02:40 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autosectionlabel']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Whalebone'
copyright = u'2024, Whalebone, s.r.o.'
author = u'Whalebone'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'3.2'
# The full version, including alpha/beta/rc tags.
release = u'3.2.1-12'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/scroll-end.html",
        "sidebar/variant-selector.html",
    ]
}
html_title = "Whalebone Documentation"

html_theme_options = {
    "light_logo": "whalebone.png",
    "dark_logo": "whalebone_logo_white.png",
    "light_css_variables": {
        "color-sidebar-background": "#2C2662",
        "color-sidebar-background-border": "transparent",
        "color-background-secondary": "#FCFCFC",
        "color-background-primary": "#FCFCFC",
        "color-sidebar-brand-text": "#D9D9D9",
        "color-sidebar-link-text": "#D9D9D9",
        "color-header-text": "#2BB8BC",
        "color-foreground-primary": "#2C2662",
        "color-foreground-secondary": "#FCFCFC",
        "color-sidebar-item-background": "transparent",
        "color-sidebar-item-background--current": "transparent",
        "color-sidebar-item-background--hover": "transparent",
        "color-brand-primary": "#2BB8BC",
        "color-brand-content": "#2BB8BC",
        "color-brand-visited": "#2BB8BC",
        "color-sidebar-search-text": "#2BB8BC",
        "color-sidebar-search-background": "#FCFCFC",
        "color-sidebar-search-background--focus": "#FCFCFC",
        "color-sidebar-search-border": "transparent",
        "color-sidebar-search-icon": "#2C2662",
        "color-sidebar-caption-text": "#FCFCFC",
        "color-sidebar-link-text--top-level": "#D9D9D9",
        "color-card-background": "#FCFCFC",
        "color-card-border": "#FCFCFC",
        "color-card-marginals-background": "#FCFCFC",
        "sidebar-caption-font-size": "100%",
        "sidebar-item-font-size": "90%",
        "sidebar-search-input-font-size": "100%",
        "font-stack": "Trebuchet MS",
        "sidebar_hide_name": True,
        "color-admonition-background": "#FCFCFC",
    },
    "dark_css_variables": {
        "color-background-primary": "#363636",
        "color-background-secondary": "#363636",
        "color-foreground-primary": "#D9D9D9",
        "color-foreground-secondary": "#D9D9D9",
        "color-admonition-background": "#363636",
        "color-sidebar-background": "#363636",
        "color-sidebar-background-border": "transparent",
    }    
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'default.css',
]

# Output file base name for HTML help builder.
htmlhelp_basename = 'Whalebonedoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Whalebone.tex', u'Whalebone admin guide',
     u'', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'whalebone', u'Whalebone admin guide',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Whalebone', u'Whalebone admin guide',
     author, 'Whalebone', 'Filter online threats off your network',
     'Miscellaneous'),
]


#remove blank pages from pdf
latex_elements = {
  'classoptions': ',openany,oneside',
  'babel': '\\usepackage[english]{babel}'
}
