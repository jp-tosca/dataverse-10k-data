import random
import re
import os
import shutil
from cairosvg import svg2png

generated_files = 10000
dir_path = './genLogo'
shutil.rmtree(dir_path)
os.mkdir(dir_path)

with open('dvlogohr.svg', 'r') as file:
    svg_code = file.read()

for _ in range(generated_files):
    random_color = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))
    print(random_color)
    svg_code_tmp = re.sub(r'#c65b28', random_color, svg_code)
    svg2png(bytestring=svg_code_tmp, write_to=f'./genLogo/output{_}.png')