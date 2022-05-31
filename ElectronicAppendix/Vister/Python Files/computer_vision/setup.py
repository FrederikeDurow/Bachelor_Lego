from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup
d = generate_distutils_setup(
    packages=['Vister_Classes'],
    package_dir={'': 'computer_vision/scripts/Nodes'}
)
setup(**d)