import json
import requests

response = requests.get("https://mach-eight.uc.r.appspot.com/")
file = response.json()
values = list(file.values())
values = values[0]

def pairs_of_players(h_in):
    pairs = [  ( " ".join((i["first_name"], i["last_name"])), " ".join((j["first_name"], j["last_name"])) ) for i in values for j in values if int(i["h_in"]) + int(j["h_in"]) == h_in ]
    if len(pairs)>1:
        for i in pairs:
            for j in pairs:
                if ((i[0] == j[1] and i[1]==j[0] and pairs.index(j) > pairs.index(i)) or (j[0]==j[1])):
                    pairs.remove(j)
        answer =""
        for p in pairs:
            answer = answer + "- " + p[0] + " "*9 + p[1] + "\n"
        return answer
    else:
        return("No matches found")
##commented lines to allow unit tests to work correctly. Please remove the # below in case of executing the code
#h_in = int(input("Hello an Welcome to the App!\nPlease enter a number to see the pairs of players: "))
#print(pairs_of_players(h_in))