from services.file_service import FileService
if __name__ == "__main__":
    src = "./app/src/main/files"
    dest = "./app/src/lang"
    file = FileService(src, dest)
    file.make_group()