"""
CP5632 Practical
Kivy GUI program to convert Miles to Km
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Patrick Driscoll'


class MilesToKmApp(App):
    """ MilesToKmApp is a Kivy App for converting Miles to KM """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('milesToKm.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = value * 1.609344
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment, ):
        if self.root.ids.text_input.text == '':
            self.root.ids.text_input.text  = '0'
        self.root.ids.text_input.text = str(int(self.root.ids.text_input.text) + increment)

MilesToKmApp().run()
