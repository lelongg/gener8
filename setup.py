# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='gener8',
    version='0.2.0',
    description='Simple yet powerful universal scaffolding tool',
    author='Gérald Lelong',
    author_email='lelong.gerald@gmail.com',
    url='https://github.com/lelongg/gener8',
    scripts = [
        'gener8'
    ],
    install_requires=[
        'pyyaml',
        'empy'
    ],
)
