# itunes-image-repairer
iTunes for Windows can mangle the headers of PNG/JPEG images embedded in mp3 files by adding extra null bytes. This is a Python script that will remove these extra bytes and fix the artwork permanently.

## Installation
Once the repo has been cloned, run `pip install .` to install the package

## Usage
Once the package has been installed, run using:
```repair-itunes-images <directory>```

More options are available through the help text, accessed via
```repair-itunes-images <directory> -h```
