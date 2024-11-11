from manim import *

config.pixel_height = 1080
config.pixel_width = 1920
config.frame_rate = 60


class WhatIsLove(Scene):
    def __init__(self):
        super().__init__()
        self.te_group = VGroup()
        self.am_group = VGroup()
        self.o_group  = VGroup()

    def construct(self):

        self.te_group = self.make_element("Telúrio", "Te", "52")

        self.play(self.te_group.animate.scale(0.6).shift(DOWN*2.5 + LEFT*1.2))

        self.am_group = self.make_element("Amerício", "Am", "95")
        self.play(self.am_group.animate.scale(0.6).shift(DOWN*2.5))

        self.o_group = self.make_element("Oxigênio", "O", "8")
        self.play(self.o_group.animate.scale(0.6).shift(DOWN * 2.5 + RIGHT*1.2))

        group = VGroup(self.te_group, self.am_group, self.o_group)

        self.play(group.animate.scale(10/6).shift(UP*2.5))

        te_text = Text("Pode afetar\no sistema nervoso", font_size=32).shift(LEFT * 5 + DOWN * 2.5)
        te_line = Line(
            start=self.te_group[0].get_left(),
            end=te_text.get_right() + LEFT * 2 + UP * 0.5
        )

        self.play(Create(te_line))
        self.play(Create(te_text))

        am_text = Text("É difícil de encontrar", font_size=32).shift(DOWN*2.5)
        am_line = Line(
            start=self.am_group[0].get_bottom(),
            end=am_text.get_top() + UP*0.25
        )

        self.play(Create(am_line))
        self.play(Create(am_text))

        o_text = Text("Não posso viver sem", font_size=32).shift(RIGHT * 5 + DOWN * 2.5)
        o_line = Line(
            start=self.o_group[0].get_right(),
            end=o_text.get_right() + LEFT * 2 + UP * 0.5
        )

        self.play(Create(o_line))
        self.play(Create(o_text))

        self.wait(0.7)

        title = Text("O amor é pura química", font_size=64).shift(UP * 3)

        underline = Line(
            start=title.get_left() + DOWN * 0.28,
            end=title.get_right() + DOWN * 0.28,
            stroke_width=2,
        )

        self.play(Create(title), run_time=1.5)
        self.play(Create(underline))

        self.wait(5)

    def make_element(self, name, symbol, number):
        square = Square()
        square.set_stroke(width=3)
        square.set_fill(color=DARKER_GRAY, opacity=0.5)

        symbol = Text(symbol)
        symbol.scale(1.3)

        sub = Text(name)
        sub.shift(DOWN * 0.75).scale(0.4)

        num = Text(number)
        num.shift(UP * 0.7).shift(LEFT * 0.7).scale(0.5)

        self.play(FadeIn(square))
        self.play(Create(symbol))
        self.play(Create(sub))
        self.play(Create(num))

        return VGroup(square, symbol, sub, num)
