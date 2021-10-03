'''
Functia primeste unu numar intreg.
Funcita returneaza True daca numarul introdus este prim,sau false in caz contrar.
'''
def numar_prim(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d  <=  n:
        if n % d == 0:
            return False
        d += 2
    return True
'''
Fucntia returneaza cel mai mare numar prim mai mic strict decat un numar dat.
'''
def get_largest_prime_below(n):
    n = n - 1
    while numar_prim(n) == False and n>=1:
        n = n - 1
    return n 

'''
Fucntia returneanza true daca nr(care reprezinta un an) este bisect 
si false in caz contrar
'''

def an_bisect(nr):
    if nr % 4 == 0 and nr % 100 != 0:
        return True
    if nr % 400 == 0:
        return True
    return False

'''
Functia primieste ziua nasterii,luna nasterii,si anul nasterii(pentru a sti daca este un an bisect,in cazul in care luna este februarie)
Functia o sa returneze zilele ramase pana la sfarsitul lunii din momentrul zilei nasterii
'''

def zile_ramase_din_luna_nasterii(zi_nastere,luna_nastere,an_nastere):
    if luna_nastere == 2:
        if an_bisect(an_nastere) == True:
            return 29 - zi_nastere
        else:
            return 28 - zi_nastere
    else:
        if luna_nastere <= 7:
            if luna_nastere % 2 == 1:
                return 31 - zi_nastere
            else:
                return 30 - zi_nastere
        else:
            if luna_nastere % 2 == 1:
                return 30 - zi_nastere
            else:
                return 31 - zi_nastere

'''
fucntia calculeaza si returneaza numarul de zile dintre anul x si anul y
excluzand anul x si anul y
'''

def zile_dintre_anul_nasterii_si_cel_curent(an_nastere,an_curent):
    suma_zile = 0
    while an_nastere < an_curent:
        if an_bisect(an_nastere):
            suma_zile += 366
        else:
            suma_zile += 365
        an_nastere += 1
    return suma_zile

'''
In cazul in care anul a nasterii a fost diferit de cel curent,si am ajuns in anul curent
va trebuii sa calculam zilele trecute de la inceputul anului pana in prezent.
Date de intrare: zi_nastere=ziua care o vom folosii sa ajungem pe ziua curenta,luna_nastere -||-||- luna curenta,an_nastere...si zi,luna_curenta care repezinta
datele din prezent...(anul curent nu trebuie folosit deoarece anul curent = anu nastere)
returenaza nuamrul zilelor de la inceputul anului pana in prezent in cazul in care persoana nu s-a nuascut anul din prezent
'''

def zile_trecut_din_din_anul_curent_pana_in_prezent(zi_nastere,luna_nastere,an_nastere,zi_curenta,luna_curenta):
    zi_nastere = 1
    luna_nastere = 1
    suma_zile = 0
    while luna_nastere < luna_curenta:
        if luna_nastere == 2:
            if an_bisect(an_nastere):
                suma_zile += 29
                luna_nastere += 1
            else:
                suma_zile += 28
                luna_nastere += 1
        elif luna_nastere <= 7:
            if luna_nastere % 2 == 1:
                suma_zile += 31
                luna_nastere += 1
            else:
                suma_zile += 30
                luna_nastere += 1
        else:
            if luna_nastere % 2 == 1:
                suma_zile += 30
                luna_nastere += 1
            else:
                suma_zile += 31
                luna_nastere += 1
    return (suma_zile + zi_curenta)

'''
functia get_age_in_days ia un tip de date de forma
zi/luna/an
si retureanaza numarul de zile din data selectata pana in data
prezenta
'''
def get_age_in_days(birthday)-> int:
    zi_nastere = birthday[0]
    luna_nastere = birthday[1]
    an_nastere = birthday [2]
    import datetime
    current_date = datetime.date.today()
    zi_curenta = current_date.day
    luna_corenta = current_date.month
    an_curent = current_date.year
    suma_zile = 0
    if an_nastere == an_curent: #cazul in care anul nasterii este egal cu anul curent v-a fi tratat separata
        if luna_nastere == luna_corenta:
            suma_zile += zi_curenta - zi_nastere
        else:
            suma_zile += zile_ramase_din_luna_nasterii(zi_nastere,luna_nastere,an_nastere)
            luna_nastere += 1
            while luna_nastere < luna_corenta:
                if luna_nastere == 2:
                    if an_bisect(an_nastere) == True:
                        suma_zile += 29
                        luna_nastere += 1
                    else:
                        suma_zile +=28
                        luna_nastere +=1
                elif luna_nastere <=7:
                    if luna_nastere % 2 ==1:
                        suma_zile += 31
                        luna_nastere +=1
                    else:
                        suma_zile +=30
                        luna_nastere+= 1
                else:
                    if luna_nastere % 2 ==1:
                        suma_zile += 30
                        luna_nastere += 1
                    else:
                        suma_zile += 31
                        luna_nastere += 1
            suma_zile += zi_curenta

    else:
        suma_zile = zile_ramase_din_luna_nasterii(zi_nastere,luna_nastere,an_nastere)
        luna_nastere += 1
        while luna_nastere <= 12:
            if luna_nastere == 2:
                if an_bisect(an_nastere):
                    suma_zile += 29
                    luna_nastere += 1
                else:
                    suma_zile += 28
                    luna_nastere += 1
            elif luna_nastere <= 7:
                if luna_nastere % 2 == 1:
                    suma_zile += 31
                    luna_nastere += 1
                else:
                    suma_zile += 30
                    luna_nastere += 1
            else:
                if luna_nastere % 2 == 1:
                    suma_zile += 30
                    luna_nastere += 1
                else:
                    suma_zile += 31
                    luna_nastere += 1
        an_nastere += 1
        suma_zile += zile_dintre_anul_nasterii_si_cel_curent(an_nastere,an_curent)
        an_nastere = an_curent
        suma_zile += zile_trecut_din_din_anul_curent_pana_in_prezent(zi_nastere,luna_nastere,an_nastere,zi_curenta,luna_corenta)
    return suma_zile

'''
Testarea datelor pentru functia de calcul a celui mai mare numar prim mai mic(strict) decat un numar dat.
'''

def test_get_largest_prime_below():
    assert(get_largest_prime_below(3)==2)
    assert(get_largest_prime_below(4)==3)
    assert(get_largest_prime_below(9)==7)
    assert(get_largest_prime_below(10)==7)
    assert(get_largest_prime_below(15)==13)
    assert(get_largest_prime_below(100)==97)

'''
Testarea datelor pentru functia care calculeaza varsta undei persoane in zile.
Datele pentru asertiune au fost preluate is verificate pe platformele:
https://www.topster.ro/calendar/tagerechner.php?styp=datum&stag=21&smonat=7&sjahr=2005&typ=datum&etag=03&emonat=10&ejahr=2021&subDazu=%2B&dazu=3
http://www.timeadate.eu/pages/ro/calculator-days-ro.html
'''

def test_get_age_in_days():
    #in ziua in care au fost scrise aceste date numarul indicat era numarul exact de zile
    assert(get_age_in_days((10,10,2002))>=6933)  
    assert(get_age_in_days((5,4,1998))>=8582)
    assert(get_age_in_days((21,7,2005))>=5918)

'''
Functia centrala care preia datele,si creeaza un meniu pentru utilizator.
'''

def main():
    while True:
        print('1.   Ultimul numar prim mai mic decat un numar dat.')
        print('2.   Varsta persoanei in zile.')
        print('x    Exit')
        optiune = input('Introduceti optiunea: ')
        if optiune == '1':
             x = int(input('Introduceti numarul: '))
             if x < 2:
                print('Nu exista.') 
             else:
                print(f'Cel mai mare numar prim mai mic strict decat {x} este: ',get_largest_prime_below(x))
                test_get_largest_prime_below()
        elif optiune == '2':
            data_nastere=[1,2,3]
            data_nastere[0] = int(input('Intoruceti ziua nasterii: '))
            data_nastere[1] = int(input('Intoruceti luna nasterii: '))
            data_nastere[2] = int(input('Intoruceti anul nasterii: '))
            print(f'Varsta persoanei care s-a nascut in {data_nastere[0]}.{data_nastere[1]}.{data_nastere[2]} este de: ',get_age_in_days(data_nastere),' zile.')
            test_get_age_in_days()
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida !')

main()