
print()
print("\t\t\t\t\t\tINSTAPY")
running = True

while running:
    response = input("(f)ilter an image or (q)uit \n")
    if response == "q" or response == "quit":
        running = False
    else:
        filePath = input("What's the full path to your image?\n")
        filter = input("Write a series of filters to apply:\n(p)ixelate\n(k)aleidoscope\n(g)ray-day\n(r)ighty\nExample: kpkr will run keleidoscope, pixelate, kaleidoscope and gray-day in sequence\n")
        if(filter == "k" or response == "kaleidoscope"):
            print()

print('Done')