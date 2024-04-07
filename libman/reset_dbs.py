import os

os.remove("db.sqlite3")
os.chdir("./users/migrations")
for f in os.listdir("."):
    if f != "__init__.py":
        os.remove(f)
os.chdir("../../")

os.chdir("./library/migrations")
for f in os.listdir("."):
    if f != "__init__.py":
        os.remove(f)
os.chdir("../../")
