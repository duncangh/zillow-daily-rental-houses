"""
module run daily Zillow query and save results
"""

'searchQueryState={"pagination":{},"usersSearchTerm":"Atlanta, GA","mapBounds":{"west":-84.67446835595703,"east":-84.28651364404297,"south":33.69131610727286,"north":33.84258120504907},"regionSelection":[{"regionId":37211,"regionType":6}],"isMapVisible":true,"mapZoom":11,"filterState":{"price":{"min":286028,"max":629262},"pmf":{"value":false},"fore":{"value":false},"apa":{"value":false},"mp":{"min":1000,"max":2200},"sort":{"value":"paymenta"},"auc":{"value":false},"nc":{"value":false},"fr":{"value":true},"fsbo":{"value":false},"cmsn":{"value":false},"pf":{"value":false},"fsba":{"value":false}},"isListVisible":true}'

import json
from urllib.parse import unquote
import subprocess
url_contents = 'searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Atlanta%2C%20GA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-84.67446835595703%2C%22east%22%3A-84.28651364404297%2C%22south%22%3A33.69131610727286%2C%22north%22%3A33.84258120504907%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A37211%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22mapZoom%22%3A11%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A286028%2C%22max%22%3A629262%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3A1000%2C%22max%22%3A2200%7D%2C%22sort%22%3A%7B%22value%22%3A%22paymenta%22%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'

parsed_url_parameters : dict = json.loads(
	unquote(url_contents)
		.split('=', maxsplit=1)[1]
)


def make_new_url():
	"""
	:return: new url
	"""
	# todo: implement
	return


def make_new_command():
	"""
	:return: new curl command
	"""
	# todo: implement
	return

def make_results():
	"""

	:return: new json data results
	"""
	# todo: implement
	return


CURL_COMMAND = """curl 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22Atlanta%2C%20GA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-84.67446835595703%2C%22east%22%3A-84.28651364404297%2C%22south%22%3A33.69131610727286%2C%22north%22%3A33.84258120504907%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A37211%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22mapZoom%22%3A11%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A286028%2C%22max%22%3A629262%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3A1000%2C%22max%22%3A2200%7D%2C%22sort%22%3A%7B%22value%22%3A%22paymenta%22%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D&includeMap=false&includeList=true' \
  -H 'authority: www.zillow.com' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36' \
  -H 'accept: */*' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://www.zillow.com/homes/Atlanta,-GA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22Atlanta%2C%20GA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-84.67446835595703%2C%22east%22%3A-84.28651364404297%2C%22south%22%3A33.69131610727286%2C%22north%22%3A33.84258120504907%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A37211%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22mapZoom%22%3A11%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A286028%2C%22max%22%3A629262%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3A1000%2C%22max%22%3A2200%7D%2C%22sort%22%3A%7B%22value%22%3A%22paymenta%22%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cookie: zguid=23|%245a96c858-2605-41ef-8400-31b2863cc6cc; zjs_anonymous_id=%225a96c858-2605-41ef-8400-31b2863cc6cc%22; _ga=GA1.2.4388863.1589659155; __gads=ID=0ff954ef03faeb74:T=1589659158:S=ALNI_MZWdh-01kvz0R64-564XyNGK4hx9A; _gcl_au=1.1.1143306261.1589659161; G_ENABLED_IDPS=google; _fbp=fb.1.1589659161681.1481208861; _pxvid=bd481cb9-97af-11ea-86f2-0242ac120004; userid=X|3|38abc8213fb9b8de%7C5%7ClYwunm9lfs57pVe73ni4XUPRd_r5CEnd6KbgYmwPH5Q%3D; loginmemento=1|533217dce83164c5ae7d74f6531b294ffac5967df39b31ed30afe96baf6c63fe; zjs_user_id=%22X1-ZUuuicus2869e1_517cm%22; ki_r=; ki_s=; _pin_unauth=dWlkPU1tRXhNelZqWmpZdFlXWmxZaTAwTW1ZekxUazRZV0V0TVdOaFl6QTVNemcyWWpKbA; zgsession=1|ac3f4650-24c8-4a7d-86a9-ef42792a331c; ZILLOW_SID=1|AAAAAVVbFRIBVVsVElCv8%2B77gtuHRIK50TkCsfEvL0HQaNb9cFlCsClSNy4cymNDCJ%2Fo9Sn1Y2MtCrMLU3MhTm5yjdXF; _gid=GA1.2.1298953267.1594501774; JSESSIONID=D5099567F1B937020528B2A5E14739B5; KruxPixel=true; DoubleClickSession=true; KruxAddition=true; _derived_epik=dj0yJnU9VlBvWXFyZjBEZFhKQXUwUV9hU2xlMHpWdXlNZmJ0azcmbj1GSkhUeDk1bkQ0LV9DMWVlYlRSUTBBJm09NyZ0PUFBQUFBRjhLSzRV; intercom-session-xby8p85u=VWVhUGZnRjZKYy9XK3lsTXUxcXRCcTZqb0c3UU83TkhGenhySm5wVDZxVW1jWWh5SnIxak1ieHhFcWxGdEJkcC0takRJbnM0YktGQmZnaHVJUHZtNW1XQT09--03346418db5b418a8c58320adb95051182db4d98; _uetsid=75c147ef-ee38-dbf1-3ab2-bb675e77b689; _uetvid=20e5184a-5589-c7cf-c6f8-8dafc69b962b; _px3=ac7322588289a6a39626f369282c1606618ac70b1c20468ee8719caa89439421:SceB/XZ4dpujL1Qe9bF6RhvFIOSzhSBU5BmIXzPD9PeuHUOcHEMIuiYZSFlX40rE8+OQFiI7tupBxZLdLI/jsQ==:1000:bCFxaDNVdO59sM1328qlgx1grM7U4lwebOqJ8MWzogpy1Rx1slgRPZeCjZHAyzP1gXWDtoqa02p+vHKTSH0fsa8QVX6dPdeC/pZK1QWCwQPPnAN49q30nHaQVGNV3C5/ITdJuGtyd37zTlG/mBiPmYaiXwPskgKewCWXKjkLOXo=; _gat=1; ki_t=1590523755299%3B1594501793298%3B1594504869781%3B5%3B225; AWSALB=DAwclV0eFro+INuiiq+3CpgN9M/BufJU31RArkGNcVe+I1XlRdjuKdnllpnj4X/esRMtH9SOXxgZlpvcDgE8cGPLm9GvQSodys/gqcLiz5NbuDAHWZ79Uae2wwsQ; AWSALBCORS=DAwclV0eFro+INuiiq+3CpgN9M/BufJU31RArkGNcVe+I1XlRdjuKdnllpnj4X/esRMtH9SOXxgZlpvcDgE8cGPLm9GvQSodys/gqcLiz5NbuDAHWZ79Uae2wwsQ; search=6|1597096869886%7Crect%3D33.84258120504907%252C-84.28651364404297%252C33.69131610727286%252C-84.67446835595703%26rid%3D37211%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26sort%3Dpaymenta%26z%3D0%26type%3Dhouse%252Ccondo%252Cmultifamily%252Cmobile%252Cland%252Ctownhouse%26price%3D286028-629262%26mp%3D1000-2200%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%09%0937211%09%09%09%09%09%09' \
  --compressed"""


with subprocess.Popen(CURL_COMMAND, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as _raw_curl_result:
	decoded_curl_result = _raw_curl_result.stdout.read().decode()

	data = json.loads(decoded_curl_result)


CURRENT_PAGE = 1
if data['searchList']['totalPages'] == CURRENT_PAGE:
	print("done")

else:
	url = make_new_url()
	command = make_new_command()
	results = make_results()


data['searchList']['pagination']['nextUrl']


{'pagination': {'currentPage': 2}, 'usersSearchTerm': 'Atlanta, GA', 'mapBounds': {'west': -84.67446835595703, 'east': -84.28651364404297, 'south': 33.69131610727286, 'north': 33.84258120504907}, 'regionSelection': [{'regionId': 37211, 'regionType': 6}], 'isMapVisible': True, 'mapZoom': 11, 'filterState': {'price': {'min': 286028, 'max': 629262}, 'pmf': {'value': False}, 'fore': {'value': False}, 'apa': {'value': False}, 'mp': {'min': 1000, 'max': 2200}, 'sort': {'value': 'paymenta'}, 'auc': {'value': False}, 'nc': {'value': False}, 'fr': {'value': True}, 'fsbo': {'value': False}, 'cmsn': {'value': False}, 'pf': {'value': False}, 'fsba': {'value': False}}, 'isListVisible': True}
