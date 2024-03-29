# from utl import dbeditfunctions

def createTables(c):
    c.execute("CREATE TABLE IF NOT EXISTS stories (storyID INTEGER PRIMARY KEY, name TEXT)");

    c.execute("CREATE TABLE IF NOT EXISTS story_edits (storyID INTEGER, userID INTEGER, content TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)");

    c.execute("CREATE TABLE IF NOT EXISTS users (userID INTEGER PRIMARY KEY, username TEXT, password TEXT)");

#returns an array with all values from a given story's row in table.
#find this story by its id
def selectStory(c, storyID):
    c.execute("SELECT * FROM stories WHERE storyID ="+storyID)
    return c.fetchall()

#returns an array with all story names
#arguments: table = storyMasterlist table
def returnStoryNames(c):
    c.execute("SELECT name FROM stories")
    return c.fetchall()

#returns story's latest update.
def getLatestStoryEdit(c, storyID):
    return 0

#returns an array with entire table as data.
def getTable(c, table):
    c.execute("SELECT * FROM " + table)
    return c.fetchall()

def debugPrintSelect(c, table):
    c.execute("SELECT * FROM " + table)
    print(str(c.fetchall()) + "\n")

#TESTING !!

import sqlite3

DB_FILE = "odyssey.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor() #facilitate db operations
createTables(c)

debugPrintSelect(c, "stories")
debugPrintSelect(c, "story_edits")
debugPrintSelect(c, "users")
