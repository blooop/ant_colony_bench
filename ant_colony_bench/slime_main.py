# from https://github.com/theAfish/Homework-2-Ant-Colony
from handy_shader_functions import *
from ant_colony import Renderer, Detectables, AntColony, Ants


ti.init(arch=ti.gpu)
dt = 1e-3

rdr = Renderer(600, 600, "Slime Simulation")

ph = Detectables(rdr, 5.0 * dt, 1.0, 1.0)
pf = Detectables(rdr, 5.0 * dt, 1.0, 1.0)
ants = Ants(50000, 1.0, pf, ph, 0.1, 10.0)
ac = AntColony(rdr, ants, ph, pf)

if __name__ == "__main__":
    ac.slime_run()
