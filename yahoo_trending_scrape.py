# This program scrapes Yahoo.com for the current Top 10 Trending Searches
# Inspired by Jeff Hoffman (Priceline) and his 'Knowledge Sponging'
#  AKA - Checking Yahoo Trending everyday to see what is on America's mind.
# Works cited: http://docs.python-guide.org/en/latest/scenarios/scrape/
# Want to schedule hourly refreshes and connect to a database to do some queries later.

from lxml import html
import requests
import datetime
from pytz import timezone


def main():
    # -- Provide the website to scrape --
    page = requests.get('https://www.yahoo.com/')
    tree = html.fromstring(page.content)

    # -- Scrape the web page --
    # Look at the CSS and see where the data exists.
    # In this case, they're all titles in this specific class.
    title = tree.xpath('//span[@class="C($searchBlue):h Fw(b) Mstart(2px)"]/text()')

    # -- Clean up the data points --
    # Keep in mind a comma will be the value delimiter.
    for i in range(len(title)):
        if i == len(title) - 1:
          title[i] = title[i].lstrip()
        else:
          title[i] = title[i].lstrip() + ', '
    string = ''.join(title) + '\n'

    # -- Define relevant data points --
    tz = timezone('EST')
    year = datetime.datetime.now(tz).date().year
    month = datetime.datetime.now(tz).date().month
    day = datetime.datetime.now(tz).date().day
    dow = datetime.datetime.now(tz).today().weekday()     # Day of the week as an int, Monday = 0, Sunday = 6.
    hour = datetime.datetime.now(tz).time().hour
    hUTC = datetime.datetime.now().time().hour            # Hour in tz = UTC
    min = datetime.datetime.now(tz).time().minute
    
    # -- Convert Weekday from INT to String --
    # dow seems to be based on UTC even though I've changed the  
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if hour in range(19, 23)
       dow = days[dow - 1]
    else:
       dow = days[dow]
    
    # -- Combine variables using a list --
    trending = ', '.join([str(year), str(month), str(day), dow, str(hour), str(min), string])                 
    
    # -- Export results to a CSV --
    fd = open('historical_trending.csv','a')
    fd.write(trending)
    fd.close()


if __name__ == '__main__':
    main()
