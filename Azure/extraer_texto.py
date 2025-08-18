

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import os
from PIL import Image
import tkinter as tk
from tkinter import scrolledtext

ENDPOINT = "https://computervisionpolicia.cognitiveservices.azure.com/"
API_KEY = "1I6Ra8XO9qT7UtD5icW7sIiQ15OBV7pOYRuJj00xF8OKgo9sGzYRJQQJ99BDACYeBjFXJ3w3AAAFACOGIfRH"

cliente = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))

def extraer_texto(imagen_path):
    with open(imagen_path, "rb") as imagen:
        respuesta = cliente.recognize_printed_text_in_stream(imagen)
    
    texto_extraido = ""
    for region in respuesta.regions:
        for linea in region.lines:
            texto_extraido += " ".join([palabra.text for palabra in linea.words]) + "\n"
    
    return texto_extraido

def mostrar_texto(texto):
    ventana = tk.Tk()
    ventana.title("Texto Extraído de la Imagen")
    
    texto_scroll = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=80, height=20)
    texto_scroll.insert(tk.INSERT, texto)
    texto_scroll.pack(padx=10, pady=10)
    
    ventana.mainloop()

ruta_imagen = "imagen/Proyecto.jpeg"
texto = extraer_texto("imagen/Proyecto.jpeg")

mostrar_texto(texto)