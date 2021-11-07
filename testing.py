from pyfzf.pyfzf import FzfPrompt
from datetime import date, datetime

today_date = datetime.today().strftime('%Y.%m.%d')
today_date_object = datetime.today()

sample_date = date(2021, 8, 9)
sample_date_two = date.today()

print(sample_date_two - sample_date)
x = sample_date_two - sample_date
print(x.split()[0])