import pandas as pd

class DataInvestigator:

    def __init__(self, df: pd.DataFrame):
        try:
            if not isinstance(df, pd.DataFrame):
               raise ValueError
            self.df = df
            self.valid = True
        except Exception:
            self.valid = False

    def baseline(self, col):
        if not self.valid:
            return None

        # get the most frequent value in the column 
        try:
            # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html
            results = self.df.iloc[:, col]
            return results.mode().iloc[0]
        except Exception:
            return None
        
    def corr(self, col1, col2):
        if not self.valid:
            return None
        
        # return the linear correlation between two columns
        try:
            resultsCol1 = self.df.iloc[:, col1]
            resultsCol2 = self.df.iloc[:, col2]
            return resultsCol1.corr(resultsCol2)
        except Exception:
            return None

    def zeroR(self, col):
        # return the most frequent value in the column
        return self.baseline(col)
