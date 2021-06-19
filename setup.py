from setuptools import setup
setup(
    name = 'luna23',
    version = '0.1.0',
    packages = ['luna23'],
    entry_points = {
        'console_scripts' : [
            'luna23 = luna23.__main__:main'
            ]


    }






)

