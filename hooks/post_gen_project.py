import subprocess
import sys

print("Intializing git repository ...")
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
subprocess.call(['git', 'remote', 'add', 'origin', '{{cookiecutter.repo_url}}'])
subprocess.call([sys.executable, "install.py"])
