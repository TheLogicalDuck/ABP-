import flet as ft
from gtts import gTTS
import uuid
import os

def main(page: ft.Page):
    page.title = "Proyecto ABP"
    page.window_width = 1000
    page.window_height = 800
    #audio = ft.Audio(src="", autoplay=False)
    #page.overlay.append(audio)

    def narrar(texto_a_leer: str): #Convierte el texto en voz y lo reproduce automáticamente."""
        if not texto_a_leer.strip():
            return
        nombre = f"voz_{uuid.uuid4().hex}.mp3"
        tts = gTTS(text=texto_a_leer, lang="es")
        tts.save(nombre)
        #audio.src = nombre
        #audio.autoplay = True
        page.update()

    
    estado = {"actual": "inicio"}
    
    titulo = ft.Text("CPU", size=25, weight="bold", bgcolor=ft.Colors.PURPLE_900)
    texto = ft.Text("", size=18)
    imagen = ft.Image(src="", width=300, height=250, fit=ft.ImageFit.CONTAIN, visible=False)

    btn_si =ft.ElevatedButton("Empezacemos!",bgcolor=ft.Colors.GREEN_900,icon=ft.Icons.PLAY_ARROW)

    btn_a = ft.ElevatedButton("a) Gestionar la memoria",bgcolor=ft.Colors.RED_900) #Con solo copiar lo de bgcolor asi como esta en todos queda bro, aunque creo ya sabe xd
    btn_b = ft.ElevatedButton("b) Ejecutar operaciones aritméticas y lógicas")
    btn_c = ft.ElevatedButton("c) Coordinar los registros internos")
    btn_d = ft.ElevatedButton("c) Coordinar los registros internos")
    #correctaB

    btn_a1 = ft.ElevatedButton("a) GPU")
    btn_b1 = ft.ElevatedButton("b) Unidad de Control")
    btn_c1 = ft.ElevatedButton("c) Memoria RAM")
    btn_d1 = ft.ElevatedButton("d) CPU")
    #correctaD

    btn_a2 = ft.ElevatedButton("a) Realizar cálculos aritméticos")
    btn_b2 = ft.ElevatedButton("b) Almacenar datos temporalmente")
    btn_c2 = ft.ElevatedButton("c) Coordinar la ejecución correcta de instrucciones")
    btn_d2 = ft.ElevatedButton("d) Dibujar gráficos en pantalla")
    #correctaC

    btn_a3 = ft.ElevatedButton("a) Disco duro")
    btn_b3 = ft.ElevatedButton("b) ALU")
    btn_c3 = ft.ElevatedButton("c) ROM")
    btn_d3 = ft.ElevatedButton("d) Tarjeta de red")
    #correctaB

    btn_a4 = ft.ElevatedButton("a) Información visual")
    btn_b4 = ft.ElevatedButton("b) Información temporal durante la ejecución de instrucciones")
    btn_c4 = ft.ElevatedButton("c) Configuraciones de hardware")
    btn_d4 = ft.ElevatedButton("d) Datos almacenados permanentemente")
    #correctaB

    btn_a5 = ft.ElevatedButton("a) En la memoria RAM externa")
    btn_b5 = ft.ElevatedButton("b) Dentro del disco duro")
    btn_c5 = ft.ElevatedButton("c) Dentro de la CPU")
    btn_d5 = ft.ElevatedButton("d) En la tarjeta gráfica")
    #correctaC

    btn_a6 = ft.ElevatedButton("a) Cómo la GPU procesa imágenes")
    btn_b6 = ft.ElevatedButton("b) Cómo los dispositivos de entrada y salida se conectan al CPU",)
    btn_c6 = ft.ElevatedButton("c) Cómo la CPU interactúa con memoria, entrada/salida y realiza procesamiento")
    btn_d6 = ft.ElevatedButton("d) Cómo se programan videojuegos")
    #correctaC

    btn_a7 = ft.ElevatedButton("a) La memoria RAM",)
    btn_b7 = ft.ElevatedButton("b) Los registros")
    btn_c7 = ft.ElevatedButton("c) La Unidad de Control")
    btn_d7 = ft.ElevatedButton("d) El mouse y el teclado")
    #correctaC

    btn_reset = ft.ElevatedButton("Reiniciar", icon=ft.Icons.REFRESH)
    botones = ft.Column([btn_a, btn_b,btn_si, btn_c, btn_d, btn_a1,btn_b1,btn_c1,btn_d1, btn_a2, btn_b2, btn_c2, btn_d2, btn_a3, btn_b3, btn_c3, btn_d3, btn_a4, btn_b4, btn_c4, btn_d4, btn_a5, btn_b5, btn_c5, btn_d5, btn_a6, btn_b6, btn_c6, btn_d6, btn_a7, btn_b7, btn_c7, btn_d7,], width=500, height=300, alignment=ft.MainAxisAlignment.CENTER, spacing=20)

    def mostrar_inicio():
        estado["actual"] = "inicio"
        page.bgcolor = None
        texto.value = "Estas listo para comenzar el quiz sobre la CPU?, si respondes correctamente pasaras a la siguiente pregunta, si fallas el quiz terminara."
        btn_si.visible = True
        imagen.visible = True
        imagen.src = "meme1.jpg"
        btn_a.visible = False
        btn_b.visible = False
        btn_c.visible = False  
        btn_d.visible = False
        btn_a1.visible = False
        btn_b1.visible = False 
        btn_c1.visible = False
        btn_d1.visible = False
        btn_a2.visible = False
        btn_b2.visible = False
        btn_c2.visible = False
        btn_d2.visible = False
        btn_a3.visible = False
        btn_b3.visible = False
        btn_c3.visible = False
        btn_d3.visible = False
        btn_a4.visible = False
        btn_b4.visible = False
        btn_c4.visible = False
        btn_d4.visible = False
        btn_a5.visible = False
        btn_b5.visible = False
        btn_c5.visible = False
        btn_d5.visible = False
        btn_a6.visible = False
        btn_b6.visible = False
        btn_c6.visible = False
        btn_d6.visible = False
        btn_a7.visible = False
        btn_b7.visible = False
        btn_c7.visible = False
        btn_d7.visible = False
        #narrar(texto.value)
        
        page.update()
        
    def a_pregunta2_si():
        estado["actual"] = "p2_si"
        texto.value = "¿Cuál es la función principal de la ALU dentro de un microprocesador?"
        imagen.visible = True
        imagen.src = "meme2.jpg"
        btn_a.visible = True
        btn_b.visible = True
        btn_c.visible = True 
        btn_d.visible = True
        btn_si.visible = False
        page.update()
        #narrar(texto.value)

    def a_pregunta3_si():
        estado["actual"] = "p3_si"
        texto.value = "¿La ALU se encuentra contenida dentro de qué otro componente más general?"
        imagen.visible = True
        imagen.src = "meme3.jpg"
        btn_a.visible = False
        btn_b.visible = False
        btn_c.visible = False
        btn_d.visible = False
        btn_a1.visible = True
        btn_b1.visible = True
        btn_c1.visible = True
        btn_d1.visible = True
        page.update()
        #narrar(texto.value)

    def a_pregunta4_si():
        estado["actual"] = "p4_si"
        texto.value = "¿Cuál es la responsabilidad principal de la Unidad de Control?"
        imagen.visible = True
        imagen.src = "meme4.jpg"
        btn_a1.visible = False
        btn_b1.visible = False 
        btn_c1.visible = False
        btn_d1.visible = False
        btn_a2.visible = True
        btn_b2.visible = True
        btn_c2.visible = True
        btn_d2.visible = True
        page.update()
        #narrar(texto.value)
        
    def a_pregunta5_si():
        estado["actual"] = "p5_si"
        texto.value = "¿Qué otro componente siempre trabaja en conjunto con la Unidad de Control dentro de la CPU?"
        imagen.visible = True
        imagen.src = "meme5.jpg"
        btn_a2.visible = False
        btn_b2.visible = False
        btn_c2.visible = False
        btn_d2.visible = False
        btn_a3.visible = True
        btn_b3.visible = True
        btn_c3.visible = True
        btn_d3.visible = True
        page.update()
        #narrar(texto.value)
        
    def a_pregunta6_si():
        estado["actual"] = "p6_si"
        texto.value = "¿Qué tipo de información almacenan los registros?"
        imagen.visible = True
        imagen.src = "meme6.jpg"
        btn_a3.visible = False
        btn_b3.visible = False
        btn_c3.visible = False
        btn_d3.visible = False
        btn_a4.visible = True
        btn_b4.visible = True
        btn_c4.visible = True
        btn_d4.visible = True
        page.update()
        #narrar(texto.value)
        
    def a_pregunta7_si():
        estado["actual"] = "p7_si"
        texto.value = "¿Dónde se encuentran físicamente los registros?"
        imagen.visible = True
        imagen.src = "meme7.jpg"
        btn_a4.visible = False
        btn_b4.visible = False  
        btn_c4.visible = False
        btn_d4.visible = False
        btn_a5.visible = True
        btn_b5.visible = True
        btn_c5.visible = True
        btn_d5.visible = True
        page.update()
        #narrar(texto.value)
        
    def a_pregunta8_si():
        estado["actual"] = "p8_si"
        texto.value = "¿Qué muestra el diagrama completo presentado al final del programa?"
        imagen.visible = True  
        imagen.src = "meme8.jpg"
        btn_a5.visible = False
        btn_b5.visible = False
        btn_c5.visible = False
        btn_d5.visible = False
        btn_a6.visible = True
        btn_b6.visible = True
        btn_c6.visible = True
        btn_d6.visible = True
        page.update()
        #narrar(texto.value)
        
    def a_pregunta9_si():
        estado["actual"] = "p9_si"
        texto.value = "¿Quién coordina todas las operaciones dentro del CPU según el diagrama?"
        imagen.visible = True
        imagen.src = "meme9.jpg"
        btn_a6.visible = False
        btn_b6.visible = False
        btn_c6.visible = False
        btn_d6.visible = False
        btn_a7.visible = True
        btn_b7.visible = True
        btn_c7.visible = True
        btn_d7.visible = True
        page.update()
        #narrar(texto.value)
        
    def final_bueno():
        estado["actual"] = "final_bueno"
        texto.value = "🏆🎉Felicidades, has completado el quiz con éxito!"
        page.bgcolor = ft.Colors.GREEN
        imagen.visible = True
        imagen.src = "bueno.jpg"
        btn_reset.visible = True
        btn_a.visible = False
        btn_b.visible = False
        btn_c.visible = False  
        btn_d.visible = False
        btn_a1.visible = False
        btn_b1.visible = False 
        btn_c1.visible = False
        btn_d1.visible = False
        btn_a2.visible = False
        btn_b2.visible = False
        btn_c2.visible = False
        btn_d2.visible = False
        btn_a3.visible = False
        btn_b3.visible = False
        btn_c3.visible = False
        btn_d3.visible = False
        btn_a4.visible = False
        btn_b4.visible = False
        btn_c4.visible = False
        btn_d4.visible = False
        btn_a5.visible = False
        btn_b5.visible = False
        btn_c5.visible = False
        btn_d5.visible = False
        btn_a6.visible = False
        btn_b6.visible = False
        btn_c6.visible = False
        btn_d6.visible = False
        btn_a7.visible = False
        btn_b7.visible = False
        btn_c7.visible = False
        btn_d7.visible = False        
        page.update()
        narrar(texto.value)
        
    
    def final_malo():
        estado["actual"] = "final_malo"
        texto.value = "💀☠️Has fallado el quiz, estudia más."
        page.bgcolor = ft.Colors.RED_300
        imagen.visible = True
        imagen.src = "malo.jpg"
        btn_reset.visible = True
        btn_a.visible = False
        btn_b.visible = False
        btn_c.visible = False  
        btn_d.visible = False
        btn_a1.visible = False
        btn_b1.visible = False 
        btn_c1.visible = False
        btn_d1.visible = False
        btn_a2.visible = False
        btn_b2.visible = False
        btn_c2.visible = False
        btn_d2.visible = False
        btn_a3.visible = False
        btn_b3.visible = False
        btn_c3.visible = False
        btn_d3.visible = False
        btn_a4.visible = False
        btn_b4.visible = False
        btn_c4.visible = False
        btn_d4.visible = False
        btn_a5.visible = False
        btn_b5.visible = False
        btn_c5.visible = False
        btn_d5.visible = False
        btn_a6.visible = False
        btn_b6.visible = False
        btn_c6.visible = False
        btn_d6.visible = False
        btn_a7.visible = False
        btn_b7.visible = False
        btn_c7.visible = False
        btn_d7.visible = False
        page.update()
        narrar(texto.value)
        
    def on_si(e):
        if estado["actual"] == "inicio":
            a_pregunta2_si()

    
    
    def on_bien(e):
        if estado["actual"] == "p2_si":
            a_pregunta3_si()
        elif estado["actual"] == "p3_si":
            a_pregunta4_si()
        elif estado["actual"] == "p4_si":
            a_pregunta5_si()
        elif estado["actual"] == "p5_si":
            a_pregunta6_si()
        elif estado["actual"] == "p6_si":
            a_pregunta7_si()
        elif estado["actual"] == "p7_si":
            a_pregunta8_si()
        elif estado["actual"] == "p8_si":
            a_pregunta9_si()
        elif estado["actual"] == "p9_si":
            final_bueno()

    def on_no(e):
        if estado["actual"] == "inicio":
            final_malo()
        elif estado["actual"] == "p2_si":
            final_malo()
        elif estado["actual"] == "p3_si":
            final_malo()
        elif estado["actual"] == "p4_si":
            final_malo()
        elif estado["actual"] == "p5_si":
            final_malo()
        elif estado["actual"] == "p6_si":
            final_malo()
        elif estado["actual"] == "p7_si":
            final_malo()
        elif estado["actual"] == "p8_si":
            final_malo()


    def on_reset(e):
        mostrar_inicio()

    btn_si.on_click = on_si
    btn_reset.on_click = on_reset

    btn_b.on_click = on_bien      # Pregunta 1 - correcta
    btn_a.on_click = on_no
    btn_c.on_click = on_no
    btn_d.on_click = on_no

    btn_d1.on_click = on_bien     # Pregunta 2 - correcta
    btn_a1.on_click = on_no
    btn_b1.on_click = on_no
    btn_c1.on_click = on_no

    btn_c2.on_click = on_bien     # Pregunta 3 - correcta
    btn_a2.on_click = on_no
    btn_b2.on_click = on_no
    btn_d2.on_click = on_no

    btn_b3.on_click = on_bien     # Pregunta 4 - correcta
    btn_a3.on_click = on_no
    btn_c3.on_click = on_no
    btn_d3.on_click = on_no

    btn_b4.on_click = on_bien     # Pregunta 5 - correcta
    btn_a4.on_click = on_no
    btn_c4.on_click = on_no
    btn_d4.on_click = on_no

    btn_c5.on_click = on_bien     # Pregunta 6 - correcta
    btn_a5.on_click = on_no
    btn_b5.on_click = on_no
    btn_d5.on_click = on_no

    btn_c6.on_click = on_bien     # Pregunta 7 - correcta
    btn_a6.on_click = on_no
    btn_b6.on_click = on_no
    btn_d6.on_click = on_no

    btn_c7.on_click = on_bien     # Pregunta 8 - correcta
    btn_a7.on_click = on_no
    btn_b7.on_click = on_no
    btn_d7.on_click = on_no



    page.add(
    ft.Container(
        content=ft.Column(
            [titulo, texto, imagen, botones, btn_reset],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
            expand=True
        ),
        padding=20,
        alignment=ft.alignment.center
    )
)

    mostrar_inicio()
    
ft.app(target=main)