from setuptools import setup
import os
setup(
    name = 'luna23',
    version = '0.1.0',
    packages = [os.path.dirname(os.path.abspath(__file__))+'/luna23'],
    entry_points = {
        'console_scripts' : [
            'luna23 = luna23.__main__:main'
            ]


    }






)

