from bs4 import BeautifulSoup
from win32com.client import Dispatch
import requests
import os, winshell
import shutil
import zipfile



def get_download_specs():

	#faz requst do html do site
	main_website = BeautifulSoup(

		requests.get('http://leagueskin.net/p/download-mod-skin-2020-chn').text,
		features="html.parser"
	)

	#pega o link de download
	href_from_button = main_website.find(	
		'a', 
		attrs={
			'id': 'link_download3'
		}
	)['href']


	#pega o patch com DOM junto com uma manipulaçao de str
	patchName_from_button = main_website.find(	
		'button', 
		attrs={
			'id': 'name_button_download3'
		}
	).text.split(' ')

	try:
		while True:
			patchName_from_button.remove('')
	except ValueError:
		pass

	patchName_from_button = patchName_from_button[3]


	return [href_from_button, patchName_from_button]
	


def createShortcut(local_download_specs, path):
	
	desktop = winshell.desktop()
	shell = Dispatch('WScript.Shell')
	shortcut = shell.CreateShortCut(os.path.join(desktop, "ModSkin LOLPRO.lnk"))
	shortcut.Targetpath = rf"{path}LOLPRO {local_download_specs}.exe"
	shortcut.WorkingDirectory = r"C:\Fraps"
	shortcut.IconLocation = rf"{path}LOLPRO {local_download_specs}.exe"
	shortcut.save()



def update():
    
	path = r'C:\\Fraps\\temp\\'

	#arruma os diretorios apagando se já existe e criando se ainda nao existe
	try:
		shutil.rmtree(path)
	except:
		os.makedirs(path)
		dir_path = True
	else:
		dir_path = False

	if not dir_path:
		os.makedirs(path)
	
	#cria request pra baixar o bag
	print('Updating Modskin LOLPRO...')	
	global download_specs
	download_specs = get_download_specs()
	donwload = requests.get(download_specs[0], allow_redirects=True)

	open(path+'file.zip', 'wb').write(donwload.content)
	with zipfile.ZipFile(path+'file.zip',"r") as zip_ref:

		#extrai o zip
	    zip_ref.extractall(path)

	#apaga o zip
	os.remove(f'{path}file.zip')
	try:
		#liga o exec da atualização nova
		os.startfile(f'{path}LOLPRO {download_specs[1]}.exe')
	except:
		pass
	
	print('\nCreating shortcut...', end='   ')
	createShortcut(download_specs[1], path)
	print('Finished')


#box
#########
		#
update()#
		#
#########

