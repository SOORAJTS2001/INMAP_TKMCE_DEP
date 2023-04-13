import os
import sys
import subprocess

def main():
    # Change to the directory containing your script
    os.chdir('INMAPWEB_DEP/the_destroyer.py')

    # Run your script
    subprocess.call([sys.executable, 'the_destroyer.py'])

if __name__ == '__main__':
    main()
