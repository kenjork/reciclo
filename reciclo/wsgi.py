"""
WSGI config for reciclo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from whitenoise import WhiteNoise
from reciclo import MyWSGIApp


from django.core.wsgi import get_wsgi_application



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reciclo.settings')

application = get_wsgi_application()

application = MyWSGIApp()

application = WhiteNoise(application, root='/staticfile/')
application.add_files('/static/', prefix='more-files/')

