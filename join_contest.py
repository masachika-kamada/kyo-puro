import shutil


contest_name = input("input contest name: ")
q = "abcd"
for i in range(len(q)):
    shutil.copy("./stdin_template.py", f"src/{contest_name}_{q[i]}.py")
