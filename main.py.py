#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests                                    #@
from pspy import D                                 #@
from random import choice                          #@
from kivymd.app import MDApp                       #@
from kivy.lang import Builder                      #@ 
from kivy.core.window import Window                #@
from kivy.uix.boxlayout import BoxLayout           #@
from kivy.properties import ObjectProperty         #@
from kivy.uix.scrollview import ScrollView         #@
from kivy_garden.mapview import MapView, MapSource #@

class MainApp(MDApp):
	
	def build(self):
		self.icon = "py.png"
		self.title = "My Pass Create"
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "Orange"

		if True:
			Window.top = 20
			Window.left = 1300
			Window.size = (300,580)
		
		return MainWindow() 

class MainWindow(BoxLayout):
	''' Oggeti di properita   '''
	teip = ObjectProperty(None)
	searchdt = ObjectProperty(None)
	risultato = ObjectProperty(None) 
	richiesta = ObjectProperty(None)

	def search(self):
		try:
			dato = self.searchdt.text
			endpoint = f"https://it.wikipedia.org/w/api.php?prop=extracts&explaintext&exintro&format=json&action=query&titles={dato}"
			respons =  requests.get(endpoint)
			json_dict = respons.json()["query"]["pages"]
			dt_pagi = next(iter(json_dict))
			risultato_informazioni = json_dict[dt_pagi]["extract"]
			self.richiesta.text = risultato_informazioni
		except:
			self.richiesta.text = "Errore"

	
	def slak(self):
		nuova_stringa = ""
		stringa = self.teip.text
		
		for lettera in stringa:
		
			if lettera in D.par:
				nuova_stringa += D.par[lettera]
		
			else:
				nuova_stringa += lettera
		
		self.risultato.text = nuova_stringa
		print(stringa)

	def random_pass(self):
		final = ""
	
		for i in range(12):
			final += choice(D.lista_completa)
		
		self.risultato.text = final

if __name__ == "__main__":
	MainApp().run()


