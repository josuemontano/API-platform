import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'psycopg2',
    'marshmallow',
    'PyJWT',
    'pyramid_jwt',
    'requests',
    'alembic',
    'apscheduler',
    'rollbar'
    ]

tests_require = [
    'pytest',
    'pytest-mock',
    'factory_boy',
    'freezegun',
    'pytest-cov',
    ]


setup(name='canopus',
      version='1.1',
      description='canopus',
      long_description=README,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Josue Montano',
      author_email='josuemontanoa@gmail.com',
      url='',
      keywords='web pyramid pylons rest api angularjs',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = metropolitan:main
      """,)
