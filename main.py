def pairs_of_players(h_in):
    import json
    import requests

    response = requests.get("https://mach-eight.uc.r.appspot.com/")
    file = response.json()
    values = list(file.values())
    values = values[0]

    pairs = [ [(i["first_name"], i["last_name"]), (j["first_name"], j["last_name"])] for i in values for j in values if int(i["h_in"]) + int(j["h_in"]) == h_in ][::2]
    if len(pairs)>1:
        answer =""
        for p in pairs:
            answer = answer + str("- " + " ".join(p[0]) + " "*4 + " ".join(p[1])) + "\n"
        return answer
    else:
        return("No matches found")

##commented lines to allow unit tests to work correctly. Please remove the # below in case of executing the code
#h_in = int(input("Hello an Welcome to the App!\nPlease enter a number to see the pairs of players: "))
#print(pairs_of_players(h_in))