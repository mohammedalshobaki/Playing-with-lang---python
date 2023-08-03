import os

class File:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

  # Groups files into sub-folders based on language
    def make_group(self):
        files = os.listdir(self.src)
        for file in files:
            language, number = file.split("-")
            language_dir = os.path.join(self.dest, language)
            if not os.path.exists(language_dir):
                os.mkdir(language_dir)
            os.rename(os.path.join(self.src, file), os.path.join(language_dir, file))

if __name__ == "__main__":
    src = "./app/main/files"
    dest = "./app/lang"
    file = File(src, dest)
    file.make_group()