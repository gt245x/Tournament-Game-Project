#Tournament Game project 

**Udacity project to build a game/sports swiss-system tournament in which players are not eliminated when they lose a match but are paired in each round with opponents having approximately the same win-loss record. Ties are broken by looking at how well the tied players opponets have done

##Installation/Running
    + Ensure that python and postgreSQL are properly installed
    + cd to the directory containing the files
    + On postgreSQL, create a database called 'tournament' and connect to the database
    + Copy the table and views from tournament.sql into the 'tournament' database.
    + Alternatively, connect to the database using the template code "tournament.sql" 
    + The program can then be run by typing "python tournament_test.py" on the terminal.

##Program output
The file "tournament_test.py" contains unit test that tests the functions written in "tournament.py". Successful running the code should give the following:
1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered
3. countPlayers() returns 2 after two player is registered
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings 
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired. Success! All test pass!

##FEATURES

- Use of postgreSQL database to store data.
- Tournament game has to feature even number of players and there has to be a winner in each game.




