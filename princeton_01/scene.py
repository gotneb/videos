from manim import *

class PrincetonQuestion(Scene):
    def construct(self):
        self.introduce_problem()
        self.wait()
        self.solve_problem()
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
            vg.animate.to_corner(RIGHT + UP, buff=0.2).scale(0.65),
            run_time = 2.5,
        )

        equation = MathTex(r"\sqrt{7 + 4 \sqrt{3}} \ + \ \sqrt{7 - 4 \sqrt{3}} \ = \ ?", font_size=60, color = BLACK)
        frame = SurroundingRectangle(equation, buff=0.7, color=BLACK)
        self.play(Write(equation))
        self.play(Create(frame))
        self.wait(4)
        self.play(FadeOut(frame), FadeOut(equation), run_time = 1.5)
    

    def solve_problem(self):
        def CustomMathTex(text, size = 40):
            return MathTex(text, font_size= size, color=BLACK)
        

        equation = [
            CustomMathTex(r"\sqrt{7 + 4 \sqrt{3}} \ + \ \sqrt{7 - 4 \sqrt{3}} \ = \ ?"),
            CustomMathTex(r"x = \sqrt{7 + 4\sqrt{3}} \ + \ \sqrt{7 - 4 \sqrt{3}}"),
            CustomMathTex(r"x^2 = \left(\sqrt{7 + 4  \sqrt{3}} \ + \ \sqrt{7 - 4  \sqrt{3}}\right)^2"),
            CustomMathTex(r"x^2 = \left(\sqrt{7 + 4 \sqrt{3}}\right)^2 \ + \ \left(\sqrt{7 - 4  \sqrt{3}}\right)^2 + \ 2 \sqrt{\left(7+4\sqrt{3}\right)\left(7-4\sqrt{3}\right)}"),
            CustomMathTex(r"x^2 = 7 + 4 \sqrt{3} \ + \ 7 - 4 \sqrt{3} + \ 2\sqrt{49 - 16\times3}"),
        ]

        vg = VGroup()
        for i in range(0, len(equation)):
            vg.add(equation[i])
        vg.arrange(DOWN, buff= MED_LARGE_BUFF)

        for i in range(0, len(equation)):
            self.play(Write(equation[i]))
            self.wait()
        
        self.play(FadeOut(vg))

        vg_right = VGroup()

        continue_equation = [
            CustomMathTex(r"x^2 = 14 \ + \ 2\sqrt{49 - 48}"),
            CustomMathTex(r"x^2 = 14 \ + \ 2\sqrt{1} \ = 14 + 2 = 16"),
            CustomMathTex(r"\therefore x = \pm\sqrt{16}"),
            CustomMathTex(r"Mas, x \geq 0 \\ \therefore x = 4"),
        ]

        for i in range(0, len(continue_equation)):
            vg_right.add(continue_equation[i])
        vg_right.arrange(DOWN)

        for i in range(0, len(continue_equation)):
            self.play(Write(continue_equation[i]))
            if i >= len(continue_equation) - 2:
                self.wait(2)
            else:
                self.wait()