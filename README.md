# A sample Flask Api project

A sample project using Flask, and flask_restful to take requests that include a package, its version, and the hostname it's installed on and respond with the hostnames and their CVEs.

Due to dependacies that are available in live PyPI instead of TestPyPI, please install the package without dependancies and then install dependancies separately:

```python
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps api_app
python3 -m pip install Flask flask-restful pandas
```
# sample_api_app
