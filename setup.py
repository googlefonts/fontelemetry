import sys
from setuptools import setup, find_packages
from distutils.util import convert_path

# Version
main_namespace = {}
version_path = convert_path("Lib/fbReporter/__init__.py")
with open(version_path) as v:
    exec(v.read(), main_namespace)

# Classifiers for PyPI
classifiers = {
    "classifiers": [
        "Development Status :: 3 - Alpha",
        "Framework :: Jupyter",
        "Environment :: Console",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Text Processing :: Fonts",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
    ]
}

# Extra, optional dependency packages
extras_require = {}

# Use repository Markdown README.md for PyPI long description
try:
    with open("README.md", encoding="utf-8") as f:
        readme = f.read()
except IOError as e:
    sys.stderr.write(
        "[ERROR] Failed to read the README.md file from git repository for long description definition: {}".format(
            str(e)
        )
    )

setup(
    name="fb-reporter",
    version=main_namespace["__version__"],
    description="A library and toolset for typeface software development reporting",
    author="Font Bakery Reporter Authors and Contributors",
    author_email="dcrossland@google.com",
    # TODO
    url="***",
    # TODO
    license="***",
    platforms=["Any"],
    long_description=readme,
    long_description_content_type="text/markdown",
    package_dir={"": "Lib"},
    packages=find_packages("Lib"),
    include_package_data=True,
    extras_require=extras_require,
    python_requires=">=3.6",
    entry_points={"console_scripts": ["fb-reporter = fbReporter.__main__:main"]},
    **classifiers
)
