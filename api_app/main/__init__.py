from flask import request, jsonify
from flask_restful import Resource
import os
import pandas as pd
from packaging.version import parse
from .errors import InvalidHostNameError


basedir = os.path.abspath(os.path.dirname(__file__))

# read in cve.csv file and convert it to a dict
cve_file = pd.read_csv(os.path.join(
    basedir, '..', 'data/cve.csv'), index_col=0)
cve_dict = cve_file.to_dict('index')


class CveApi(Resource):
    def post(self):

        received_json = request.get_json()
        cve_list = []
        hostname = []

        # looping through each json mesaage to get data
        for message in received_json:
            package = message['package']
            version = message['version']
            host = message['host']

            # loop though dict to determine whether the package is vulnerable or not
            for key in cve_dict:
                if cve_dict[key]["package"] == package:
                    if parse(version) >= parse(cve_dict[key]["vulnerable_version"]) \
                            and parse(version) < parse(cve_dict[key]["patched_version"]):
                        cve_list.append(key)

            hostname.append(host)

        # check to make sure host names are consistent in each post data
        if len(set(hostname)) == 1:
            hostname_out = hostname[0]
        else:
            raise InvalidHostNameError

        # if list if empty then return empty json
        if not cve_list:
            return {}, 200
        # else return json with host name and list of cve ids
        else:
            return {hostname_out: cve_list}, 200
