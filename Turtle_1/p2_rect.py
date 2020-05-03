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

w = 70
h = 20
draw_rec(w,h)
t.left(180)
draw_rec(w,h)
t.left(180)
draw_rec(w,h)
t.left(180)
draw_rec(w,h)



