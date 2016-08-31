COLOUR_DICT = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
"AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378", "aquamarine1": "#7fffd4",
"aquamarine2": "#76eec6", "aquamarine4": "#458b74", "azure1": "#f0ffff"}

# for colour,code in COLOUR_DICT.items():
#     print("{:25s} - {}".format(colour, code))

colour = input("Enter Colour Name: ")
print(COLOUR_DICT.get(colour))
