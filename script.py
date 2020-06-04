import requests
from plyer import notification
import time

"""
TODO:
get total cases from https://nepalcorona.info/api/v1/data/nepal or https://nepalcorona.info/api/v1/data/world
get positive, recovered, deaths 
save tha positive cases in file & compare next time 
if it increases compare the old and new cases 
notify with the difference and info
"""

def getData():
    response    = requests.get("https://nepalcorona.info/api/v1/data/nepal").json()
    total_cases = response['tested_positive']
    recovered   = response['recovered']
    deaths      = response['deaths']
    updated_at  = response['latest_sit_report']['date']
    notification_title = ""
    with open('data.txt', 'r+') as f:
        old_cases  = f.read()
        difference = int(total_cases) - int(old_cases)
        # clearing the file #
        f.seek(0)
        f.truncate(0)
        # clearing ends #
        f.write(str(total_cases))
        notification.notify(
            title= "{} New Cases".format(difference) if difference != 0 else "No New Cases",
            message=f"Total cases: {total_cases}\nRecovered: {recovered}\nDeaths: {deaths}\nDate: {updated_at}",
            timeout = 30,
            app_icon = 'virus.ico',
        )

if __name__ == "__main__":
    is_running = True
    while is_running:
        getData()
        time.sleep(3000)