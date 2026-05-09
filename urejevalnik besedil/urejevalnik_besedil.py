from time import sleep
from random import randint
import unicodedata

version = "2.5.19"

with open("besede.txt", "r", encoding="utf-8") as f:
    content = f.read().lstrip()
with open("besede.txt", "w", encoding="utf-8") as f:
    f.write(content)


maininput = str(input('ali želite zagnati urejevalnik besedil (ja = j, ne = n)? '))
#_______________________________________________________________________________________________________________________
if maininput == "x":
    filePlace = "exc"#str(input(r"vpišite kraj besedila (primer: C:\MAJ\Python\python projekti\PyCharm Projects\doma\urejevalnik besedil\besedilo.txt): "))
    #input

    if filePlace == 'exc':
        filePlace = r'C:\MAJ\Python\python projekti\PyCharm Projects\doma\urejevalnik besedil\besedilo.txt'

    does_file_works:bool = False
    try:
        with open(filePlace, "r", encoding="utf-8"):
            does_file_works = True
    except FileNotFoundError:
        does_file_works = False
        print(f'FileNotFoundError::računalnik ne najde datoteke s takim imenom: "{filePlace}".')

    if does_file_works:
        with open(filePlace, "r", encoding="utf-8") as file:
            words = file.read().lower()

        for ch in ['.', ',', '?', '!', '(', ')', ':', ';', '-', '+', '/', '*', '–']:
            words = words.replace(ch, '')

        words = (
            words
            .replace("š", "s")
            .replace("č", "c")
            .replace("ž", "z")
            .replace("\n", " ")
            .replace("0", "")
            .replace("1", "")
            .replace("2", "")
            .replace("3", "")
            .replace("4", "")
            .replace("5", "")
            .replace("6", "")
            .replace("7", "")
            .replace("8", "")
            .replace("9", "")
            .replace("í", "i")
            .replace("ó", "o")
            .replace("á", "a")
        )
        words = words.replace(" ", "\n")
        words = "\n" + words
        words = words.splitlines()
        words = sorted(words)

        with (open("besede.txt", "a", encoding="utf-8") as infilew, \
              open("besede.txt", "r", encoding="utf-8") as infiler):
            infile_list = infiler.read().lstrip().splitlines()
            okwords:list[str] = []
            for _i in words:
                if _i not in infile_list:
                    if _i not in okwords:
                        okwords.append(_i)
                else:
                    continue
            print(f'V bazo smo dodali: {okwords[1:]}.')
            ok_infilew_list = "\n".join(okwords)
            infilew.write(ok_infilew_list)
        words = "\n".join(words)
        word_list = words.split()
        print(word_list)
        with open("besede.txt", 'r', encoding="utf-8") as file:
            lines = str(file.read())
            lines = lines.splitlines()
            lines = sorted(lines)
            print(f'število besed v bazi: {len(lines)}.')
            lines = "\n".join(lines)
            with open("besede.txt", "w", encoding="utf-8") as filewrite:
                filewrite.write(lines)
    print(f"infos: version:{version}")
    print(f"       author : Maj Flajnik")
#_______________________________________________________________________________________________________________________
elif maininput == "j" or maininput == "j -mode -db" or maininput == "j -m -db": #db-debug

    with open("besede.txt", 'r') as data:
        vwords = data.read().replace("\n", " ").lower().split()
        if maininput == "j -mode -db" or maininput == "j -m -db":
            print(f"output: /*{vwords}")
        else:
            print("output: /* Napaka:Nimate dovoljenja")
    with open("besedilo.txt", 'r', encoding='utf-8') as valid:
        text = unicodedata.normalize("NFC", valid.read())
        words = (text
                 .replace("\n", " ")
                 .replace("č", "c")
                 .replace("š", "s")
                 .replace("ž", "z")
                 .replace("(", "")
                 .replace(")", "")
                 .replace(".", "")
                 .replace(",", "")
                 .replace("!", "")
                 .replace("?", "")
                 .replace(";", "")
                 .replace("–", "")
                 .lower()
                 .split()
                 )
        if maininput == "j -mode -db" or maininput == "j -m -db":
            print(f"        /*{words}")
        else:
            print("        /* Napaka:Nimate dovoljenja")
    a = False
    for i in words:
        if i not in vwords:
            print(f'Besede "{i}" (še) ni v bazi besed.')
            #koda za predloge
            dumthis = []
            for vrd in vwords:
                #vrd = pravilna beseda
                #i = neznan beseda
                if len(i) <= 2:
                    if i[0] == vrd[0]:
                        dumthis.append(vrd)
                elif 5 >= len(i) >= 3:
                    if i[0:3] == vrd[0:3]:
                        dumthis.append(vrd)
                elif 8 >= len(i) > 5:
                    if i[0:5] == vrd[0:5]:
                        dumthis.append(vrd)
                elif 10 >= len(i) > 8:
                    if i[0:6] == vrd[0:6]:
                        dumthis.append(vrd)
                elif 13 >= len(i) > 10:
                    if i[0:7] == vrd[0:7]:
                        dumthis.append(vrd)
                elif len(i) > 13:
                    if i[0:9] == vrd[0:9]:
                        dumthis.append(vrd)
            print(f"ste morda mislili eno od teh besed: "
                  f"{", ".join(dumthis) if ", ".join(dumthis) != "" else "ni podobnih besed"}"
                  )
            wanadd = str(input(f'želite besedo "{i}" dodati v bazo besed?(j/n) '))
            if wanadd == "j":
                print(f'besedo "{i}" dodajam v bazo besed...')
                with open("besede.txt", 'a', encoding="utf-8") as file:
                    file.write("\n")
                    file.write(i)
                    file.write("\n")
                sleep(0.5)
                print('Beseda uspešno dodana!')
            elif wanadd == "n":
                print('nadaljujem...')
                sleep(0.5)
                print("_____________________________")
            else:
                print('to se šteje kot "ne".')
                print("_____________________________")
            a = True
    if not a:
        print('vse besedo so pravilne (vse besede so v bazi besed).')

    with open("besede.txt", 'r', encoding="utf-8") as file:
        lines = str(file.read())
        lines = lines.splitlines()
        lines = sorted(lines)
        print(f'število besed v bazi: {len(lines)}')
        lines = "\n".join(lines)
        with open("besede.txt", "w", encoding="utf-8") as filewrite:
            filewrite.write(lines)
    print(f"infos: ")
    print(f"       version: {version}")
    print(f"       author : Maj Flajnik")
elif maininput == "n":
    print("terminating code...")
    sleep(randint(1, 3))
elif maininput == "n -s":
    print("terminating code...")
else:
    print('napačen vnos')