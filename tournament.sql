-- Table definitions for the tournament project.
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.'''
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


DROP DATABASE if exists tournament;
create database tournament;
-- drops tournament database if it already exists and then creates tournament database.
\c tournament;


create table players (id serial PRIMARY KEY, name VARCHAR(50));
--creates the table (players). Restriction on the name not to be  more than 50 characters.

create table matches (id serial PRIMARY KEY, winner integer REFERENCES players (id) NOT NULL, loser integer REFERENCES players (id) NOT NULL);
--creates the table (matches) with 3 columns: id, winner and loser.

create view standings AS SELECT players.id, players.name,
    (SELECT count(matches.winner) FROM matches where players.id = matches.winner) AS wins,
    (SELECT count(matches.id) FROM matches where players.id = matches.winner OR players.id = matches.loser) as matches_played
    FROM players ORDER BY wins DESC, matches_played DESC;
-- uses view to create standings table.


