activate_this = "C:/Users/101180612/Envs/cmApp/Scripts/activate_this.py"
# execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(),dict(__file__=activate_this))

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir("C:/Users/101180612/Envs/cmApp/Lib/site-packages")




# Add the app's directory to the PYTHONPATH
sys.path.append("C:/Users/101180612/Envs/cmApp/CMserver/mysite")
sys.path.append("C:/Users/101180612/Envs/cmApp/CMserver/mysite/mysite")

os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()