import eyed3
import chardet
import tqdm
import os

eyed3.log.setLevel("ERROR")


def get_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp3"):
                yield os.path.join(root, file)


pbar = tqdm.tqdm(get_files('.'))

no_repaired = 0

for fname in pbar:
    pbar.set_description(fname)
    try:
        x = eyed3.load(fname)
    except UnicodeDecodeError:
        continue
    try:
        no_embedded_images = len([i for i in x.tag.images])
    except IndexError as e:
        continue
    if no_embedded_images == 1:
        do_png = True
        img_type = x.tag.images[0].mime_type
        encoding = chardet.detect(x.tag.images[0].image_data[:8])['encoding']
        if encoding is None:
            do_png = False
        if img_type == 'image/png' and do_png:
            if x.tag.images[0].image_data[1:4].decode(encoding=encoding) != 'PNG':
                if x.tag.images[0].image_data[2:4].decode(encoding=encoding) == 'PN':
                    print(f"Repairing {fname}")
                    x.tag.images[0].image_data = bytearray(x.tag.images[0].image_data[1:])
                    x.tag.save(version=(2,3,0))
                    no_repaired +=1
        elif img_type == 'image/jpeg' or img_type == 'image/jpg':
            if x.tag.images[0].image_data[:4] == b'\x00\xff\xd8\xff':
                print(f"Repairing {fname}")
                x.tag.images[0].image_data = x.tag.images[0].image_data[1:]
                x.tag.save(version=(2,3,0))
                no_repaired +=1

print(f"{no_repaired} files repaired")
