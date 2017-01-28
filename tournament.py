#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except:
        print ("error message")


def deleteMatches():
    """Delete and clears out the match records from the database."""
    db, c = connect()
    c.execute("DELETE FROM matches")
    db.commit()
    db.close()



def deletePlayers():
    """Remove all the player records from the database"""
    db, c = connect()
    c.execute("DELETE from players")
    db.commit()
    db.close()



def countPlayers():
    """Returns the number of currently registered players from the database"""
    db, c = connect()
    c.execute("SELECT count(*) from players")
    registered_players = c.fetchone()[0]
    db.close()
    return registered_players



def registerPlayer(name):
    """Adds a player to the tournament by assigning an entry in the database with an ID number"""
    db, c = connect()
    c.execute ("INSERT INTO players (name) VALUES (%s)",(name,))
    db.commit()
    db.close()




def playerStandings():
    """Returns a list of the players, sorted by the number of wins"""
    db, c = connect()
    c.execute("SELECT * FROM standings")
    db.commit()
    Playerstandings = c.fetchall()
    db.close()
    return Playerstandings



def reportMatch(winner, loser):
    """Records the outcome of a single match between two players in the database"""
    db, c = connect()
    result = ("INSERT INTO matches (winner, loser) VALUES (%s, %s)")
    c.execute(result,(winner, loser))
    db.commit()
    db.close()



def swissPairings():
    """Generates a list of pairings according to the Swiss system for the next round of a match"""
    db, c = connect()
    standings = playerStandings()
    players_count = "SELECT count(players.id) as num from players;"
    c.execute(players_count)
    count = c.fetchone()[0]
    player = [item[0:2] for item in standings]
    index = 0
    SwissPairList = []
    while index < count:
        pair = player[index] + player[index + 1]
        SwissPairList.append(pair)
        index += 2
    db.close()
    return SwissPairList






