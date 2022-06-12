from setuptools import setup

setup(
    name='itunes-image-repairer',
    version='0.1',
    description='iTunes for Windows can mangle the headers of PNG/JPEG images embedded in mp3 files by adding extra null bytes. This is a Python script that will remove these extra bytes and fix the artwork permanently.',
    author='Duncan Walker',
    packages=['itunes-image-repairer'],
    install_requires=['eyed3', 'tqdm'],
    scripts=['itunes-image-repairer/repair-itunes-images']
)
