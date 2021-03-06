# -*- coding: utf-8 -*-

from gimpfu import *


def plugin_main(image, drawable, path):
    if not path.endswith(".dds"):
        gimp.message('Invalid file: ' + path)
        return

    new_image = pdb.gimp_image_duplicate(image)
    drawable = pdb.gimp_image_merge_visible_layers(new_image, CLIP_TO_IMAGE)
    drawable = pdb.gimp_item_transform_flip_simple(drawable, 1, True, 0.0)
    try:
        pdb.file_dds_save(new_image, drawable, path, path
                          , 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        pdb.gimp_image_delete(new_image)
    except WindowsError as e:
        gimp.message(str(e))
    except RuntimeError as e:
        print(str(e))


register(
    "python-fu-plugin-notruf_en",
    "Export as Emergency Call 112 Skin",
    "Export as Emergency Call 112 Skin",
    "Kaktushose",
    "Kaktushose",
    "2020",
    "<Image>/Image/Export as Emergency Call 112 Skin...",
    "*",
    [
        (PF_FILENAME, "Path", "File", "")
    ],
    [],
    plugin_main)

main()
