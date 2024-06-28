from setuptools import setup, find_packages

setup(
    name='exchange-rates-selim',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'flask',
        'flasgger'
    ],
    entry_points={
        'console_scripts': [
            'exchange-rates-selim-cli = exchange-rates-selim.app:cli',
        ],
    },

    author='selimerdinc',
    author_email='serdinc10@gmail.com',
    description='A Python library for fetching exchange rates.',
    license='MIT',
    url='https://github.com/selimerdinc/exchange-rates-selim',
)
