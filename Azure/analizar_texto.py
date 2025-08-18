from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Configuración de Azure Text Analytics
TEXT_ANALYTICS_ENDPOINT = "https://caso-policia-analytics.cognitiveservices.azure.com"
TEXT_ANALYTICS_API_KEY = "1qFvZZNENZpICV6HhrNK5w4smsak9baVuGjVusvnouBYsbv8OurpJQQJ99BHACYeBjFXJ3w3AAAEACOG3RF5"

# Verifica que estás usando el endpoint correcto
print("Endpoint usado:", TEXT_ANALYTICS_ENDPOINT)

# Crear cliente de Text Analytics
cliente_nlp = TextAnalyticsClient(
    endpoint=TEXT_ANALYTICS_ENDPOINT,
    credential=AzureKeyCredential(TEXT_ANALYTICS_API_KEY)
)

# Función para extraer palabras clave
def extraer_palabras_clave(texto):
    respuesta = cliente_nlp.extract_key_phrases([texto])
    documento = respuesta[0]

    if not documento.is_error:
        return documento.key_phrases
    else:
        print("Error en la extracción de palabras clave:", documento.error)
        return []

print("=" * 50)

texto = """
Texto Extraído:
Reunidn pactada
para el 25 de abril.
Coordenadas enviadas
Con Pirmar presencia,
No usar canal habitud,
"""

palabras_clave = extraer_palabras_clave(texto)

print(texto)
print("=" * 50)
print("\nPalabras Clave Detectadas:")
for palabra in palabras_clave:
    print(f"- {palabra}")

print("=" * 50)
