Jeudizza
========

Setup 
-----
> This setup is mainly intended for the engine-coder.
> If you've never played a Kingdoms game before, you should really try it. Although the code is heavily documented and pretty simple to understand, core concepts of the games lies in its scripting engine; making this engine-code quite abstract to starts with.

* `git clone git@github.com:HackBil/jeudizza.git` : retrieve the repo
* `cd jeudizza`
* `virtualenv --no-site-packages .v_env` : create a virtual-env for python code
* `source .v_env/bin/activate` : activate the v_env.
* `pip install -r requirements.txt` : install all requirements
* `./manage.py syncdb ` : create DB
* `./manage.py migrate` : migrate DB

```sh
git clone git@github.com:HackBil/jeudizza.git
cd jeudizza
virtualenv --no-site-packages .v_env
source .v_env/bin/activate
pip install -r requirements.txt
./manage.py syncdb
./manage.py migrate
```

Running
-------
* `./manage.py runserver`
* Access `http://127.0.0.1:8000` with your browser. The admin is on `http://127.0.0.1:8000/admin/`.
