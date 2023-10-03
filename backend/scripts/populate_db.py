import json
import psycopg2

def loadPlayers():
    playerDict = {} # maps player id to their nanme

    with open('raw_data/players.json', "r") as f:
        players = json.load(f)

    for x in players:
        playerDict[int(x["id"])] = x["name"]
        query = "insert into app.app_players (player_id, player_name) values (%s, %s) on conflict do nothing"
        cur.execute(query, (x["id"], x["name"]))
        conn.commit()

    return playerDict

def loadTeams():
    with open('raw_data/teams.json', "r") as f:
        teams = json.load(f)
    for x in teams:
        query = "insert into app.app_teams (team_id, team_name) values (%s, %s) on conflict do nothing"
        cur.execute(query, (x["id"], x["name"]))
        conn.commit()

def loadGames():
    numShots = 0
    with open('raw_data/games.json', "r") as f:
        games = json.load(f)

    shot_id = 1

    # games = games[0]

    for i in range(len(games)):

        game_id = games[i]["id"]
        game_date = games[i]["date"]

        game_query = "insert into app.app_games (game_id, game_date) values (%s, %s) on conflict do nothing"
        cur.execute(game_query, (game_id, game_date))
        conn.commit()

        hometeam_players = games[i]["homeTeam"]["players"]
        awayteam_players = games[i]["awayTeam"]["players"]

        hometeam_id = games[i]["homeTeam"]["id"]
        awayteam_id = games[i]["awayTeam"]["id"]
        
        # creating homeTeam Player entity
        for j in range(len(hometeam_players)):
            home_player_shots = hometeam_players[j]["shots"]

            pid = hometeam_players[j]["id"]
            is_starter = hometeam_players[j]["isStarter"]
            mins = hometeam_players[j]["minutes"]
            pts = hometeam_players[j]["points"]
            ast = hometeam_players[j]["assists"]
            oreb = hometeam_players[j]["offensiveRebounds"]
            dreb = hometeam_players[j]["defensiveRebounds"]
            stl = hometeam_players[j]["steals"]
            blk = hometeam_players[j]["blocks"]
            to = hometeam_players[j]["turnovers"]
            df = hometeam_players[j]["defensiveFouls"]
            of = hometeam_players[j]["offensiveFouls"]
            ftm = hometeam_players[j]["freeThrowsMade"]
            fta = hometeam_players[j]["freeThrowsAttempted"]
            two_pm = hometeam_players[j]["twoPointersMade"]
            two_pa = hometeam_players[j]["twoPointersAttempted"]
            three_pm = hometeam_players[j]["threePointersMade"]
            three_pa = hometeam_players[j]["threePointersAttempted"]
            
            player_stats_query = '''
                insert into app.app_player_stats (
                    team_id,
                    game_id,
                    player_id,
                    is_starter,
                    minutes,
                    points,
                    assists,
                    offensive_rebounds,
                    defensive_rebounds,
                    steals,
                    blocks,
                    turnovers,
                    defensive_fouls,
                    offensive_fouls,
                    free_throws_made,
                    free_throws_attempted,
                    two_pointers_made,
                    two_pointers_attempted,
                    three_pointers_made,
                    three_pointers_attempted
                )
                values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                on conflict do nothing
            '''
            cur.execute(player_stats_query, (hometeam_id, game_id, pid, is_starter, mins, pts, ast, oreb, dreb, stl, blk, to, df, of, ftm, fta, two_pm, two_pa, three_pm, three_pa))
            conn.commit()

            # create Shot entities for this player
            for k in range(len(home_player_shots)):
                is_make = home_player_shots[k]["isMake"]
                loc_x = home_player_shots[k]["locationX"]
                loc_y = home_player_shots[k]["locationY"]

                shot_data_query = '''insert into app.app_shot_data (
                    shot_data_id,
                    game_id,
                    player_id,
                    is_make,
                    location_x,
                    location_y
                )
                values (%s, %s, %s, %s, %s, %s)
                on conflict do nothing'''
                cur.execute(shot_data_query, (shot_id, game_id, pid, is_make, loc_x, loc_y))
                conn.commit()
                shot_id += 1

        # creating awayTeam Player entity
        for j in range(len(awayteam_players)):
            away_player_shots = awayteam_players[j]["shots"]

            pid = awayteam_players[j]["id"]
            is_starter = awayteam_players[j]["isStarter"]
            mins = awayteam_players[j]["minutes"]
            pts = awayteam_players[j]["points"]
            ast = awayteam_players[j]["assists"]
            oreb = awayteam_players[j]["offensiveRebounds"]
            dreb = awayteam_players[j]["defensiveRebounds"]
            stl = awayteam_players[j]["steals"]
            blk = awayteam_players[j]["blocks"]
            to = awayteam_players[j]["turnovers"]
            df = awayteam_players[j]["defensiveFouls"]
            of = awayteam_players[j]["offensiveFouls"]
            ftm = awayteam_players[j]["freeThrowsMade"]
            fta = awayteam_players[j]["freeThrowsAttempted"]
            two_pm = awayteam_players[j]["twoPointersMade"]
            two_pa = awayteam_players[j]["twoPointersAttempted"]
            three_pm = awayteam_players[j]["threePointersMade"]
            three_pa = awayteam_players[j]["threePointersAttempted"]
            
            # print(pid, pname, is_starter, mins, pts, ast, oreb, dreb, stl, blk, to, df, of, ftm, fta, two_pm, two_pa, three_pm, three_pm)

            player_stats_query = '''
                insert into app.app_player_stats (
                    team_id,
                    game_id,
                    player_id,
                    is_starter,
                    minutes,
                    points,
                    assists,
                    offensive_rebounds,
                    defensive_rebounds,
                    steals,
                    blocks,
                    turnovers,
                    defensive_fouls,
                    offensive_fouls,
                    free_throws_made,
                    free_throws_attempted,
                    two_pointers_made,
                    two_pointers_attempted,
                    three_pointers_made,
                    three_pointers_attempted
                )
                values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                on conflict do nothing
            '''
            cur.execute(player_stats_query, (awayteam_id, game_id, pid, is_starter, mins, pts, ast, oreb, dreb, stl, blk, to, df, of, ftm, fta, two_pm, two_pa, three_pm, three_pa))
            conn.commit()

            # create Shot entities for this player
            for k in range(len(away_player_shots)):
                is_make = away_player_shots[k]["isMake"]
                loc_x = away_player_shots[k]["locationX"]
                loc_y = away_player_shots[k]["locationY"]

                shot_data_query = '''insert into app.app_shot_data (
                    shot_data_id,
                    game_id,
                    player_id,
                    is_make,
                    location_x,
                    location_y
                )
                values (%s, %s, %s, %s, %s, %s)
                on conflict do nothing'''
                cur.execute(shot_data_query, (shot_id, game_id, pid, is_make, loc_x, loc_y))
                conn.commit()
                shot_id += 1


if __name__ == "__main__":

    # create postgres db connection
    conn = psycopg2.connect(host="localhost", database="okc", user="okcapplicant", password="thunder")
    cur = conn.cursor()

    # load players into db
    playerDict = loadPlayers() # return dictionary mapping player ids -> player names

    # load teams into db
    loadTeams()

    # load games into db
    loadGames()

    # close connection
    cur.close()
    conn.close()
