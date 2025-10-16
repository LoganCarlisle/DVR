import warp as wp
import numpy as np
import torch


wp.init()

@wp.struct
class Drop:
    position: wp.vec3
    radius: wp.float32
    weight: wp.float32
    energy: wp.float32
    sigma: wp.float32

@wp.struct
class Ray:
    origin: wp.vec3
    dir: wp.vec3
