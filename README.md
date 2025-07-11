# Whalebone public documentation

The documentation is based on the Sphinx framework and .RST (reStructuredText) files. The RST syntax documentation is available [here](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html). Individual product-specific branches are built and published on [Read the Docs](https://app.readthedocs.org/).

The main branch you should use is called `content`. This is where all the documents are and where all changes should be made. The `content` branch is then linked as a submodule to product-specific branches, e.g., `immunity_product`, `peacemaker_product`, etc. The product branches should contain only `product_variables.py` with the product name and `.readthedocs.yaml` with some basic definitions for Read the Docs.

The link to the `content` branch in each product-specific branch is static and needs to be updated to the latest commit with every commit to the `content` branch. These updates are automated using GitHub actions, so you do not need to take care of it. The GitHub action definition is in the `content` branch in `.github/workflows/update_linked_branches.yml`. All documentation projects in Read the Docs are connected to the `wb-docs` repository using webhooks. The webhooks initiate project rebuilding with every new commit to the product-specific branches. All this together means that when you want to make some changes, you only need to commit the changes to the `content` branch and all other activities are carried out automatically, including publishing of the new version on the web.

## Prerequisites

Sphinx requires Python to be installed. The currently used Python version is 3.12. You will then need to install the `pipenv` Python package for testing purposes. The `pipenv` package can be installed as follows: `pip install pipenv`

Next, you need to activate the pipenv virtual environmet by executing `pipenv shell` and `pipenv install -d` commands. Now, your environment is ready.

## Contribution

1. Check out the `content` branch.
1. Create a new branch based on the `content` branch and give it a meaningful name.
1. Make the desired changes.
1. Make a test build
    1. `pipenv shell`
    1. `cd en` or `cd cs`, depending on which language you want to build
    1. `sphinx-build -n -W -b html . ../doc`
    1. Important: Make sure there are no new warnings or errors in the output. There are some known warnings that can be ignored. They are related to deployment_XXX.rst, hos_XXX.rst, and idp_overview.rst.
1. Review the changes in the HTML files in the doc directory.
1. Commit the changes to the new branch.
1. Create a pull request in GitHub to get your changes to the `content` branch.
1. Once the pull request has been approved and merged, your changes will be automatically published to all product-specific documentations in Read the Docs.
