import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, 'demonstrare'))
config = os.path.join(here, 'production.ini')

from pyramid.paster import get_app
application = get_app(config, 'main')
