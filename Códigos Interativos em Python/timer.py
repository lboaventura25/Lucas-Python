import arcade
import random

SCREEN_WIDTH = 1850
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Timer do Lucas"
name = input('Digite o nome do palestrante: ')
time = int(input('Digite a restrição do tempo em minutos: '))


class LucasTimer(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.total_time = 0.0

    def setup(self):
        arcade.set_background_color(arcade.color.WHITE)
        self.total_time = 0.0

    def on_draw(self):
        """ Função para mostrar na tela. """

        arcade.start_render()

        # Calcula os minutos
        minutes = int(self.total_time) // 60

        # Calcula os segundo pelo módulo
        seconds = int(self.total_time) % 60

        #Pisca a tela apartir do minuto escolhido
        if minutes >= time:
            if seconds < 40:
                if seconds % 5 == 0:
                    arcade.set_background_color(random_color())
            if seconds >= 40:
                    arcade.set_background_color(random_color())
                

        # Saída
        output = f"{name}: {minutes:02d}:{seconds:02d}"

        # Coloca na tela as informações com as devidas características
        arcade.draw_text(output, 0, 400, arcade.color.BLACK, 160)

    def update(self, delta_time):
        """
        Lógica de Atualização do tempo
        """
        self.total_time += delta_time

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255) 
    return (r, g, b)


def main():
    window = LucasTimer()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()