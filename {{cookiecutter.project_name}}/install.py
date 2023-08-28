import subprocess

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    while process.stdout.readable():
        line = process.stdout.readline()
        if not line:
            break
        print(line.decode().strip())


print("Installing environment ...")
run_command("poetry install")
print("Install pre-commit ...")
run_command("pre-commit install --hook-type pre-commit --hook-type post-checkout --hook-type pre-push")

