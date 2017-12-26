## AGEpy [![Build Status](https://travis-ci.org/mpg-age-bioinformatics/AGEpy.svg?branch=master)](https://travis-ci.org/mpg-age-bioinformatics/AGEpy) [![PyPI version](https://badge.fury.io/py/AGEpy.svg)](https://badge.fury.io/py/AGEpy) ![ReadtheDocs](https://readthedocs.org/projects/pip/badge/)

This python package contains Bioinformatics tools developed at the
Bioinformatics Core Facility of the Max Planck Institute for Biology of Ageing.

> Max Planck Institute for Biology of Ageing  
> Joseph-Stelzmann-Str. 9b  
> D-50931 Cologne  
> Germany

[https://bioinformatics.age.mpg.de](https://bioinformatics.age.mpg.de)

#### Read the Docs

[agepy.readthedocs.io](http://agepy.readthedocs.io)

#### Installation

###### pip

```bash
pip install https://github.com/mpg-age-bioinformatics/AGEpy/archive/0.6.0.tar.gz --user
```

###### github

Get the latest release from github:

```bash
git clone https://github.com/mpg-age-bioinformatics/AGEpy
```

Install:

```bash
cd AGEpy
python setup.py install --user
```

and then update to the latest release whenever required with:

```bash
cd AGEpy
git pull
python setup.py install --user --force

```

Alternatively you can also install the package with a symlink, so that changes
to the source files will be immediately available to users of the package on
your system:

```bash
cd AGEpy
python setup.py develop --user
```

Be aware that with the develop option you won't be able to properly update once new scripts are added.

#### Example usage

```python
import AGEpy as age

gtf=age.readGTF("/path/to/file.gtf")

gtf.head()
```

#### Help

In bash:

```bash
pydoc AGEpy.AGEpy
```

In python:

```python
help("AGEpy.AGEpy")
```

#### Scripts

* `david` a script to perform enrichment analysis from the DAVID database.
The usage is described in the script's help output called via `david --help`.
More information at: https://github.com/mpg-age-bioinformatics/AGEpy/wiki/david

* `bit` The [b]ermuda [i]nformation [t]riangle is a git-based tool for the management of code and data.
Check out https://github.com/mpg-age-bioinformatics/AGEpy/wiki/bit
