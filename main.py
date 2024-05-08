import yfinance as yf
from datetime import date
import pandas as pd

START = "2019-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

aktier = ("NDA-SE.ST", "TELIA.ST", "BOL.ST", "EVO.ST", "ASSA-B.ST", "SCA-B.ST", "GETI-B.ST", "ELUX-B.ST", "TEL2-B.ST", "ATCO-B.ST", "SKF-B.ST", "SAND.ST", "ATCO-A.ST", "HEXA-B.ST", "ERIC-B.ST", "VOLV-B.ST", "HM-B.ST", "SHB-A.ST", "SEB-A.ST", "INVE-B.ST", "ALFA.ST", "ALIV-SDB.ST", "ESSITY-B.ST", "SWED-A.ST", "KINV-B.ST", "ABB.ST", "NIBE-B.ST", "AZN.ST", "SINCH.ST", "SBB-B.ST")


def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data = load_data(aktier).drop(columns=["Open", "High", "Low", "Adj Close", "Volume"])

df = data.to_csv("data.csv", index=False)
df = pd.read_csv("data.csv")

#sätter första raden som kolumnnamn
df.columns = df.iloc[0]
#sätter rader 1 och framåt som data
df = df[1:]

#konvertera kolumnerna till en lista
cols = df.columns.tolist()
#ändra namn på första kolumnen
cols[0] = 'Date'
#ändra namn på kolumner till kolumnnamn i listan
df.columns = cols 

df.to_csv("data.csv", index=False)
df = pd.read_csv("data.csv")

print(df)

   