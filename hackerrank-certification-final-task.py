import requests


def getTotalGoals(year, winner, competition, num):
    goals = 0
    url = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&competition={competition}&team{num}={winner}&&page=1'
    response = requests.get(url)
    data = response.json()
    total_pages = data['total_pages']
    temp = data['data']
    for d in temp:
        goals += int(d[f'team{num}goals'])
    for page in range(2, total_pages+1):
        url = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&competition={competition}&team{num}={winner}&&page={page}'
        response = requests.get(url)
        data = response.json()
        temp = data['data']
        for d in temp:
            goals += int(d[f'team{num}goals'])
    return goals

def getWinnerTotalGoals(competition, year):
    url = f'https://jsonmock.hackerrank.com/api/football_competitions?name={competition}&year={year}'
    response = requests.get(url)
    data = response.json()
    winner = data['data'][0]['winner']
    goals = 0
    goals += getTotalGoals(year, winner, competition, 1)
    goals += getTotalGoals(year, winner, competition, 2)
    return goals

print(getWinnerTotalGoals('English Premier League', 2011))
