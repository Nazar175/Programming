from jikanpy import Jikan

jikan = Jikan()

data = jikan.seasons(year=2026, season="winter")

for anime in data["data"]:
    title = anime["titles"][0]["title"]
    score = anime["score"]
    print(f"{title} — рейтинг: {score}")