from pyscript import display
#restaurant order system (Python data types)

#STring
store_name = "The_Hangar"
owner_name = "Ethan Francia"

#Integer
year_since = 2025

#float 
tax_rate = 0.05

#Boolean
has_delivery = True
is_dine_in = True
is_takeaway = False

#List
product_names = ["86 -Eighty Six- HG Model Kit: Reginleif (Shin Custom) 1/48 Scale" , "Code Geass Lelouch of the Rebellion: Lancelot (Royal Coating Ver.) 1/35 Scale Model Kit" , "30MM Armored Core VI Fires of Rubicon Model Kit: Orbiter Nightfall", "Gundam MG Model Kit: Force Impulse Gundam", "Gundam MG Model Kit: Sword Impulse Gundam"]

#Tuples
business_hours = ("10:00 AM" , "8:00 PM")

#Dictionary
items = {
    "86 -Eighty Six- HG Model Kit: Reginleif (Shin Custom) 1/48 Scale" : 1800.00,
    "Code Geass Lelouch of the Rebellion: Lancelot (Royal Coating Ver.) 1/35 Scale Model Kit" : 2200.00,
    "30MM Armored Core VI Fires of Rubicon Model Kit: Orbiter Nightfall" : 2980.00,
    "Gundam MG Model Kit: Force Impulse Gundam" : 2835.00,
    "Gundam MG Model Kit: Sword Impulse Gundam" : 2655.00
}

#Set 
choking_hazards = {"plastic", "screws"}

#Display restaurant information
display(store_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since: {year_since}", target="since")
display(f"Items Pricelist", target="heading1")

#Display items 
display(product_names[0], target="prod1")
display(f"₱{items[ '86 -Eighty Six- HG Model Kit: Reginleif (Shin Custom) 1/48 Scale']:.2f}", target="price1")
display(product_names[1], target="prod2")
display(f"₱{items[ 'Code Geass Lelouch of the Rebellion: Lancelot (Royal Coating Ver.) 1/35 Scale Model Kit']:.2f}", target="price2")
display(product_names[2], target="prod3")
display(f"₱{items[ '30MM Armored Core VI Fires of Rubicon Model Kit: Orbiter Nightfall']:.2f}", target="price3")
display(product_names[3], target="prod4")
display(f"₱{items[ 'Gundam MG Model Kit: Force Impulse Gundam']:.2f}", target="price4")
display(product_names[4], target="prod5")
display(f"₱{items[ 'Gundam MG Model Kit: Sword Impulse Gundam']:.2f}", target="price5")



#Display additional information
display(f"Open : {business_hours[0]} - {business_hours[1]}" , target="openingHours")

#Display order type
display(f"In-store Purchases Available", target="orderType")