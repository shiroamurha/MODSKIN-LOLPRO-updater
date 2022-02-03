import requests
import zipfile
import os
from datetime import date



def get_patch():
	main_site = str(requests.get('http://leagueskin.net/p/download-mod-skin-2020-chn').text)
	season = date.today().year - 2010

	button_name = f'DOWNLOAD MOD SKIN LOL  {season}'

	button_index = main_site.find(button_name)

	button_index = button_index + len(button_name)

	if main_site[button_index+2] != '.' and main_site[button_index+2] != ' ':

		season_str = f'{season}.{main_site[button_index+1], main_site[button_index+2]}'
	else:
		season_str = f'{season}.{main_site[button_index+1]}'

	return season_str


def update():

	path = r'C:\\Fraps\\temp\\'

	try:
		os.makedirs(path)
	except: 
		pass

	donwload = requests.get(f'http://s4.modskinlolvn.com/MODSKIN_{get_patch()}.zip', allow_redirects=True)


	open(path+'file.zip', 'wb').write(donwload.content)

	with zipfile.ZipFile(path+'file.zip',"r") as zip_ref:

	    zip_ref.extractall(path)

	os.remove(path+'file.zip')

	os.startfile(f'{path}LOLPRO {get_patch()}.exe')


update()