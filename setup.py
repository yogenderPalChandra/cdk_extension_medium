from distutils.core import setup
from setuptools import find_packages
from aws_cdk_extensions.__version__ import __version__

setup(
    name='your-cdk',
    version=__version__,
    python_requires='>=3.10',
    packages=find_packages(exclude=['*test']),
    package_data={'': ['py.typed']},
    author='yogender',
    url='https://pd.bitbucket.your_name.com/projects/your_name/repos/lib-cdk',
    install_requires=['constructs>=10.2.9', 'aws-cdk-lib>=2.77.0']
)
