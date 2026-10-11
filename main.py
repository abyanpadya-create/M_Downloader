from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MDownloaderApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        judul = Label(
            text="[b]M Downloader[/b]\nTikTok · YouTube · Instagram",
            markup=True,
            font_size='20sp',
            size_hint=(1, 0.3)
        )
        layout.add_widget(judul)

        tombol = Button(
            text="Tes Tombol",
            font_size='18sp',
            size_hint=(1, 0.2)
        )
        tombol.bind(on_press=self.tombol_ditekan)
        layout.add_widget(tombol)

        self.status = Label(text="Tekan tombol di atas", font_size='14sp')
        layout.add_widget(self.status)

        return layout

    def tombol_ditekan(self, instance):
        self.status.text = "✅ Tombol berhasil ditekan!"


if __name__ == "__main__":
    MDownloaderApp().run()
