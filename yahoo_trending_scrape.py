# This program scrapes Yahoo.com for the current Top 10 Trending Searches
# Inspired by Jeff Hoffman (Priceline) and his 'Knowledge Sponging'
#  AKA - Checking Yahoo Trending everyday to see what is on America's mind.
# Works cited: http://docs.python-guide.org/en/latest/scenarios/scrape/
# Want to schedule hourly refreshes and connect to a database to do some queries later.

from lxml import html
import requests
import datetime

def main():
    # -- Provide the website to scrape --
    page = requests.get('https://www.yahoo.com/')
    tree = html.fromstring(page.content)

    # -- Scrape the web page --
    # Look at the CSS and see where the data exists.
    # In this case, they're all titles in this specific class.
    title = tree.xpath('//span[@class="C($searchBlue):h Fw(b) Mstart(2px)"]/text()')

    # -- Clean up the data points --
    # Keep in mind a comma will be the delimiter.
    for i in range(len(title)):
        if i == len(title) - 1:
          title[i] = title[i].lstrip()
        else:
          title[i] = title[i].lstrip() + ', '
    string = ''.join(title)

    # -- Define relevant data points --
    year = datetime.datetime.now().date().year
    month = datetime.datetime.now().date().month
    day = datetime.datetime.now().date().day
    hour = datetime.datetime.now().time().hour
    min = datetime.datetime.now().time().minute

    # -- Combine variables using a list --
    trending = [str(year)+', ', str(month)+', ', str(day)+', ', str(hour)+', ', str(min)+', ', string]
    clean = ''.join(trending)

    # -- Export results to a CSV --
    fd = open('historical_trending.csv','a')
    fd.write(clean)
    fd.close()


if __name__ == '__main__':
    main()
