#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyodbc 

from cheese.appSettings import Settings
from cheese.Logger import Logger

"""
File generated by Cheese Framework

database connection of Cheese Application for SQL Server
"""

class SQLServerDB:

    # connect to database
    def connect(self):
        self.connection = pyodbc.connect(f"Driver={Settings.dbDriver};"
                      f"Server={Settings.dbHost},{Settings.dbPort};"
                      f"Database={Settings.dbName};"
                      f"UID={Settings.dbUser};"
                      f"PWD={Settings.dbPassword};"
                      f"Trusted_Connection=yes;")

        self.cursor = self.connection.cursor()

    # close connection with database
    def close(self):
        self.cursor.close()

    # select query
    def query(self, sql):
        Logger.okBlue(Logger.WARNING + "QUERY: " + Logger.ENDC + sql)
        try:
            self.cursor.execute(sql)
        except Exception as e:
            Logger.fail(str(e))
            self.rollback()
            return None
        ret = self.cursor.fetchall()
        return ret

    # insert, update ...
    def commit(self, sql):
        if (Settings.allowCommit):
            Logger.okBlue(Logger.WARNING + "COMMIT: " + Logger.ENDC + sql)
            try:
                self.cursor.execute(sql)
            except Exception as e:
                Logger.fail(str(e))
                self.rollback()
        else:
            Logger.fail("Commiting is not allowed")

    # commit when done
    def done(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()