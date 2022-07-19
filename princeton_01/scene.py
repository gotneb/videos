from manim import *

class PrincetonQuestion(Scene):
    def construct(self):
        self.introduce_problem()
        self.wait()
    

    def introduce_problem(self):
        self.camera.background_color = WHITE
        logo = ImageMobject("assets/princeton_logo.png")
        name = Text("Princeton University", font_size = 20, color=BLACK)

        vg = Group()
        vg.add(logo, name)
        vg.arrange(DOWN)

        self.play(FadeIn(logo), FadeIn(name))
        self.wait()
        self.play(FadeOut(name))
        vg.remove(name)
        self.play(
            vg.animate.to_corner(RIGHT + UP, buff=0).scale(0.65),
            run_time = 2.5,
        )

        equation = MathTex(r"\sqrt{7 + 4 \sqrt{3}} \ + \ \sqrt{7 - 4 \sqrt{3}} \ = \ ?", font_size=60, color = BLACK)
        frame = SurroundingRectangle(equation, buff=0.7, color=BLACK)
        self.play(Write(equation))
        self.play(Create(frame))
        self.wait(4)
        self.play(FadeOut(frame), FadeOut(equation), run_time = 1.5)
    

    def solve_problem(self):
        size = 50
        equation = [
            MathTex(r"\sqrt{7 + 4 \sqrt{3}} \ + \ \sqrt{7 - 4 \sqrt{3}} \ = \ ?", font_size= size),
            MathTex(r"x = \sqrt{7 + 4\sqrt{3}} \ + \ \sqrt{7 - 4 \sqrt{3}}", font_size= size),
            MathTex(r"x^2 = \left(\sqrt{7 + 4  \sqrt{3}} \ + \ \sqrt{7 - 4  \sqrt{3}}\right)^2", font_size= size),
            MathTex(r"x^2 = \left(\sqrt{7 + 4 \sqrt{3}}\right)^2 \ + \ \left(\sqrt{7 - 4  \sqrt{3}}\right)^2 + \ 2\sqrt{\left(7+4\sqrt{3}\right)\left(7-4\sqrt{3}\right)}", font_size= size - 10),
            MathTex(r"x^2 = 7 + 4 \sqrt{3} \ + \ 7 - 4 \sqrt{3} + \ 2\sqrt{49 - 16\times3}", font_size= size),
            MathTex(r"x^2 = 14 \ + \ 2\sqrt{49 - 48}", font_size= size),
            MathTex(r"x^2 = 14 \ + \ 2\sqrt{1} \ = 14 + 2 = 16", font_size= size),
            MathTex(r"\therefore x = \pm\sqrt{16}", font_size= size)
        ]

        vg = VGroup()
        for i in range(0, len(equation)):
            vg.add(equation[i])
        vg.arrange(DOWN)

        for i in range(0, len(equation)):
            self.play(Write(equation[i]))
            self.wait()


class Testing(Scene):
    def construct(self):
        tex = MathTex(r"a^2 = b^2 + c^2", font_size=50)

        self.play(Create(tex))