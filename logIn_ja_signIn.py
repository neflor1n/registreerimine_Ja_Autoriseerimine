from reg_ja_aut import *

# users = []
# passwords = []

while True:
    # try:
        u, p = load_user_data('UserDate')
        print('\n# --------------- MENU ----------------- #')
        print('\n1 - Näita kõiki kasutajaid\n2 - Registreerimine\n3 - Autoriseerimine\n4 - Unustatud parool\n'
              '5 - Muuta kasutajanimi või parool\n6 - Mine välja\n')
        print('# -------------------------------------- #')
        valik = int(input())
        if valik == 1:
            print()
            # print(u)
            # print(p)
            andmed_veerudes(u, p)
        elif valik == 2:
            registreerimine(u, p)
            kirjutaFailisse('UserDate', u, p)
        elif valik == 3:
            autoriseerimine(u, p)
        elif valik == 4:
            unustatud_parool(u, p)
        elif valik == 5:
            muuta_kasutajanimi_ja_parool(u, p)
            kirjutaFailisse('UserDate', u, p)
        elif valik == 6:
            #kirjutaFailisse('UserDate', u, p)
            break
    # except:
    #     print(ValueError)



