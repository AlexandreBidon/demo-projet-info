
nom_film = ""

def click_button():
    requests.get("/rechercher_film/" + nom_film, headers=headers)
