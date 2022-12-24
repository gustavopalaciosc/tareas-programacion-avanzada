from servidor import Servidor
import sys

if __name__ == "__main__":
    server = Servidor()
    server.start_server()

    try:
        while True:
            input("[Presione Ctrl+C para cerrar]".center(82, "+") + "\n")
    except KeyboardInterrupt:
        print("\n\n")
        print("Cerrando servidor...".center(80, " "))
        print("".center(82, "-"))
        print("".center(82, "-") + "\n")
        server.socket_server.close()
        sys.exit()