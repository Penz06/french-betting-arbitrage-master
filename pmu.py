from bs4 import BeautifulSoup
import requests

def get_page():
	url = "https://paris-sportifs.pmu.fr/pari/competition/169/football/ligue-1-conforama"
	response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"})
	html = BeautifulSoup(response.content, 'html.parser')
	return html

def get_games():
	html = get_page()
	games = []
	game_elements = html.select(".pmu-event-list-grid-highlights-formatter-row")
	for el in game_elements:
		game_name = el.select(".trow--event--name")[0].text
		game_name = "".join(game_name.split())
		team1, team2 = game_name.split("//")
		odds_el = el.select(".hierarchy-outcome-price")
		odds = []
		for el2 in odds_el:
			tmp = "".join(el2.text.split()).replace(",", ".")
			odds.append(float(tmp))
		games.append({
			'team1': team1,
			'team2': team2,
			'odds': odds
		})
	return games
