from utils.reader_csv_service import call_read_csv

dir = "./data/calendar_data.csv"
data = call_read_csv(dir)

print(data)