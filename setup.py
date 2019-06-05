from setuptools import setup

setup(name='pyAudioAnalysis',
      version='0.2.6',
      description='Python Audio Analysis Library: Feature Extraction, Classification, Segmentation and Applications',
      url='https://github.com/tyiannak/pyAudioAnalysis',
      author='Theodoros Giannakopoulos',
      author_email='tyiannak@gmail.com',
      license='Apache License, Version 2.0',
      packages=['pyAudioAnalysis'],
      install_requires=[
            'eyed3',
            'libmagic',
            'python-magic', #brew install libmagic on osx
            'numpy',
            'pydub',
            'scipy',
            'sklearn',
            'matplotlib',
            'hmmlearn',
      ],
      zip_safe=False)
