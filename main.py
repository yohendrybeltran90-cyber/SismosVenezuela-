 from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
import urllib.request
import json
from datetime import datetime

class SismosApp(App):
    def build(self):
        # Layout principal de la app
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Título de la App
        titulo = Label(
            text="[b]Sismos Venezuela & Frontera[/b]",
            markup=True,
            font_size=22,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(titulo)

        # Área de desplazamiento para la lista de sismos
        self.scroll = ScrollView()
        self.resultado_label = Label(
            text="Presiona el botón para actualizar sismos...",
            markup=True,
            size_hint_y=None,
            valign='top',
            halign='left'
        )
        self.resultado_label.bind(
            texture_size=lambda instance, value: setattr(instance, 'height', value[1]),
            width=lambda instance, value: setattr(instance, 'text_size', (value, None))
        )
        self.scroll.add_widget(self.resultado_label)
        layout.add_widget(self.scroll)

        # Botón para actualizar
        btn = Button(
            text="Actualizar Sismos",
            size_hint_y=None,
            height=60
        )
        btn.bind(on_press=self.actualizar_sismos)
        layout.add_widget(btn)

        return layout

    def actualizar_sismos(self, instance):
        self.resultado_label.text = "Cargando sismos..."
        # Lógica para consultar los datos

if __name__ == '__main__':
    SismosApp().run()
