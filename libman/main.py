import subprocess, sys, os, csv, shutil

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libman.settings')
django.setup() 

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
        sys.exit()
    return True


def check_python_installed():
    try:
        if 'windows' in sys.platform.lower():
            output = subprocess.check_output(['where', 'python']).strip().decode()
        else:
            output = subprocess.check_output(['which', 'python'], universal_newlines=True)

        if output:
            print('✔️  Python 3 is installed')
        else:
            print('❌  Python 3 is not installed.')
            sys.exit()
    except Exception as e:
        print('Error: {}'.format(e))
        sys.exit()
    return True



def check_django_installed():
    try:
        import django
    except Exception as e:
        print(e)
        sys.exit()
    else:
        version = django.VERSION
        print("✔️  Django - {} is installed".format(django.__version__))
    if version[0] < 3:
        print("❌  Install Django version >= 3.2.25")
        sys.exit()
    return True


def install_requirements():
    command = "pip install -r requirements.txt"
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print("❌  - {}".format(e))
        sys.exit()
    return True

def check_database_exists():
    current_folders = os.listdir(os.curdir)
    if 'db.sqlite3' in current_folders:
        print("✔️  Database exists")
    else:
        print("❌  Database does not exists")
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
            print(f'{file_path} deleted.')   

def create_dummy_database():
    if os.path.exists('db.sqlite3'):
        os.remove('db.sqlite3')

    remove_files('./library/migrations')
    remove_files('./users/migrations')

    from library.models import Book
    subprocess.run('python manage.py makemigrations')
    subprocess.run('python manage.py migrate')

    with open('dummy.csv', mode="r") as csv_file:
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
            print("✔️  Added Book - {}".format(title))
    from django.contrib.auth import get_user_model
    User = get_user_model()
    User.objects.create_superuser('admin', '', 'admin')
    print("✔️  Creating Admin credentials")
    print("✔️  Username - admin")
    print("✔️  Password - admin")
        

def run_project():
    print("✔️  Starting APP")
    subprocess.run("cls", shell=True)
    subprocess.run("python manage.py runserver")



if __name__ == '__main__':
    print("Checking system requirements")
    check_current_path()
    check_python_installed()
    check_django_installed()
    install_requirements()
    check_database_exists()
    run_project()