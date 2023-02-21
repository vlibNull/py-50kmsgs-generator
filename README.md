# py-500kmsgs-generator

# basics:
- running ``500kmsgsmockusers.py`` with the appropriate requirements (pref in venv) will create
- a ``messages.db`` if it doesn't exist, and then add 500k entries of mock user data generated with ``faker lib``
- includes basic flash server to view and paginate the generated data in ``messages.db``
- use ``flask run`` in the root of the project folder to run ``app.py`` as a debuggable flask server.
- defaults to ``127.0.0.1:5000``