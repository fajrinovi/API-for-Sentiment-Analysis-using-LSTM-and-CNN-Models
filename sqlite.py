
import sqlite3
db = sqlite3.connect('database.db', check_same_thread=False)
db.text_factory = bytes
mycursor = db.cursor()
table1 = db.execute('''CREATE TABLE IF NOT EXISTS sentiment_cnn (cnn_id INTEGER PRIMARY KEY AUTOINCREMENT, original_text text, clean_text text, analyst_sentiment text);''')
table2 = db.execute('''CREATE TABLE IF NOT EXISTS sentiment_lstm (lstm_id INTEGER PRIMARY KEY AUTOINCREMENT, original_text text, clean_text text, analyst_sentiment text);''')


