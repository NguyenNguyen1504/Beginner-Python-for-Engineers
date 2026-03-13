import pandas as pd
# Stadium capacity for all EPL clubs (1993-94 to 2021-22)
# Source: Wikipedia, NBC Sports (https://www.nbcsports.com/soccer/news/list-of-premier-league-stadiums-every-clubs-current-and-former-ground-from-the-pl-era)
# Teams with changed stadiums
changes = {
    'Arsenal': [('2006-07', 60704), ('1993-94', 38419)],
    'Man City': [('2003-04', 53400), ('1993-94', 35150)],
    'Southampton': [('2001-02', 32384), ('1993-94', 15200)],
    'Leicester': [('2002-03', 32261), ('1993-94', 22000)],
    'Middlesbrough': [('1995-96', 34742), ('1993-94', 26667)],
    'West Ham': [('2016-17', 60000), ('1993-94', 35016)],
    'Tottenham': [('2019-20', 62850), ('1993-94', 36284)],
    'Bolton': [('1997-98', 28723), ('1993-94', 22000)],
    'Sunderland': [('1997-98', 49000), ('1993-94', 22000)],
}

# Teams with unchanged stadiums
fixed = {
    'Man United': 74197,
    'Liverpool': 54074,
    'Newcastle': 52258,
    'Aston Villa': 42785,
    'Chelsea': 40173,
    'Everton': 39414,
    'Sheffield Weds': 39812,
    'Leeds': 37890,
    'Blackburn': 31367,
    'Wolves': 32050,
    'Sheffield United': 32050,
    'Brighton': 31876,
    'Ipswich': 29813,
    'Birmingham': 29409,
    'Stoke': 27902,
    'Norwich': 27359,
    'Charlton': 27111,
    'West Brom': 26850,
    'Wimbledon': 26309,
    'Fulham': 25700,
    'Crystal Palace': 25486,
    'Hull': 25400,
    'Wigan': 25138,
    'Bradford': 25136,
    'Huddersfield': 24500,
    'Reading': 24161,
    'Barnsley': 23009,
    'Watford': 22200,
    'Burnley': 21944,
    'Swansea': 21088,
    'Portsmouth': 20700,
    'QPR': 18360,
    'Brentford': 17250,
    'Blackpool': 16220,
    'Swindon': 15728,
    'Oldham': 13512,
    'Bournemouth': 11307,
    'Derby': 33597,
    'Cardiff': 33280,
    'Coventry': 32609,
    "Nott'm Forest": 30404,
}
def get_capacity(team, season):


    if team in changes:
        for from_season, cap in changes[team]:  # duyệt từ mới → cũ
            if season >= from_season:
                return cap

    if team in fixed:
        return fixed[team]

    print(f"WARNING: No capacity data for team '{team}'")
    return None

def main():
    df_results = pd.read_csv("results.csv", encoding="latin1")
    df_results['HomeTeam_StadiumCapacity'] = df_results.apply(lambda row: get_capacity(row['HomeTeam'],row['Season']), axis=1)
    print(df_results.head(5))

main()