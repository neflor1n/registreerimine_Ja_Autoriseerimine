import string
import smtplib, ssl
import os
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def list_1(u:list, p: list) -> str:
    ''' Функция возвращает пароли из листа в строку

    :param list p:
    :rtype: str
    '''
    return ''.join(map(str, p)) # map(str, p) используется для того, чтобы преобразовать каждый элемент списка в строку перед объединением



def andmed_veerudes(u: str, p: str):
    """ Funktsioon kuvab ekraanile kahe jarjendite andmed veerudes

    :param list nimi:
    :param list palga:
    """
    for j in range(len(u)):
        print(u[j] + ":", p[j])



def registreerimine(u:list, p:list):
    """
    Registreerib uue kasutaja süsteemi.
    """


    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0 + str1 + str2 + str3
    #print(str4)
    ls = list(str4)
    random.shuffle(ls)
    username = input("Sisestage oma kasutajanimi: ")
    if username != u:
        u.append(username)
        #kirjutaFailisse('UserDate')
        num = int(input("kas sa tahad genereerida parool voi sisesta? (1 - genereerida/2 - sisesta oma): "))
        if num == 1:
            psword = ''.join([random.choice(ls)
                              for x in range(12)])
            p.append(psword)
            print("Teie loodud parool:", psword)
            print("Sa oled registreeritud")
            # with open('UserDate.txt', 'w', encoding = 'utf-8') as file:
            #     file.write(f'{username}: {psword}\n')
            # file.close()
            #kirjutaFailisse('UserDate')
        elif num == 2:
            password_2 = input('Sisesta oma parool: ')
            message = "Nõrk parool. Soovitused: "
            set1 = (len(password_2)) > 11
            set2 = all(char in password_2 for char in str0)
            set3 = all(char in password_2 for char in str1)
            set4 = all(char in password_2 for char in str2)
            set5 = all(char in set(password_2) for char in set(str4))
            rules = [set1, set2, set3, set4, set5]
            p_ = set(password_2)
            a = set(str4)
            result = []
            for x in p_:
                result.append(x in a)
            if all(result) is False:
                print('Viga: illegaalne erimark')
            elif all(result) is True:
                if set1 is False:
                    message += ' suurendage märkide arvu -'+" "+str(12- len(password_2))+','
                if set2 is False:
                    message += ' ' + "lisage 1 erimärk, "
                if set3 is False:
                    message += 'lisada 1 suurtäht, '
                if set4 is False:
                    message += "lisage 1 number, "
                    print(message[:(len(message) - 1)])
                return password_2
            else:
                if all(rules) is True:
                    print("Tugev parool")
            korda_pas = input('Sisestage oma parool veel kord: ')
            if korda_pas == password_2:
                p.append(password_2)
               #kirjutaFailisse('UserDate')
                print("Sa oled registreeritud!")
                # with open("UserDate.txt", 'w', encoding = 'utf-8') as file:
                #     file.write(f'{username}: {password_2}\n')
                # file.close()
            else:
                print("Sa sisestasid parooli valesti")
                return password_2
        else:
            print("See parool on juba, sisestage uus parool")
            return num
    else:
        print("See kasutajanimi on juba, palun, sisestage erinev kasutajanimi!")


def autoriseerimine(u: list, p:list):
    """ Autoriseerimine

    :param list u:
    :param list p:
    :return:
    """

    logIn_username = input("Sisesta sinu kasutajanimi: ")

    if logIn_username in u or load_user_data('UserDate.txt'):
        logIn_password = input("Sisesta sinu parool: ")
        if logIn_password in p:
            print("Sa oled autoriseeritud")
        else:
            print("Vale parool")
            return logIn_password
    else:
        print("Vale username")
        return logIn_username

def unustatud_parool(u: list, p: list):
    """ Parooli taastamine. Unustatud parool saadetakse kasutaja meilile

    :param list u:
    :param list p:
    :return:
    """
    global server
    nimi = input("Sisesta oma nimi:")
    if nimi in u:
        ind = u.index(nimi)
        unustatud_parool_ = str(p[ind])
        try:
            context = ssl.create_default_context()
            smtp_server = "smtp.gmail.com"
            port = 587
            sender_email = "bsergachev@gmail.com"
            receiver_email = input("Sisesta oma emaili aadress: ")
            password = input("Type your password and press enter: ")
            subject = "Unustatud parool"
            body = f"Teie unustatud parool on: {unustatud_parool_}"

            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))
            msg = message.as_string()

            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg)
            print("Unustatud parool on saadetud teie email")
        except Exception as e:
            print("Midagi läks valesti:", e)
        finally:
            server.quit()
    else:
        print("Sisestatud hüüdnime pole olemas või see on valesti sisestatud")



def kirjutaFailisse(fail: str, u = [], p = []):
    """ Faili kirjutamine antud järjendi sisuga.

    :param fail:
    :param jarjend:
    :return:
    """
    f = open(fail, 'w', encoding="utf-8")
    for i in range(len(u)):
        f.write(u[i] + ": " + p[i] + '\n')
    f.close()


def muuta_kasutajanimi_ja_parool(u: list, p: list):
    """

    :param u:
    :param p:
    :return:
    """
    name = input('Sisesta oma kasutajanimi: ')
    if name in u:
        ind = u.index(name)
        old_password = input('Sisesta oma vana parool: ')
        if old_password in p[ind]:
            new_password = input('Sisesta uus parool: ')
            p[ind] = new_password
            print("Parool muudetud!")
        else:
            print('Vale vana parool!')
            return old_password
    else:
        print('Seda nime pole olemas või see on valesti sisestatud!')
        return name








def load_user_data(fail:str):
    """
    Функция загружает данные пользователя из файла

    """
    u = []
    p = []
    f = open(fail, 'r', encoding="utf-8")  # try
    for line in f:
        n = line.find(": ")  # login: password - разделитель
        u.append(line[0:n].strip())
        p.append(line[n + 1:len(line)].strip())
    f.close()
    return u, p



