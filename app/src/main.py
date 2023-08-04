from services.file_service import FileService
if __name__ == "__main__":
    src = "../app/main/files"
    dest = "../app/lang"
    file = FileService(src, dest)
    file.make_group()