# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile remove-footer all

all: clean html latexpdf remove-footer

remove-footer:
	@echo "Removing footer..."
	@find ./build/html -type f -name "*.html" -exec sed -i'' -z 's|Made with[[:space:]]*<a href="https://github.com/pradyunsg/furo">[[:space:]]*Furo[[:space:]]*</a>||g' {} +
	@echo "Footer removed from HTML files."

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
