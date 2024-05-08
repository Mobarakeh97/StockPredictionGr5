import yfinance as yf
from datetime import date

START = "2019-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

aktier = ("ABB.ST", "ALFA.ST", "ALIV-SDB.ST", "ASSA-B.ST", "ATCO-A.ST", "ATCO-B.ST", "AZN.ST", "CAST.ST", "ELUX-B.ST", "ERIC-B.ST", "GETI-B.ST", "HM-B.ST", "INDU-C.ST", "INVE-B.ST", "KINV-B.ST", "LUMI-SDB.ST", "NDA-SEK.ST", "SAND.ST", "SCA-B.ST", "SEB-A.ST", "SECU-B.ST", "SHB-A.ST", "SKA-B.ST", "SKF-B.ST", "SSAB-A.ST", "SWED-A.ST", "SWMA.ST", "TEL2-B.ST", "TREL-B.ST", "VOLV-B.ST")

def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data = load_data(aktier).drop(columns=["Open", "High", "Low", "Adj Close", "Volume"])

print(data.head())