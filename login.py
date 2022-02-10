import time, json
import requests


def login(nation, password, main_nation):
    headers = {
        "User-Agent": f"Login script devved by nation=sweeze, in use by nation={main_nation}",
        "X-Password": password,
    }

    params = (
        ("nation", nation),
        ("q", "ping"),
    )

    response = requests.get(
        "https://www.nationstates.net/cgi-bin/api.cgi",
        headers=headers,
        params=params,
    )
    if response.status_code == 200:
        print(f"Successfully logged in as {nation}")
    else:
        print(f"Login to {nation} failed. Did you supply the right password?")


def main():
    with open("config.json", "r") as read_file:
        config = json.load(read_file)
    
    nations = config["nations"]
    
    for nation in nations:
        password = nations[nation]
        login(nation, password, config["main_nation"])
        time.sleep(30/50)

if __name__ == "__main__":
    main()
