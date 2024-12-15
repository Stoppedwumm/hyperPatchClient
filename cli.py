import rq
def main():
    s = input("Enter game name to search for: ")
    search = rq.search(s)
    # Ask user which game they want to install
    print("===========")
    print("Games found:")
    for i in range(len(search)):
        print(f"{i + 1}: {search[i]['name']}")
    print("===========")
    game = input("Enter the number of the game you want to install: ")
    game = search[int(game) - 1]
    rq.download(game["id"])
    print("Auto patched!")
    
    
    