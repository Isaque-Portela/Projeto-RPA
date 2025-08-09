

cnh = input("Do you have CNH? ")

speed = int(input("What's the speed? "))

def what_speed():
    if speed <= 90:
        print("At adequate apeed!")
    elif speed > 95:
        print("High Speed, fine applied")
    elif speed >110:
        print("Serious Infraction")

def have_drivers_license():
    if cnh == "yes" or cnh == "Yes" or cnh == "sim" or cnh == "Sim":
        print("Reguled situation")
    elif cnh == "No" or cnh == "no" or cnh == "Não" or cnh == "não":
        print("Serious Infraction")

what_speed() 
have_drivers_license()