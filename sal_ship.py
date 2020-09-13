def gnd_ship(pack_wht):
    if (pack_wht <= 2):
        price = 1.5 * pack_wht + 20
    elif (pack_wht > 2) and (pack_wht <=6):
        price = 3 * pack_wht + 20
    elif (pack_wht > 6) and (pack_wht <= 10):
        price = 4 * pack_wht + 20
    elif (pack_wht > 10):
        price = 4.75 * pack_wht + 20
    price = round(price,2)
    return price

def drone_ship(pack_wht):
    if (pack_wht <= 2):
        price = 4.5 * pack_wht
    elif (pack_wht > 2) and (pack_wht <=6):
        price = 9 * pack_wht
    elif (pack_wht > 6) and (pack_wht <= 10):
        price = 12 * pack_wht
    elif (pack_wht > 10):
        price = 14.25 * pack_lbs
    price = round(price, 2)
    return price

def gnd_ship_prem(pack_wht):
    price = 125
    return price

pack_lbs = float(input("Package weight?"))

gnd_price = gnd_ship(pack_lbs)
drone_price = drone_ship(pack_lbs)
prem_price = gnd_ship_prem(pack_lbs)

print("Ground Shipping price is: $" + str(gnd_price))
print("Drone Shipping price is $" + str(drone_price))
print("Premium Ground Shipping price is $" + str(prem_price))

def find_method(option1, option2, price):
    method = input("Which method you like to choose?" + " (" + option1.title() + "/ " + option2.title() + ")").lower()
    if method == option1:
        msg_2 = "You chose " + option1.title() + ". It will cost $" + str(price) + " to ship " + str(pack_lbs)+ " pounds."
    elif method == option2:
        msg_2 = "You chose " + option2.title() + ". It will cost $" + str(price) + " to ship " + str(pack_lbs)+ " pounds."
    else:
        print("Invalid Entry. Must enter either " + option1.title() + " or " + option2.title() + ". Try again.")
        msg_2 = find_method(option1, option2, price)
    return msg_2

def print_msg():
    if (gnd_price < drone_price) and (gnd_price < prem_price):
        msg = "Ground Shipping is the cheapest option. It will cost $" + str(gnd_price) + " to ship " + str(pack_lbs) + " pounds."
    elif (drone_price < gnd_price) and (drone_price < prem_price):
        msg = "Drone Shipping is the cheapest option. It will cost $" + str(drone_price) + " to ship " + str(pack_lbs) + " pounds."
    elif (prem_price < drone_price) and (prem_price < gnd_price):
        msg = "Premium Ground Shipping is the cheapest option. It will cost $" + str(prem_price) + " to ship " + str(pack_lbs) + " pounds."
    elif (prem_price == drone_price) or (prem_price == gnd_price):
        if drone_price < gnd_price:
            msg = "Premium Ground Shipping Price is the same as Drone Shipping Price"
            print(msg)
            msg_3 = find_method('premium ground', 'drone shipping',prem_price)
        elif gnd_price < drone_price:
            msg = "Premium Ground Shipping Price is the same as Ground Shipping Price."
            print(msg)
            msg_3 = find_method('premium ground shipping','ground shipping',prem_price)
        return msg_3
    elif (drone_price == prem_price) or (drone_price == gnd_price):
        if prem_price < gnd_price:
            msg = "Drone Shipping Price is the same as Premium Ground Shipping Price."
            print(msg)
            msg_3 = find_method('drone shipping','premium ground shipping',drone_price)
        elif gnd_price < prem_price:
            msg = "Drone Shipping Price is the same as Ground Shipping Price."
            print(msg)
            msg_3 = find_method('drone shipping','ground shipping',drone_price)
    elif (gnd_price == prem_price) or (gnd_price == drone_price):
        if prem_price < drone_price:
            msg = "Ground Shipping price is the same as Premium Ground Shipping Price"
            print(msg)
            msg_3 = find_method('ground shipping','premium ground shipping',gnd_price)
        elif drone_price < prem_price:
            msg = "Ground Shipping price is the same as Drone Shipping price."
            print(msg)
            msg_3 = find_method('ground shipping','drone shipping',gnd_price)
        return msg_3
    return msg

print(print_msg())
