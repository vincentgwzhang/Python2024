with open("example.txt", "r") as file:
    content = file.read()



from zipfile import ZipFile
with ZipFile("example.zip", "w") as zipf:
    zipf.write("file1.txt")
    zipf.write("file2.txt")



import sqlite3
with sqlite3.connect("example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")




import threading
lock = threading.Lock()
def thread_safe_function():
    with lock:
        print("Thread-safe operation")

##################################################
class FileManager:
    def __init__(self, filename, mode):
        print("functon __init__ triggered")
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("functon __enter__ triggered")
        self.file = open(self.filename, self.mode)
        return self.file  # 返回文件对象

    def __exit__(self, exc_type, exc_value, traceback):
        print("functon __exit__ triggered")
        self.file.close()  # 确保文件关闭

# 使用 FileManager
with FileManager("textfile.txt", "w") as file:
    file.write("Hello, world!")
# 文件会自动关闭
