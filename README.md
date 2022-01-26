# neuroquery_webapp
A simple flask server that front ends some basic neuroquery search function

This code just provides a Flask wrapper around the Neuroquery search. See

 https://neuroquery.org/

 and specifically

 https://github.com/neuroquery/neuroquery/blob/main/examples/examples_src/minimal_example.py

for more context.

Here's an example query:

   http://localhost:13374/query?searchTerms=schizophrenia

To start the server use: python neuroquery_webapp.py
The port and host are defined in config.py
