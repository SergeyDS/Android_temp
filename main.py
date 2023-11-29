from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import nfc
import ndef
from threading import Thread

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import mainthread
from kivy.core.clipboard import Clipboard as Cb

import socket

KV = """
MyBL:
	orientation: "vertical"
	size_hint: (0.95, 0.95)
	pos_hint: {"center_x": 0.5, "center_y":0.5}

	Label:
		font_size: "15sp"
		multiline: True
		text_size: self.width*0.98, None
		size_hint_x: 1.0
		size_hint_y: None
		height: self.texture_size[1] + 15
		text: root.data_label
		markup: True
		on_ref_press: root.linki()		



	TextInput:
		id: Inp
		multiline: False
		padding_y: (5,5)
		size_hint: (1, 0.5)
		on_text: app.process()

	

	Button:
		text: "Записать NFC"
		bold: True
		background_color:'#00FFCE'
		size_hint: (1,0.5)
		on_press: root.callback4()

"""


class MyBL(BoxLayout):
    data_label = StringProperty("Треугольник!")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def callback4(self):
        print("Записать NFC")

        def on_connect(tag):
            message = nfc.ndef.TextRecord("Hello, NFC!")
            tag.ndef.message = nfc.ndef.Message(message)
            print("Data has been written to the tag.")
            with nfc.ContactlessFrontend('usb') as clf:
                clf.connect(rdwr={'on-connect': on_connect})


class MyApp(App):
    running = True

    def process(self):
        text = self.root.ids.Inp.text

    def build(self):
        return Builder.load_string(KV)

    def on_stop(self):
        self.running = False


MyApp().run()
