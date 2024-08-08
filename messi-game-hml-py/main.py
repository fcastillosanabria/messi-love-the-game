"""import eel

eel.init('templates')

@eel.expose
def App():
    print('corriendo aplicacion')

App()
eel.start('index.html' ,size=(1200,725))"""

import eel
import webview

eel.init('templates')

@eel.expose
def App():
    print('corriendo aplicacion')

App()

# Crear una ventana con pywebview y configurar su tamaño y deshabilitar el redimensionamiento
window = webview.create_window('Mi Aplicación', 'templates/index.html', width=1200, height=730, resizable=False)
webview.start()
