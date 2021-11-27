from PIL import Image
import numpy as np


def convert_image_to_mosaic(image, size, gradation_step):
    """
        Конвертирует исходное изображение в изображение с усредненным серым цветом
        для каждых size пикселей и числом градаций серого gradation_step
        :param image: исходное изображение
        :param size: размер одного элемента мозаики
        :param gradation_step: число градаций серого
        :return: изображение с шириной size пикселей одного цвета
    """
    for x in range(0, len(image), size):
        for y in range(0, len(image[0]), size):
            image[x:x + size, y:y + size] = get_average_brightness(
                image[x:x + size, y:y + size], size, gradation_step)
    return image


def get_average_brightness(block, size, gradation_step):
    """
        Возвращает усредненный оттенок для одного пикселя массива block размера size с числом градаций gradation_step
        :param block: исходный массив, полученный из картинки
        :param size: размер элемента мозаики
        :param gradation_step: число градаций серого
        :return: усредненный цвет блока с учетом числа градаций серого
        >>> get_average_brightness(np.array([[[1, 56, 3], [23, 54, 6]], [[4, 87, 67], [102, 36, 91]]]), 1, 5)
        20
    """
    average_color = (block[:size, :size].sum() / 3) // size ** 2
    return int(average_color // gradation_step) * gradation_step


def main():
    image_file = Image.open(input("Введите имя файла, которое хотите конвертировать: "))
    block_size = int(input("Введите размер блока: "))
    gradations_count = int(input("Введите количество градаций серого: "))
    image = np.array(image_file)
    gradation_step = 255 // gradations_count

    res = Image.fromarray(convert_image_to_mosaic(image, block_size, gradation_step))
    res.save(input("Введите имя файла, в которой хотите сохранить результат: "))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
