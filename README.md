# A sample Flask Api project

A sample project using Flask, and flask_restful to take requests that include a package, its version, and the hostname it's installed on and respond with the hostnames and their CVEs.

Due to dependacies that are available in live PyPI instead of TestPyPI, please install the package without dependancies and then install dependancies separately:

```python
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps api_app
python3 -m pip install Flask flask-restful pandas packaging
```

# Run the application

[Source](https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/)

For Linux and Mac:

```
$ export FLASK_APP=api_app
$ flask run
```

For Windows cmd, use **set** instead of **export**:

```
> set FLASK_APP=api_app
> flask run
```
