from setuptools import setup, find_packages
setup(
    name="name",
    version="0.1",
    packages=find_packages(),
    scripts=["main.py"],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=["pandas>=1.03"],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt", "*.rst"],
    },

    # metadata to display on PyPI
    author="",
    author_email="",
    description="",
    keywords="",
    url="",   # project home page, if any
    project_urls={
    },
    classifiers=[
    ]

    # could also include long_description, download_url, etc.
)