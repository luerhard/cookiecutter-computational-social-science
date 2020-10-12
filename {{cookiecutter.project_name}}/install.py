from pathlib import Path
import os
import subprocess
import textwrap


def run_command(command):
    output = subprocess.check_output(
        command,
        stderr=subprocess.PIPE,
        shell=True,
        text=True,
    )
    print(output)

print("Installing environment ...")
run_command("conda env create --name {{cookiecutter.project_name}} --file env.yaml")
run_command("conda run --name {{cookiecutter.project_name}} pre-commit install")

with open(".git/hooks/pre-commit", "a") as f:
    f.write(textwrap.dedent("""
    import subprocess
    out = subprocess.check_output('exec dvc git-hook pre-commit $0', stderr=subprocess.PIPE, shell=True)
    print(out)
    """))

with open(Path(".git/hooks/pre-push"), "w") as f:
    f.write(textwrap.dedent("""
    #!/bin/sh
    exec dvc git-hook pre-push $0
    """))

with open(Path(".git/hooks/post-checkout"), "w") as f:
    f.write(textwrap.dedent("""
    #!/bin/sh
    exec dvc git-hook post-checkout $0
    """))

if os.name == "posix":
    run_command("chmod +x .git/hooks/post-checkout")
    run_command("chmod +x .git/hooks/pre-push")

