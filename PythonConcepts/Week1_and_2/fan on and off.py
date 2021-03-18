def fan():
    fan_status = "off"
    while True:
        command = input("enter a command (on,off, or quit)")
        command = command.lower()
        if command == "on":
            if fan_status == "on":
                print("fan already on")
            else:
                print("fan turned on")
                fan_status = "on"
        elif command == "off":
            if fan_status == "off":
                print("fan already off")
            else:
                print("fan turned off")
                fan_status = "off"
        elif command == "quit":
            break
        else:
            print("invalid syntax")


print(fan())
