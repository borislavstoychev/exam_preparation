def stock_availability(main_list, command, *args):
    if command == "delivery":
        main_list += list(args)
    elif command == "sell":
        try:
            if args:
                number = int(args[0])
                main_list = main_list[number:]
            else:
                main_list = main_list[1:]
        except ValueError:
            for sub in args:
                while sub in main_list:
                    main_list.remove(sub)
    return main_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
