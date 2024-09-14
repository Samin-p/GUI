from not_able import randomwalk
import matplotlib.pyplot as p

rw=randomwalk()

rw.walk()
p.style.use("classic")
fig,ax=p.subplots()
ax.scatter(rw.x_value,rw.y_value,s=15)
ax.set_aspect("equal")
p.show()
