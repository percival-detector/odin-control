from setuptools import setup

setup(
    name="odin",
    version='0.1',
    description='ODIN detector server',
    url='https://github.com/timcnicholls/odin',
    author='Tim Nicholls',
    author_email='tim.nicholls@stfc.ac.uk',
    scripts=[
        'server.py',
    ],
    packages=[
        'app',
    ],
    entry_points={
        'console_scripts' : [
            'odin_server = server:main',
        ],
    },
    setup_requires=[
        'nose>=1.0'
    ],
    install_requires=[
        'tornado>=4.3',
    ],

)
