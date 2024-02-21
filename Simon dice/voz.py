import speech_recognition as sr
from pynput.mouse import Controller as MouseController
import pyautogui

def voz():
    arreglo = []
    palabra = sr.Recognizer()
    coordenadas_colores = {
        "rojo": (226, 346),
        "azul": (440, 166),
        "amarillo": (237, 143),
        "verde": (365, 376)
    }

    print("||   ACTIVANDO MICROFONO      ||")
    with sr.Microphone() as source:
        print("||       Hable ahora          ||")
        print("==============================")
        print("")
        try:
            audio = palabra.listen(source, timeout=5, phrase_time_limit=5)  # Ajustar según necesidad
            text = palabra.recognize_google(audio, language="es-ES").split()
            for palabra in text:
                arreglo.append(coordenadas_colores.get(palabra))
            return [coord for coord in arreglo if coord is not None]
        except sr.RequestError:
            print("Problema de conexión al servicio de Google.")
        except sr.UnknownValueError:
            print("No entiendo el color.")
        except Exception as e:
            print(f"Error: {str(e)}")

def funcion_click(self,mouse_x,mouse_y,current_step):
        algo = True
        for button in self.buttons:
            if button.clicked(mouse_x, mouse_y):
                self.current_step = current_step
                self.clicked_button = button.colour
                if self.clicked_button and self.clicked_button == self.pattern[self.current_step]:
                    self.button_animation(self.clicked_button)
                elif self.clicked_button and self.clicked_button != self.pattern[self.current_step]:
                    self.game_over_animation()
                    self.save_score()
                    self.playing = False
                    return False
                    
