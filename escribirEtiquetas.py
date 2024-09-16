import re

def obtenerEtiquetas():
    try:
        with open("index.html", "r", encoding="utf-8") as html:
            with open("index.txt", "w", encoding="utf-8") as txt:
                # Expresión regular para encontrar etiquetas con el atributo lang="es"
                regex = re.compile(r'<[^>]*lang="es"[^>]*>.*?</[^>]*>', re.DOTALL)
                
                # Leer todo el contenido del archivo HTML
                content = html.read()
                
                # Encontrar todas las coincidencias
                matches = regex.findall(content)
                
                # Escribir las coincidencias en el archivo de texto
                for match in matches:
                    txt.write(match.strip() + "\n")  # Agregar salto de línea

    except FileNotFoundError:
        print("El archivo 'index.html' no se encuentra.")
    except IOError as e:
        print(f"Error al leer o escribir en el archivo: {e}")

obtenerEtiquetas()
