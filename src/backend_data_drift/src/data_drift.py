import time
from eurybia import SmartDrift
import pandas as pd
from postgresql import manager

class DataDriftManager:
    def __init__(self, data_drift_csv, data_baseline):
        self.last_time = time.time()
        self.data_drift_csv = data_drift_csv
        self.data_baseline = data_baseline
        
        self.posgres = manager.ManagerPostgres()

    def _get_baseline(self):
        df = pd.read_csv(self.data_baseline)[["size", "nb_rooms", "garden"]]
        df['size'] = df['size'].astype('int64')
        df['garden'] = df['garden'].astype('bool')
        
        return df
        
    def check(self):
        df_baseline = self._get_baseline()
        df_current = self.posgres.get_prediction(0)
        self.last_time = time.time()
        
        sd = SmartDrift(
            df_current=df_current,
            df_baseline=df_baseline,
        )
        
        sd.compile(
            full_validation=True,
            datadrift_file=self.data_drift_csv,
        )