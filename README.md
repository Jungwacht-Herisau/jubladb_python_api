# JublaDB Python API
A package with generated code to access the [Jubla DB](https://db.jubla.ch) API with Python code.

For more information, please visit [the project page](https://github.com/Jungwacht-Herisau/jubladb_python_api)

## Requirements.

Python 3.10+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install it directly using:

```sh
pip install git+https://github.com/Jungwacht-Herisau/jubladb_python_api.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Jungwacht-Herisau/jubladb_python_api.git`)

Then import the package:
```python
import jubladb_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import jubladb_api
```