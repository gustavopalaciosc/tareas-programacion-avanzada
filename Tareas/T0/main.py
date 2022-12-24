from menus import MenuInicio, MenuJuego

if __name__ == "__main__":
    
    menu_juego  = MenuJuego()
    menu_inicio = MenuInicio(menu_juego)
    menu_inicio.run()
    