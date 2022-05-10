def get_number_card(uid_wallet):
    card_number = list()
    card = list()
    number = ''.join(ch for ch in uid_wallet if ch.isnumeric())
    i = 0
    for el in number:
        card.append(el)
        i += 1
        if len(card) == 4:
            text = "".join(card)
            card = list()
            card_number.append(text)        
    
    card_number = " ".join(card_number)
    return card_number