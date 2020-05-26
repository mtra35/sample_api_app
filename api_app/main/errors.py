class InvalidHostNameError(Exception):
    pass


errors = {
    "InvalidHostNameError": {
        "message": "The hostnames provided are invalid or inconsistent",
        "status": 400,
    }
}
