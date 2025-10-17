import flet as ft


def main(page: ft.Page):
    page.title = "Anime"
    page.bgcolor = ft.Colors.GREY_800

    componentes = [
        {
            "titulo": "Alu",
            "funcion": "La Unidad de Aritmética/Lógica es un componente esencial de un chip sencillo del microprocesador. Como su nombre indica, realiza operaciones aritméticas (como suma y resta) y lógicas",
            "imagen": "https://raw.githubusercontent.com/Leonex657/abp/refs/heads/main/alu.jpg",

        },
        {
            "titulo": "Control",
            "funcion": "La Unidad de Control también es uno de los componentes que están contenidos en un chip sencillo del microprocesador, junto con la ALU. Su función principal es dirigir y gestionar las operaciones dentro de la CPU para que las instrucciones se ejecuten correctamente.",
            "imagen": "https://raw.githubusercontent.com/Leonex657/abp/refs/heads/main/control.JPG",

        },
        {
            "titulo": "Registros",
            "funcion": "Los registros son pequeñas unidades de almacenamiento de información temporal dentro de la CPU. Aunque las fuentes mencionan que la memoria primaria es operada por otros chips, los registros son clave para el funcionamiento interno rápido.",
            "imagen": "https://raw.githubusercontent.com/Leonex657/abp/refs/heads/main/registros.JPG",

        },
        {
            "titulo": "Diagrama Completo",
            "funcion": "Este diagrama muestra cómo la CPU recibe datos desde los dispositivos de entrada o memoria, los procesa usando su lógica y registros internos, y luego envía los resultados a la salida o de vuelta a la memoria. Todo esto está coordinado por la unidad de control.",
            "imagen": "https://raw.githubusercontent.com/Leonex657/abp/refs/heads/main/completo.jpg",
        }
    ]

    indice_actual=[0]

    contenedor = ft.Container(
        content=ft.Column([]),
        width=500,
        height=600,
        bgcolor=ft.Colors.GREY_400,
        alignment=ft.alignment.center,
        padding=40
    )

    boton_siguiente=ft.ElevatedButton(text="siguiente componente")
    boton_anterior=ft.ElevatedButton(text="componente anterior")
    

    def mostrar_componentes():
        componente=componentes[indice_actual[0]]
        contenedor.content=ft.Column([
            ft.Image(src=componente["imagen"], width=400, height=300, fit=ft.ImageFit.CONTAIN),
            ft.Text(componente["titulo"], size=20, weight=ft.FontWeight.BOLD, bgcolor=ft.Colors.GREY_900),
            #ft.Text(f"Autor: {anime['titulo']}", size=16, weight=ft.FontWeight.BOLD,bgcolor=ft.Colors.BLUE_600),
            ft.Text(componente["funcion"], size=14, weight=ft.FontWeight.BOLD,bgcolor=ft.Colors.RED_400)
        ], alignment=ft.MainAxisAlignment.CENTER)

        if indice_actual[0]==len(componentes)-1:
            boton_siguiente.text="Volver al inicio"
        else:
            boton_siguiente.text="Siguiente Componente"
        page.update()

    def anterior_click(e):
        indice_actual[0]=(indice_actual[0]-1)%len(componentes)
        mostrar_componentes()

    def siguiente_click(e):
        indice_actual[0]=(indice_actual[0]+1)%len(componentes)
        mostrar_componentes()

    boton_siguiente.on_click=siguiente_click
    boton_anterior.on_click=anterior_click



    
    page.add(
        ft.Container(
            content=ft.Column([
                contenedor,
                boton_siguiente
        ], alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),  
            alignment=ft.alignment.center,
            expand=True
        )
    )
    mostrar_componentes()
    
ft.app(main)