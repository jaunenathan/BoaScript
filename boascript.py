import os
import random
import chardet

os.system('cls' if os.name == 'nt' else 'clear')

print("""
 ________________________/ O  \___/
<_____________________________/   \\  

> BoaScript [0.0.1] by Jauneattend
""")

filename = input("Entrez le nom du fichier BoaScript à ouvrir (sans extension) : ")

filename = filename + ".boa"

os.system('cls' if os.name == 'nt' else 'clear')

if os.path.exists(filename):
    with open(filename, 'rb') as f:
        result = chardet.detect(f.read())
    encoding = result['encoding']
    with open(filename, 'r', encoding=encoding) as f:
        for line in f:
            if 'texte="' in line:
                text = line.split('texte="')[1].split('"')[0]
                if '##' in text:
                    text_to_print = text.split("##")[1]
                    for char in text_to_print:
                        color = f"{random.randint(0, 255)};{random.randint(0, 255)};{random.randint(0, 255)}"
                        print(f"\033[38;2;{color}m{char}\033[0m", end="")
                    print()
                elif '#' in text:
                    color_start = text.find('#')
                    color_end = color_start + 7
                    color = text[color_start:color_end]
                    text_to_print = text[color_end:]
                    print(
                        f"\033[38;2;{int(color[1:3], 16)};{int(color[3:5], 16)};{int(color[5:], 16)}m{text_to_print}\033[0m")
                else:
                    print(text)
            elif 'choix' in line:
                choix_num = line.split('choix')[1].split('=')[0]
                choix_text = line.split('choix')[1].split('"')[1]
                print(f"{choix_num}. {choix_text}")

        choix = input("Entrez votre choix (numéro) : ")

        f.seek(0)
        for line in f:
            if f'Solution{choix}=' in line:
                solution_text = line.split('Solution')[1].split('"')[1]
                print(solution_text)
else:
    print("Le fichier n'existe pas.")
