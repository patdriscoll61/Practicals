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
        self.root = Builder.load_file('milesToKm_2.kv')
        return self.root

    def handle_calculate(self, str_value):
        """ handle calculation (could be button press or other call), output result to label widget
            check if the input is valid first, if not set output to 0.0 """
        try:
            value = int(str_value)
            result = value * 1.609344
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = '0.0'
            self.root.ids.text_input.text = ''

    def handle_increment(self, increment, ):
        if self.root.ids.text_input.text == '':
            self.root.ids.text_input.text = '0'
        self.root.ids.text_input.text = str(int(self.root.ids.text_input.text) + increment)
        self.handle_calculate(int(self.root.ids.text_input.text))


MilesToKmApp().run()
