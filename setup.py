#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(name='venturer',
      version='0.1.0',
      description='A game designed to teach you AI from the ground up',
      long_description=long_description,
      classifiers=[
          'Programming Language :: Python',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Development Status :: 1 - Planning',
          'Environment :: Console',
          'Intended Audience :: Education',
          'Topic :: Education :: Computer Aided Instruction (CAI)',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Topic :: Games/Entertainment :: Puzzle Games'
      ],
      keywords='artificial intelligence game neural network svm classifier',
      url='https://www.github.com/useanalias/venturer',
      author='use.an.alias',
      author_email='use.an.alias@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[],
      entry_points={
          'console_scripts': [
              'venturer = venturer.game:main'
          ],
      }
)