from setuptools import setup


setup(
    name='documd',
    version='0.0.1',
    author='Brian Hines',
    author_email='brian@projectweekend.net',
    description='Simple markdown documentation from docstrings',
    url='https://github.com/projectweekend/documd',
    packages=['documd'],
    install_requires=[],
    entry_points='''
        [console_scripts]
        documd=documd:cli
    ''',
)
