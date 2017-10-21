# -*- coding:utf8 -*-
# Created by frank at 20/10/2017

from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import pandas as pd
import sqlite3
# Get Score



conn = sqlite3.connect('/Users/frank/project/faceworks/grader/test.db')
df = pd.read_sql_query("select * from scores;", conn)
print(df)