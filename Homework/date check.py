  # Валидность дата

import time
date = input('Дата (mm/dd/yyyy):')
try:
  valid_date = time.strptime(date, '%m/%d/%Y')
except ValueError:
  print('Не правельтная дата!')