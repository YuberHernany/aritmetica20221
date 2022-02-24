






















import numpy as np
import pandas as pd
import sympy.ntheory as nt
import matplotlib.pyplot as plt
from celluloid import Camera



plt.style.use("dark_background")

fig, ax = plt.subplots()
ax.set(xticks=(), yticks=(),)

arr = np.arange(1, 151).reshape(-1, 6)
ax.text(0, 0, str(arr), fontsize=20)
plt.axis('off')
plt.pause(2)
plt.cla()
arr[0][0] = 0
ax.text(0, 0, str(arr), fontsize=20)
plt.axis('off')
plt.pause(1)
plt.cla()

tiempos = [0.1,0.2,0.6,1,2,3]
primos = [2,3,5,7,11,13]

for t, p in zip(tiempos, primos):
    for i in range(len(arr)):
        for j in range(len(arr.T)):
            if (arr[i,j] != p) and (arr[i,j] != 0) and (arr[i,j] % p == 0):
                arr[i,j] = 0
                ax.text(0, 0, str(arr), fontsize=20)
                plt.axis('off')
                plt.pause(t)

                plt.cla()

plt.show()



# #######################   PARA CREAR VIDEO ###################
# plt.style.use("dark_background")
#
# fig, ax = plt.subplots()
# camera = Camera(fig)
# ax.set(xticks=(), yticks=(),)
#
# arr = np.arange(1, 151).reshape(-1, 6)
# ax.text(0, 0, str(arr), fontsize=20)
# plt.axis('off')
# plt.pause(2)
# camera.snap()
# # plt.cla()
# arr[0][0] = 0
# ax.text(0, 0, str(arr), fontsize=20)
# plt.axis('off')
# plt.pause(1)
# camera.snap()
# # plt.cla()
#
# tiempos = [0.1,0.2,0.6,1,2,3]
# primos = [2,3,5,7,11,13]
#
# for t, p in zip(tiempos, primos):
#     for i in range(len(arr)):
#         for j in range(len(arr.T)):
#             if (arr[i,j] != p) and (arr[i,j] != 0) and (arr[i,j] % p == 0):
#                 arr[i,j] = 0
#                 ax.text(0, 0, str(arr), fontsize=20)
#                 plt.axis('off')
#                 plt.pause(t)
#                 camera.snap()
#                 # plt.cla()
#
# plt.show()
#
#
# anim = camera.animate()
# vid = anim.save('criba_video.mp4')
