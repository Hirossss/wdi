saldo = 0
is_kontynuacja= True
pin = input("Zanim skorzysta Pan/Pani z maszyny, proszę podać 4-cyfrowy PIN: ")

while is_kontynuacja:
    print("Jaką operację chce Pan/Pani wykonać: wpłata, wypłata, sprawdzić saldo? Proszę wpisać dokładną nazwę operacji. ")
    operacja = input("Proszę podać wybraną operację: ")
    if operacja=="wpłata":
        spr_pin = input("Zanim operacja zostanie dokonana proszę potwierdzić ją numerem PIN: ")
        if spr_pin != pin:
            exit("Zły PIN, proszę skorzystać ponownie z maszyny. ")
        else:
            kwota_wpłaty = float(input("Proszę podać kwotę do wpłacenia: "))
            saldo+= kwota_wpłaty
            x=input("Czy chce Pan/Pani kontynuować dokonywanie kolejnych operacji? Prosze odpowiedziec tak lub nie: ")
            if x == "tak":
                is_kontynuacja = True
            else:
                exit("Dziękujemy za skorzystanie z naszych usług.")
    elif operacja=="wypłata":
        spr_pin = input("Zanim operacja zostanie dokonana proszę potwierdzić ją numerem PIN: ")
        if spr_pin != pin:
            exit("Zły PIN, proszę skorzystać ponownie z maszyny. ")
        else:
            kwota_wypłaty = float(input("Proszę podać kwotę do wypłacenia: "))
        if kwota_wypłaty>saldo:
            exit("Niestety kwota wypłaty jest za duża, nie możemy wykonać tej operacji. Wszystkie wcześniejsze operacje zostały cofnięte, a wpłacone pieniążki zwrócone do Państwa. ")
        else:
            saldo= saldo - kwota_wypłaty
            y=input("Czy chce Pan/Pani kontynuować dokonywanie następnych operacji? Prosze odpowiedziec tak lub nie: ")
        if y == "tak":
            is_kontynuacja = True
        else:
            exit("Dziękujemy za skorzystanie z naszych usług.")
    elif operacja == "sprawdzić saldo":
        spr_pin = input("Zanim operacja zostanie dokonana proszę potwierdzić ją numerem PIN: ")
        if spr_pin != pin:
            exit("Zły PIN, proszę skorzystać ponownie z maszyny. ")
        else:
            print("Pana/Pani saldo to: "+str(saldo))
            z=input("Czy chce Pan/Pani kontynuować dokonywanie kolejnych operacji? Prosze odpowiedziec tak lub nie: ")
        if z == "tak":
            is_kontynuacja = True
        else:
            exit("Dziękujemy za skorzystanie z naszych usług.")
    else:
        exit("Źle wprowadzono nazwę operacji. Proszę ponownie włozyć kartę do maszyny. ")




