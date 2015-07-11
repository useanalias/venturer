#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
      name = 'venturer',
      version = '0.1.0',
      packages = find_packages(),

      author = 'useanalias',
      author_email = 'use.an.alias@gmail.com',
      description = 'A game designed to teach you AI from the ground up',
      license = 'MIT',
      keywords = 'artificial intelligence game neural network svm classifier',
      url = 'https://www.github.com/useanalias/venturer',
      classifiers = ['Programming Language :: Python',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: OS Independent',
                     'Development Status :: 1 - Planning',
                     'Environment :: Console',
                     'Intended Audience :: Education',
                     'Topic :: Education :: Computer Aided Instruction (CAI)',
                     'Topic :: Scientific/Engineering :: Artificial Intelligence',
                     'Topic :: Games/Entertainment :: Puzzle Games'],

      entry_points = {
          'console_scripts': [
              'venturer = venturer.game:main'
          ],
      }
)