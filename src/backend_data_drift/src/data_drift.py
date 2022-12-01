import time
from eurybia import SmartDrift
import pandas as pd
from postgresql import manager
from datetime import datetime
from os.path import exists


class DataDriftManager:
    def __init__(self, data_drift_csv, data_baseline):
        self.last_time = time.time()
        self.data_drift_csv = data_drift_csv
        self.data_baseline = data_baseline
        self.columns = ["fixed acidity", "volatile acidity",
                        "citric acid", "total sulfur dioxide",
                        "pH", "alcohol"]
        
        self.posgres = manager.ManagerPostgres()

    def _get_baseline(self):
        df = pd.read_pickle(self.data_baseline)[self.columns]
        return df
    
    def _save_auc(self, date, auc):
        df = pd.DataFrame([[date, round(auc, 3)]], columns=["Date", "AUC"])
        
        if not exists(self.data_drift_csv):
           df.to_csv(self.data_drift_csv, index=True)
           return
        
        df.to_csv(self.data_drift_csv, index=True, header=False, mode='a')
        
    def check(self):
        # df_current = self.posgres.get_prediction(self.last_time)
        df_current = self._get_baseline()
        if len(df_current) == 0:
            return 
        
        df_baseline = self._get_baseline()
       
        try: 
            sd = SmartDrift(
                df_current=df_current,
                df_baseline=df_baseline,
            )
            sd.compile(
                full_validation=True,
            )
            
            date = datetime.fromtimestamp(int(self.last_time))
            self._save_auc(date, sd.auc)

            self.last_time = time.time()
        except Exception as _:
            pass