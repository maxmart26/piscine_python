import time
from datetime import datetime



timee = time.time()

print(f"Second since January 1, 1970: {timee:,.4f} or {timee:.2e} in scientific notation")

readable_date = datetime.fromtimestamp(timee).strftime("%b %d %Y")
print(readable_date)