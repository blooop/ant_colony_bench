import taichi as ti
import bencher as bch
from video_writer import VideoWriter
ti.init(arch=ti.gpu)
import numpy as np
n = 120
pixels = ti.field(dtype=float, shape=(n * 2, n))


@ti.func
def complex_sqr(z):
    return ti.Vector([z[0]**2 - z[1]**2, z[1] * z[0] * 2])


@ti.kernel
def paint(t: float,c0:float,c1:float):
    for i, j in pixels:  # Parallelized over all pixels
        c = ti.Vector([c0, ti.cos(t) * c1])
        z = ti.Vector([i / n - 1, j / n - 0.5]) * 2
        iterations = 0
        while z.norm() < 20 and iterations < 50:
            z = complex_sqr(z) + c
            iterations += 1
        pixels[i, j] = 1 - iterations * 0.02


gui = ti.GUI("Julia Set", res=(n * 2, n))

class SweepJulia(bch.ParametrizedSweep):
    
    c0 = bch.FloatSweep(default=-0.8,bounds=(-2,0))
    c1 = bch.FloatSweep(default=0.2,bounds=(0,1))

    vid = bch.ResultVideo()

    def __call__(self,**kwargs):
        self.update_params_from_kwargs(**kwargs)
        vr = VideoWriter(gui)

        for i in range(100):
            paint(i * 0.03,self.c0,self.c1)
            vr.update_gui(pixels)

        self.vid = self.gen_video_path("julia")
        vr.write(self.vid)
        return super().__call__()



if __name__ == "__main__":
    run_cfg = bch.BenchRunCfg()
    run_cfg.level = 4
    run_cfg.use_sample_cache=True
    run_cfg.run_tag="4"
    bench =SweepJulia().to_bench(run_cfg)
    bench.plot_sweep("julia")
    bench.report.show()

