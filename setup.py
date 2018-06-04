# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name='iNLP',
    version='1.0.0',
    url='https://github.com/Jie-Yuan/iNLP',
    keywords=["iNLP", "313303303@qq.com"],
    
    description=('NLP human utils'),
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='JieYuan',
    author_email='313303303@qq.com',
    maintainer='JieYuan',
    maintainer_email='313303303@qq.com',
    license='MIT',
    include_package_data=True,
    platforms=["all"],
    python_requires='>=2.7, <4',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ]
)
