import tkinter as tk
import turtle
import random
import winsound


class RunawayGame:
    def __init__(self, canvas, runner, chaser, catch_radius=50, difficulty='medium', bg_color='white'):
        self.canvas = canvas
        self.runner = runner
        self.chaser = chaser
        self.catch_radius2 = catch_radius ** 2
        self.difficulty = difficulty
        self.bg_color = bg_color

        self.change_shape_and_color(self.runner)
        self.change_shape_and_color(self.chaser)

        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup()

    def is_caught(self):
        p = self.runner.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx ** 2 + dy ** 2 < self.catch_radius2

    def change_shape_and_color(self, turtle):
        shapes = ['turtle', 'circle', 'triangle', 'square']
        colors = ['blue', 'green', 'purple', 'orange', 'pink']
        shape = random.choice(shapes)
        color = random.choice(colors)
        turtle.shape(shape)
        turtle.color(color)

    def start(self, init_dist=400, ai_timer_msec=100):
        self.runner.setpos((-init_dist / 2, 0))
        self.runner.setheading(0)
        self.chaser.setpos((+init_dist / 2, 0))
        self.chaser.setheading(180)

        if self.difficulty == 'easy':
            self.runner.step_move = 5
            self.chaser.step_move = 10
            self.catch_radius2 = 100 ** 2
            self.canvas.bgcolor('lightgreen')
        elif self.difficulty == 'medium':
            self.runner.step_move = 10
            self.chaser.step_move = 15
            self.catch_radius2 = 50 ** 2
            self.canvas.bgcolor('lightblue')
        elif self.difficulty == 'hard':
            self.runner.step_move = 15
            self.chaser.step_move = 20
            self.catch_radius2 = 25 ** 2
            self.canvas.bgcolor('lightcoral')

        self.ai_timer_msec = ai_timer_msec
        self.canvas.ontimer(self.step, self.ai_timer_msec)

    def step(self):
        self.runner.run_ai(self.chaser.pos(), self.chaser.heading())
        self.chaser.run_ai(self.runner.pos(), self.runner.heading())

        is_caught = self.is_caught()
        self.drawer.undo()
        self.drawer.penup()
        self.drawer.setpos(-300, 300)
        if is_caught:
            self.drawer.write('Game Over - You were caught!', font=('Arial', 16, 'normal'))
            winsound.PlaySound('sound_file.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
            self.canvas.bye()  # Close the window when caught
        else:
            self.drawer.write('Is caught? No', font=('Arial', 16, 'normal'))

        self.canvas.ontimer(self.step, self.ai_timer_msec)


class Castle(turtle.RawTurtle):
    def __init__(self, canvas, position):
        super().__init__(canvas)
        self.shape('square')
        self.color('gray')
        self.penup()
        self.goto(position)


class Bush(turtle.RawTurtle):
    def __init__(self, canvas, position):
        super().__init__(canvas)
        self.shape('circle')
        self.color('green')
        self.penup()
        self.goto(position)


class ManualMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.listen()

    def run_ai(self, opp_pos, opp_heading):
        pass


class RandomMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

    def run_ai(self, opp_pos, opp_heading):
        mode = random.randint(0, 2)
        if mode == 0:
            self.forward(self.step_move)
        elif mode == 1:
            self.left(self.step_turn)
        elif mode == 2:
            self.right(self.step_turn)


class Villain(turtle.RawTurtle):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.shape('turtle')
        self.color('purple')
        self.penup()
        self.speed(0)

    def run_ai(self, opp_pos, opp_heading):
        self.setheading(self.towards(opp_pos))
        self.forward(10)


if __name__ == '__main__':
    root = tk.Tk()
    canvas = tk.Canvas(root, width=700, height=700)
    canvas.pack()
    screen = turtle.TurtleScreen(canvas)

    # Уровень сложности: 'easy', 'medium', 'hard'
    difficulty_level = 'medium'

    runner = RandomMover(screen)
    chaser = ManualMover(screen)
    villain = Villain(screen)

    game = RunawayGame(screen, runner, chaser, difficulty=difficulty_level)

    # Создаем замок и кусты
    castle = Castle(screen, (0, 0))
    bushes = [Bush(screen, (random.randint(-300, 300), random.randint(-300, 300))) for _ in range(5)]


    # Добавляем злодея
    villain.goto(0, 0)

    game.start()
    screen.mainloop()
