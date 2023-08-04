# File Grouper

File Grouper is a Python script that groups files in a source directory into sub-folders based on language codes found in the file names. It helps organize files by language, making it easier to manage and access them.

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/mohammedalshobaki/Playing-with-lang---python
```
```bash
cd Playing-with-lang---python/app/src
```

2. Install the required dependencies (if any):

3. Customize the `src` and `dest` variables in the `main.py` file:

```python

# Set the source directory containing files to be grouped
src = "../app/main/files"

## Set the destination directory where files will be grouped by language
dest = "../app/lang"
```
1. Run the main.py script:
```bash
python main.py
```

The script will group the files from the src based on the language codes in their names and move them into the corresponding sub-folders in the dest.

## Requirements
Python 3.x

## Developer
Mohammed Alshobaki# Playing-with-lang---python
