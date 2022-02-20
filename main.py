import json
import requests
response = requests.get("https://mach-eight.uc.r.appspot.com/")
file = response.json()
values = list(file.values())
values_sorted = sorted(values[0], key = lambda p: p["h_in"])

def pairs_of_players(h_in):
    if (h_in < int(values_sorted[0]["h_in"]) + int(values_sorted[1]["h_in"]))  or (h_in > int(values_sorted[-2]["h_in"]) + int(values_sorted[-1]["h_in"]))  :
        return("No matches found")
    else:
        pairs = [  ( " ".join((i["first_name"], i["last_name"])), " ".join((j["first_name"], j["last_name"])) ) for i in values_sorted for j in values_sorted if int(i["h_in"]) + int(j["h_in"]) == h_in ]
        unique_pairs = dict(set(tuple(sorted(x)) for x in pairs))
        if len(unique_pairs)==0:
            return ("No matches found")
        return (unique_pairs)
def format_output(dicti):
    try:
        for k, v in dicti.items():
            print("- {:<20} {:<20}".format(k,v))
    except:
        print(dicti)

##commented lines to allow unit tests to work correctly. Please remove the # below in case of executing the code
#h_in = int(input("Hello and Welcome to the App!\nPlease enter a number to see the pairs of players: "))
#format_output(pairs_of_players(h_in))