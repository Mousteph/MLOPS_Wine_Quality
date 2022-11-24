from data_drift import DataDriftManager

data_drift = DataDriftManager("test.csv", "../../../data/training/houses.csv")

if __name__ == '__main__':
   data_drift.check() 