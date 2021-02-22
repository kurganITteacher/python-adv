import numpy as np
from PIL import Image

image_name = 'Desert.jpg'
image = Image.open(image_name)
# print(dir(image))
# print(image)
image_np = np.array(image)
print(image_np.size, image_np.shape)
# print(image_np)  # uint8 -> 0..255
image_np_conv = image_np
image_np_conv[:, :, 2][image_np_conv[:, :, 2] <= 225] += 30
# image_np_conv = image_np / 1.2
# image_np_conv = np.zeros(shape=image_np.shape)
# image_np_conv += 127
# image_np_conv[:, :, 0] = 255
# image_np_conv[:, :, 1] = 127
# print(image_np[:, :, 0].mean(), image_np[:, :, 1].mean(),
#       image_np[:, :, 2].mean())
# print(image_np_conv[:, :, 0].mean(), image_np_conv[:, :, 1].mean(),
#       image_np_conv[:, :, 2].mean())

new_image = Image.fromarray(image_np_conv.astype('uint8'))
save_name = 'Desert_conv.jpg'
new_image.save(save_name)
