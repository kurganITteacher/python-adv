import numpy as np
from PIL import Image

image_name = 'magick.teacher.jpg'
image = Image.open(image_name)

image_np = np.array(image)
print(image_np.size, image_np.shape, image_np.dtype)

image_np_conv = image_np
delta = 50
# print(np.where(image_np_conv <= 255 - delta))
image_np_conv[np.where(image_np_conv <= 255 - delta)] += delta
image_np_conv[np.where(image_np_conv > 255 - delta)] = 255
# image_np_conv[:, :, :] += 26  # uint8 -> 255 + 26 -> -, 25

new_image = Image.fromarray(image_np_conv.astype('uint8'))
save_name = 'magick.teacher_conv.jpg'
new_image.save(save_name)
