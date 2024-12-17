import requests
import sys
import os
import subprocess
import tempfile
url = "https://macpatch-registry.vercel.app/"
print(len(sys.argv))
if len(sys.argv) >= 2:
    if sys.argv[1] == "--dev":
        url = "http://localhost:3000/"

def search(name):
    # Returns all packages in the style [{name: "name", id: "id"}]
    # Search in name AND id, also include closest matches
    r = requests.get(url)
    packages: list[dict[name: str, id: str]] = r.json()
    matches = []
    for package in packages:
        if name.lower() in package["name"].lower() or name.lower() in package["id"].lower():
            matches.append(package)
    return matches

def download(id):
    # Ask user for permissions
    while True:
        ex = input("Are you sure you want to install this patch? This will run code and cmd commands. Use C to see these commands (y/n/c) ")
        if ex == "n":
            print("Patch aborted")
            exit(0)
        elif ex == "c":
            print("Commands:")
            print("If the patch has prebuilt binaries:")
            print("chmod +x [TEMPDIR]/[EXECUTABLE]")
            print("./[TEMPDIR]/[EXECUTABLE]")
            print("Else:")
            print("git clone [GITHUB]")
            print("cd [TEMPDIR]/[REPO]")
            print("chmod +x install.sh")
            print("./install.sh")
            print("For all:")
            print("rm -rf [TEMPDIR]")
        elif ex == "y":
            break
        else:
            print("Invalid input")


    tmp = tempfile.mkdtemp(prefix="hyperPatch_")
    r = requests.get(url + "patch/" + id)
    data = r.json()
    if data["downloadableExec"]:
        r = requests.get(data["github"].replace("https://github.com/", "https://api.github.com/repos/") + "/releases/latest")
        githubData = r.json()
        # Download
        u = githubData["assets"][0]["browser_download_url"]
        r = requests.get(u)
        with open(os.path.join(tmp, id), "wb") as f:
            f.write(r.content)
        print("CHMOD OUTPUT:", subprocess.run(["chmod +x " + os.path.join(tmp, id)], shell=True).stdout)
        subprocess.run(["./" + os.path.join(tmp, id)], shell=True)
    else:
        print("Not downloadable")
        # Try to clone
        print("GIT CLONE OUTPUT:", subprocess.run(["git clone" + data["github"]], shell=True).stdout)
        repoName = data["github"].split("/")[-1]
        print("INSTALL SCRIPT OUTPUT:", subprocess.run(["cd" + os.path.join(tmp, repoName) + "&& chmod +x install.sh && ./install.sh"], shell=True))
    print("LIST:", subprocess.run(["ls " + tmp], shell=True).stdout)
    subprocess.run(["rm -rf " + tmp], shell=True)
    # https://api.github.com/repos/Stoppedwumm/halflife2patcher/releases/latest
    