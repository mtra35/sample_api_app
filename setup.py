from setuptools import find_packages, setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='api_app',
    version='0.1.0',
    description='A sample Flask Api project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Minh Tra',
    author_email='mtra35@gmail.com',
    url='https://github.com/mtra35/sample_api_app.git',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='sample flask api',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sample=api_app:app',
        ],
    },
    include_package_data=True,
    install_requires=[
        'Flask>=1.1.2',
        'Flask-RESTful>=0.3.8',
        'pandas>=1.0.3',
        'packaging==20.4',
    ]
)
