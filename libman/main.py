import subprocess, sys, os, csv, shutil, time, webbrowser


def check_current_path():
    current_folders = os.listdir(os.curdir)
    needed_folders = ['libadmin', 'libman', 'library', 'manage.py', 'media', 'requirements.txt', 'users']
    missing_folders = [
        folder
        for folder in needed_folders
        if folder not in current_folders
    ]
    if len(missing_folders):
        print("This file is not present in correct folder")
        time.sleep(5)
        sys.exit()
    else:
        print("File is in correct path")


def check_python_installed():
    try:
        if sys.version_info.major == 3:
            print('Python 3 is installed')
        else:
            print('Python 3 is not installed.')
            time.sleep(5)
            sys.exit()
    except Exception as e:
        print('Error: {}'.format(e))
        time.sleep(5)
        sys.exit()
    return True



def check_django_installed():
    try:
        import django
    except Exception as e:
        command = "pip install django==3.2.25"
        subprocess.run(command, shell=True)
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libman.settings')
        django.setup() 
        version = django.VERSION
        print("  Django - {} is installed".format(django.__version__))
    if version[0] < 3:
        print("  Install Django version >= 3.2.25")
        time.sleep(5)
        sys.exit()
    return True


def install_requirements():
    command = "pip install -r requirements.txt"
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print("  - {}".format(e))
        time.sleep(5)
        sys.exit()
    return True

def check_database_exists():
    current_folders = os.listdir(os.curdir)
    if 'db.sqlite3' in current_folders:
        print("  Database exists")
    else:
        print("  Database does not exists")
        print("Creating a new database")
        create_dummy_database()
    return True

def remove_files(folder_path, ftype="pyc"):
    caches = "{}/__pycache__".format(folder_path)
    if os.path.exists(caches):
        shutil.rmtree(caches)

    for filename in os.listdir(folder_path):
        if filename == '__init__.py':
            continue
        if filename.endswith('.'+ ftype):
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
            print('{} deleted.'.format(file_path))   

def create_dummy_database():
    if os.path.exists('db.sqlite3'):
        os.remove('db.sqlite3')

    remove_files('./library/migrations')
    remove_files('./users/migrations')

    from library.models import Book
    subprocess.run('python manage.py makemigrations')
    subprocess.run('python manage.py migrate')

    with open('books.csv', mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            code = row[0].strip()
            title = row[1].strip()
            author = row[2].strip()
            summary = row[3].strip()
            b = Book(
                title=title,
                author=author,
                book_code=code,
                summary=summary)
            b.save()
            print("  Adding Book - {}".format(title))
    from django.contrib.auth import get_user_model
    User = get_user_model()
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print("  Creating Admin credentials")
    print("  Username - admin")
    print("  Password - admin")
    from django.contrib.auth.models import User
    for i in range(1, 21):
        print(f"   Adding User{i} - password123")
        u = User.objects.create_user(f'user{i}', f'user{i}@example.com', 'password123')
        u.save()


        

def run_project():
    print("  Starting APP")
    webbrowser.open("http://127.0.0.1:8000/")
    subprocess.run("cls", shell=True)
    subprocess.run("python manage.py runserver")



if __name__ == '__main__':
    print("Checking system requirements")
    check_current_path()
    check_python_installed()
    install_requirements()
    check_django_installed()
    check_database_exists()
    run_project()
    time.sleep(5)
