from setuptools import setup, find_packages

setup(name='dev_aberto_leonardopaloschi',
    version='0.1',
    packages=['dev_aberto'],
    install_requires=['requests','setuptools'],
    scripts=['scripts/hello.py'],
    )
