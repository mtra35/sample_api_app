from . import CveApi


def initialize_routes(api):
    api.add_resource(CveApi, '/vuln')
