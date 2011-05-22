import os

import markdown


def process_markdown(src_dir, target_dir):
    md = markdown.Markdown(extensions=['codehilite'])

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            name, ext = os.path.splitext(file)

            in_file = os.path.join(src_dir, file)
            out_file = os.path.join(target_dir, name + '.html')
            md.convertFile(in_file, out_file)
