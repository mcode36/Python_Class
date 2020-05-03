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

w = 70 - 20
h = 20 - 10
t.left(180)

for i in range(0,4):
    t.left(180)
    w += 20
    h += 10
    draw_rec(w,h)



