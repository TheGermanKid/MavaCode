## THIS FILE HAS BEEN AUTOGENERATED FOR USE WITH CATKIN AND IS NOT SUPPOSED TO BE TRACKED BY GIT!
## DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(package_xml_path='/home/capstone/autoware.ai/src/vendor/lanelet2/lanelet2_python',
    packages=['lanelet2'],
    package_data={'': ['*.so*']},
    package_dir={'': '/home/capstone/autoware.ai/build/lanelet2_python/devel/lib/python2.7/dist-packages'})

setup(**setup_args)
