# py-500kmsgs-generator

# basics:
- running ``500kmsgsmockusers.py`` with the appropriate requirements (pref in venv) will create
- a ``messages.db`` if it doesn't exist, and then add 500k entries of mock user data generated with ``faker lib``
- includes basic flash server to view and paginate the generated data in ``messages.db``
- use ``flask run`` in the root of the project folder to run ``app.py`` as a debuggable flask server.
- defaults to ``127.0.0.1:5000``   
- P.S. Forgive the main branch typo, it is 500k, but you can simply alter the range of the loop
- to alter the amount of entries it will create!
- P.S. P.S. -> to assist in getting this running, use ``pip install -r requirements.txt`` within a venv or on your system
- to acquire the necessary packages to run these scripts.
- -> could not include sample generation(s) of ``messages.db`` for file constraints.