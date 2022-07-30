from manim import *

class Guidorizzi(Scene):
    def construct(self):
        self.introduce_problem()
        self.wait()
        self.show_proof()
        self.wait()
        self.demonstration_about_a()
        self.wait()
        self.demonstration_about_b()
        self.conclusion()
    

    def introduce_problem(self):
        statement = Tex(r"Seja f(x, y) diferenciável e sejam $\vec{u}$ e $\vec{v}$ \\ dois vetores de $\mathbb{R}^2$, unitários e ortogonais. Prove:")
        prove = MathTex(r"\nabla f(x, y) = \frac{\partial f}{\partial \vec{u}}(x, y) \vec{u} + \frac{\partial f}{\partial \vec{v}}(x, y) \vec{v}") 

        vg = VGroup().add(statement, prove)
        vg.arrange(DOWN, buff=MED_LARGE_BUFF)
        
        self.play(Write(statement), run_time=5)
        self.wait(2)
        self.play(Write(prove), run_time=5)
        self.play(Circumscribe(prove))
        self.wait(2)

        #self.play(vg.animate.to_edge(UP, buff=SMALL_BUFF))
        self.play(FadeOut(vg, shift=UP))
        self.np = NumberPlane()
        self.play(FadeIn(self.np))


    def show_proof(self):
        text = Tex(r"Podemos escrever $\nabla f(x, y)$ como \\ combinação linear de $\vec{u}$ e $\vec{v}$").to_corner(LEFT + UP, buff=SMALL_BUFF).set_font_size(40).shift(DOWN* 0.4)
        self.play(FadeIn(text))
        self.wait(2)
        self.play(FadeOut(text))

        # Base vectors
        vec_u = Arrow(ORIGIN, [1, 0, 0], buff=0).set_color(TEAL)
        txt_u = MathTex(r"\vec{u}").next_to(0.5*(0.8*vec_u.get_end() + DOWN), buff=0)
        vec_v = Arrow(ORIGIN, [0, 1, 0], buff=0).set_color(GREEN)
        txt_v = MathTex(r"\vec{v}").next_to(0.5*(vec_v.get_end() + LEFT), buff=0)

        self.play(GrowArrow(vec_u), GrowArrow(vec_v), run_time=3)
        self.play(FadeIn(txt_u), FadeIn(txt_v))

        # Gradient vector
        grad = Arrow(ORIGIN, [3, 3, 0], buff=0)
        grad_tex = Tex(r"$\nabla f(x, y)$").next_to(grad.get_end() + 0.2*UP, RIGHT)
        self.play(GrowArrow(grad), FadeIn(grad_tex),run_time = 3)

        # gradient linear combination
        vec_au = Arrow(ORIGIN, [3, 0, 0], buff=0).set_color(TEAL)
        txt_au = MathTex(r"a\vec{u}").next_to(0.5*(0.8*vec_au.get_end() + DOWN), buff=0)
        vec_bv = Arrow(ORIGIN, [0, 3, 0], buff=0).set_color(GREEN)
        txt_bv = MathTex(r"b\vec{v}").next_to(0.5*1.2*(vec_bv.get_end() + 1.2*LEFT), buff=0)

        #self.add(vec_au, vec_bv, txt_au, txt_bv)
        self.play(GrowArrow(vec_au), GrowArrow(vec_bv), run_time=3)
        self.play(FadeIn(txt_au), FadeIn(txt_bv))

        gp = Group(grad, grad_tex, vec_au, txt_au, vec_bv, txt_bv, vec_u, txt_u, vec_v, txt_v)

        self.wait()

        txt = Tex(r"Logo $\nabla f(x, y)$ é uma soma de vetores:").set_font_size(40)
        self.main_txt = MathTex(r"\nabla f(x, y) = ", r"a", r"\vec{u} + ", r"b", r"\vec{v}").set_font_size(40)
        vg = VGroup(txt, self.main_txt).arrange(DOWN, buff=MED_SMALL_BUFF).to_edge(DOWN, buff=LARGE_BUFF)
        self.play(FadeIn(vg))
        self.play(self.main_txt[1].animate.set_color(YELLOW), self.main_txt[3].animate.set_color(YELLOW))

        self.wait(3)

        self.play(FadeOut(txt), gp.animate.scale(0.5).to_corner(LEFT+ UP, buff=0.3), self.main_txt.animate.to_edge(UP, buff=MED_LARGE_BUFF), run_time=2)
        self.wait(2)

        self.play(Uncreate(self.np))
        self.wait()

        txt3 = Tex(r"Mostremos que a = $\frac{\partial f}{\partial \vec{u}}$ e b = $\frac{\partial f}{\partial \vec{v}}$").set_font_size(40)
        self.play(FadeIn(txt3))
        self.wait(2)
        self.play(FadeOut(txt3))
        self.wait(1)


    def demonstration_about_a(self):
        equation = [
            Tex(
                r"Se $\vec{u} \perp \vec{v} \ \therefore \vec{u} \cdot \vec{v} = 0.$",
            ),
            MathTex(
                r"\nabla f(x, y) ", r"\cdot \vec{u}", r"=\left(a\vec{u} + b\vec{v} \right) ",  r"\cdot \vec{u}",
            ),
            MathTex(
                r"\nabla f(x, y) ", r"\cdot \vec{u}", r"= a\underbrace{(\vec{u} \cdot \vec{u})}_{1} + b\underbrace{(\vec{v} \cdot \vec{u}}_{0})",
            ),
            MathTex(
                r"\nabla f(x, y) ", r"\cdot \vec{u} ", r"=a",
            ),
        ]

        vg = VGroup()
        u_11 = equation[1][1].set_color(BLUE_C)
        u_13 = equation[1][3].set_color(BLUE_C)
        for line in equation:
            #line.set_color_by_tex(vec, BLUE_C)
            vg.add(line)
        vg.arrange(DOWN, buff=0.2)

        for tex in equation:
            self.play(Write(tex), run_time = 2.5)
            if tex == equation[1]:
                self.play(Indicate(u_11, color=BLUE_B), Indicate(u_13, color=BLUE_B), run_time=2)
            self.wait()
        self.wait(2)

        tex = Tex(r"Mas, por definição \\ $\nabla f(x, y) \cdot \vec{u} = \frac{\partial f}{\partial \vec{u}}(x, y) \ \therefore a = \frac{\partial f}{\partial \vec{u}}(x, y)$")
        
        vg.add(tex)
        vg.arrange(DOWN, buff=0.4)
        self.play(FadeIn(vg), run_time = 3)
        self.play(Circumscribe(tex), run_time=2)

        self.wait(2)

        self.play(FadeOut(vg))


    def demonstration_about_b(self):
        equation = [
            Tex(
                r"Se $\vec{u} \perp \vec{v} \ \therefore \ \vec{u} \cdot \vec{v} = 0.$",
            ),
            MathTex(
                r"\nabla f(x, y) ", r"\cdot \vec{v}", r"=\left(a\vec{u} + b\vec{v} \right) ",  r"\cdot \vec{v}",
            ),
            MathTex(
                r"\nabla f(x, y) ", r"\cdot \vec{v}", r"= a\underbrace{(\vec{u} \cdot \vec{v})}_{0} + b\underbrace{(\vec{v} \cdot \vec{v}}_{1})",
            ),
            MathTex(
                r"\therefore \nabla f(x, y) ", r"\cdot \vec{v} ", r"=b",
            ),
        ]

        vg = VGroup()
        v_11 = equation[1][1].set_color(GREEN_B)
        v_13 = equation[1][3].set_color(GREEN_B)
        for line in equation:
            #line.set_color_by_tex(vec, BLUE_C)
            vg.add(line)
        vg.arrange(DOWN, buff=0.2)

        for tex in equation:
            self.play(Write(tex), run_time = 2.5)
            if tex == equation[1]:
                self.play(Indicate(v_11, color=GREEN_A), Indicate(v_13, color=GREEN_A), run_time=2)
            self.wait()
        self.wait(2)

        self.play(Circumscribe(equation[3]))
        self.play(FadeOut(vg))

    def conclusion(self):
        a, b = MathTex(r"\nabla f(x, y)", r"\cdot \vec{u}", r"= \frac{\partial f}{\partial \vec{u}}(x, y)", r"=", r"a"), MathTex(r"\nabla f(x, y)", r"\cdot \vec{v}", r"= \frac{\partial f}{\partial \vec{v}}(x, y)", r"=", r"b")
        a[1].set_color(BLUE_B)
        b[1].set_color(GREEN_B)
        a[4].set_color(YELLOW)
        b[4].set_color(YELLOW)

        gp = VGroup(a, b).arrange(DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(a[:len(a) - 2]), run_time=3)
        self.play(Write(b[:len(a) - 2]), run_time=3)
        self.wait(0.5)
        self.play(Write(a[(len(a) - 2):]), run_time=2)
        self.play(Write(b[(len(a) - 2):]), run_time=2)

        self.play(gp.animate.scale(0.7).to_corner(DOWN, buff=0.3))

        final = MathTex(
            r"\nabla f(x, y) = ", r"\frac{\partial f}{\partial \vec{u}}(x, y)", r"\vec{u} + ", r"\frac{\partial f}{\partial \vec{v}}(x, y)", r"\vec{v}"
        )
        final[1].set_color(BLUE)
        final[3].set_color(GREEN)

        self.wait()
        self.play(Write(final), run_time=5)
        self.wait()
        self.play(Indicate(final[1]), Indicate(final[3]), run_time=2)
        self.play(Circumscribe(final))

        self.wait(2) 