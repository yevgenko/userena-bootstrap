from setuptools import setup, find_packages
import sys

readme_file = 'readme.mkd'
try:
    long_description = open(readme_file).read()
except IOError, err:
    sys.stderr.write("[ERROR] Cannot find file specified as "
        "``long_description`` (%s)\n" % readme_file)
    sys.exit(1)

setup(name='userena-bootstrap',
      version=0.1,
      description='Complete user management application for Django',
      long_description=long_description,
      zip_safe=False,
      author='Rich Atkinson',
      author_email='rich@piran.com.au',
      url='https://github.com/piran/userena-bootstrap',
      download_url='https://github.com/piran/userena-bootstrap/downloads',
      packages = find_packages(exclude=['demo_project', 'demo_project.*']),
      include_package_data=True,
      install_requires = [
        'Django>=1.2.1',
        'django-userena>=1.0.2',
        'django-bootstrap-form>=2.0.5',
      ],
      classifiers = ['Development Status :: 2 - Pre-Alpha',
                     'Environment :: Web Environment',
                     'Framework :: Django',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: BSD License',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python',
                     'Topic :: Utilities'],
      )

