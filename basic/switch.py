koszyk = str(input("Co chciał*byś kupić?: "))

match koszyk:
    case "chleb":
        print("chlebik z masłem? 😏")
    case "wode":
        print("dzisiejsza pogoda jest 🥵")
    case "ser":
        print("syr")
    case _:
	    print("🤖💥🤖\terror 404\t🤖💥🤖\n\tfood not found")