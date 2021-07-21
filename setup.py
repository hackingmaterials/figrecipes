#!/usr/bin/env python

from setuptools import setup, find_packages
import os

module_dir = os.path.dirname(os.path.abspath(__file__))

reqs_file = os.path.join(module_dir, "requirements.txt")
with open(reqs_file, "r") as f:
    reqs_raw = f.read()
reqs_list = [r.replace("==", ">=") for r in reqs_raw.split("\n")]

if __name__ == "__main__":
    setup(
        name='figrecipes',
        version='0.0.7',
        description='figrecipes is a tool for quickly creating interactive plots for data science.',
        long_description=open(os.path.join(module_dir, 'README.md')).read(),
        url='https://github.com/hackingmaterials/figrecipes',
        author='Anubhav Jain',
        author_email='anubhavster@gmail.com',
        license='modified BSD',
        packages=find_packages(),
        package_data={},
        zip_safe=False,
        install_requires=reqs_list,
        extras_require={},
        classifiers=['Programming Language :: Python :: 2.7',
                     'Development Status :: 4 - Beta',
                     'Intended Audience :: Science/Research',
                     'Intended Audience :: System Administrators',
                     'Intended Audience :: Information Technology',
                     'Operating System :: OS Independent',
                     'Topic :: Other/Nonlisted Topic',
                     'Topic :: Scientific/Engineering'],
        test_suite='figrecipes',
        scripts=[]
    )
