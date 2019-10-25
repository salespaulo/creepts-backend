import os

#PLAYER WALLET RELATED

PLAYER_OWN_ADD = "0x036f5cf5ca56c6b5650c9de2a41d94a3fe1e2077"
#Overwrite own player address if environment variable set
if 'CARTESI_PLAYER_ADD' in os.environ.keys():
    PLAYER_OWN_ADD = os.environ['CARTESI_PLAYER_ADD']

#DB RELATED

DB_NAME = "db/anuto.db"
USER_LOG_TABLE = "user_logs"
CREATE_USER_LOG_TABLE = "CREATE TABLE {} (user_id INTEGER NOT NULL, tournament_id TEXT NOT NULL, score INTEGER NOT NULL, waves INTEGER NOT NULL, log BLOB NOT NULL);".format(USER_LOG_TABLE)
INSERT_SINGLE_LOG_TABLE = "INSERT INTO {} ('user_id', 'tournament_id', 'score', 'waves', 'log') VALUES (?, ?, ?, ?, ?);".format(USER_LOG_TABLE)
SELECT_LOG_TABLE_BY_USER_AND_TOURNAMENT = "SELECT * FROM {} WHERE user_id=? and tournament_id=?".format(USER_LOG_TABLE)
UPDATE_LOG_TABLE_FOR_USER_AND_TOURNAMENT = "UPDATE {} SET score=?, waves=?, log=? WHERE user_id=? and tournament_id=?".format(USER_LOG_TABLE)