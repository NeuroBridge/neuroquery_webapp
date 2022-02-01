##########################################################################
#
# This code just provides a Flask wrapper around the Neuroquery search. See
#
# https://neuroquery.org/
#
# and specifically
#
# https://github.com/neuroquery/neuroquery/blob/main/examples/examples_src/minimal_example.py
#
# Here's an example query:
#
#    http://localhost:13374/query?searchTerms=schizophrenia
#
#  To start the server use: python neuroquery_webapp.py
#  The port and host are defined in config.py
##########################################################################
from flask import Flask, request
from flask_cors import CORS
import sys
from timeit import default_timer as timer
from neuroquery import fetch_neuroquery_model, NeuroQueryModel
import pandas

# Define the app
app = Flask(__name__)
# Load configs
app.config.from_object('config')
# Set CORS policies
CORS(app)

@app.route("/query", methods=["GET"])
def qa():

    records = []

    # API to return top_n matched records for a given query
    if request.args.get("searchTerms"):
        userQuery = request.args.get("searchTerms")

        encoder = NeuroQueryModel.from_data_dir(fetch_neuroquery_model())
        result = encoder(userQuery)

        # we want to return the title and the pubmed_url
        for index,row in result["similar_documents"].iterrows():
           records.append({'pmid': row['pmid'], 'title': row['title'], 'pubmed_url': row['pubmed_url'], 'similarity': row['similarity']})

    else:
        return {"error": "Couldn't process your request"}, 422
    return {"data": records}

if __name__ == '__main__':
    listenPort = app.config['SEARCH_PORT']
    app.run(debug=True, host="0.0.0.0", port=listenPort)
