import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/matael/.virtualenvs/haumtalks/local/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/haumtalks')
sys.path.append('/home/haumtalks/haumtalks')

os.environ['DJANGO_SETTINGS_MODULE'] = 'haumtalks.settings'

# Activate your virtual env
activate_env=os.path.expanduser("/home/matael/.virtualenvs/haumtalks/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
