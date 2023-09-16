print("Welcome to Saamiya's Store!\n")
name = input("What is your name? ")
print(f'Hi! {name} its nice to meet you\n')
age = input("\nHow old are you? ")

def user_input():
  print("\nType the issue that you need assistance from out of the below choices ")
  print("\nStore Hours - Store Hours\n")
  print("Our Locations - Locations\n")
  print("Products that are available - Product Availability\n")
  print("Prices of our products - Prices\n")
  user_choice = input("Type which service you would like to know about\n ")
  if user_choice == "Prices" or user_choice == "prices":
    print("\nShirt - $12.99, Jeans - $45.99, Shorts - $15.99, T-Shirts - $10.75")
    choice_again = input("Would you like to see the choices again? ")
    if choice_again == "yes" or choice_again == "Yes":
      user_input()
    else:
      print("Goodbye")
  elif user_choice == "Locations" or user_choice == "locations":
    print("\nNorth Austin, Texas, Cedar Park, Texas, and Round Rock, Texas")
    choice_again = input("Would you like to see the choices again? ")
    if choice_again == "yes" or choice_again == "Yes":
      user_input()
    else:
      print("Goodbye")
  elif user_choice == "product availability" or user_choice == "Product Availability":
    print("\nShirts - 15 left, Jeans - 50 left, Shorts - 13 left, T-Shirts - 34 left")
    choice_again = input("Would you like to see the choices again? ")
    if choice_again == "yes" or choice_again == "Yes":
      user_input()
    else:
      print("Goodbye")
  else:
    print("\nSaturday	9 AM–9 PM")
    print("Sunday	   9 AM–8 PM")
    print("Monday	   9 AM–9 PM")
    print("Tuesday	 9 AM–9 PM")
    print("Wednesday 9 AM–9 PM")
    print("Thursday	 9 AM–9 PM")
    print("Friday	   9 AM–9 PM")
    choice_again = input("\nWould you like to see the choices again? ")
    if choice_again == "yes" or choice_again == "Yes":
      user_input()
    else:
      print("Goodbye")
user_input()
