import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

print("LOADING CSV")
emails = 'full_data_enron_emails.csv'
df = pd.read_csv(emails)
print("DONE LOADING CSV")
print ("ONLY ENRON")
df = df[df['email_from'].str.contains("@enron")==True]
print("DONE ONLY ENRON")
from flask import Flask, request
app = Flask(__name__)
app.debug = True

from dateutil import parser

def format_date(x):
    date = parser.parse(x)
    return date.year


@app.route('/')
def hello_world():
    q = request.args.get('q')
    print("make custom DF")
    custom_df = df[df['email_subject'].str.contains(q)==True]
    # grouped_df = custom_df.groupby(df['email_date'].map(lambda x: format_date(x)))
    print("DONE WIT HDF")
    grouped_df_count = custom_df.message.count()
    print(grouped_df_count)
    return str(grouped_df_count)

if __name__ == "__main__":
    app.run()



