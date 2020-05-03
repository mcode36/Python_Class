import turtle

t = turtle.Pen()

def draw_rec(rec_w, rec_h):
    t.forward(rec_w)
    t.left(90)
    t.forward(rec_h)
    t.left(90)
    t.forward(rec_w)
    t.left(90)
    t.forward(rec_h)

draw_rec(70,20)



