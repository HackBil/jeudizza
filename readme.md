Jeudizza
========

Setup 
-----
> This setup is mainly intended for the engine-coder.

* `git clone git@github.com:HackBil/jeudizza.git` : retrieve the repo
* `cd jeudizza`
* `virtualenv -p python3 --no-site-packages .v_env` : create a virtual-env for python code
* `source .v_env/bin/activate` : activate the v_env.
* `pip install -r requirements.txt` : install all requirements
* `./manage.py loaddata seed.json` : seed DB with data
* `./manage.py migrate` : create and migrate DB
* `./manage.py createsuperuser` : add your own admin. Or you can use the seeded admin.

```sh
git clone git@github.com:HackBil/jeudizza.git
cd jeudizza
virtualenv --no-site-packages .v_env
source .v_env/bin/activate
pip install -r requirements.txt
./manage.py loaddata seed.json
./manage.py migrate
./manage.py createsuperuser
```

Running
-------
* `./manage.py runserver`
* Access `http://127.0.0.1:8000` with your browser. The admin is on `http://127.0.0.1:8000/admin/`.
