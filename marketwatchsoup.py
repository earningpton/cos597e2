import requests
import json

# May need to update the EntitlementToken. To do so go to https://www.marketwatch.com/investing/stock/aapl,
#  watch network connections, find the api call and parse out the token
# If token does not match. api call will return a 400

req_url = 'https://api-secure.wsj.net/api/michelangelo/timeseries/history?json={"Step":"PT1M","TimeFrame":"D1",' \
          '"EntitlementToken":"cecc4267a0194af89ca343805a3e57af","IncludeMockTick":true,"FilterNullSlots":false,' \
          '"FilterClosedPoints":true,"IncludeClosedSlots":false,"IncludeOfficialClose":true,"InjectOpen":false,' \
          '"ShowPreMarket":false,"ShowAfterHours":false,"UseExtendedTimeFrame":false,"WantPriorClose":true,' \
          '"IncludeCurrentQuotes":false,"ResetTodaysAfterHoursPercentChange":false,' \
          '"Series":[{"Key":"STOCK/US/XNAS/AAPL","Dialect":"Charting","Kind":"Ticker","SeriesId":"s1",' \
          '"DataTypes":["Last"],"Indicators":[{"Parameters":[{"Name":"ShowOpen"},{"Name":"ShowHigh"},' \
          '{"Name":"ShowLow"},{"Name":"ShowPriorClose","Value":true},{"Name":"Show52WeekHigh"},' \
          '{"Name":"Show52WeekLow"}],"Kind":"OpenHighLowLines","SeriesId":"i2"}]}]}&ckey=cecc4267a0'

r = requests.get(req_url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
                                   "Content-Type": "application/json, text/javascript, */*; q=0.01",
                                   "Dylan2010.EntitlementToken": "cecc4267a0194af89ca343805a3e57af"})
# Full Return
print(r)

# Stock UNIX Dates
print(json.loads(r.content)['TimeInfo']['Ticks'][0:5])

# Stock Prices
print(json.loads(r.content)['Series'][0]['DataPoints'][0:5])