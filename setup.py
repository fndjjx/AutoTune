#-*- encoding: UTF-8 -*-
from setuptools import setup

setup(
    name = "AutoTune",          
    version = "0.1",              
    packages = ['autotune'],  
    include_package_data=True,    
    zip_safe=True,                
    install_requires = [        
    'deap',
    ]
 )
