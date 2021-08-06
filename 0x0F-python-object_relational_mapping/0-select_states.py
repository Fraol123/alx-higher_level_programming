#!/usr/bin/python3                                                                                                                         
"""                                                                                                                                        
python script that lists all states from the databese hbtn_0e_0_usa                                                                        
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
