import requests
import sys
import os
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
    r = requests.get(url + "patch/" + id)
    data = r.json()
    if data["downloadableExec"]:
        r = requests.get(data["github"].replace("https://github.com/", "https://api.github.com/repos/") + "/releases/latest")
        githubData = r.json()
        # Download
        u = githubData["assets"][0]["browser_download_url"]
        r = requests.get(u)
        with open(id, "wb") as f:
            f.write(r.content)
        os.system("chmod +x " + id)
        os.system("./" + id)
    else:
        print("Not downloadable")
        # Try to clone
        os.system("git clone " + data["github"])
        os.system("cd " + id + "&& chmod +x install.sh && ./install.sh")
    # https://api.github.com/repos/Stoppedwumm/halflife2patcher/releases/latest
    