import random

quotes = {"author": ["To thine own self be true.--Shakespeare", "To a great mind nothing is little.--Sherlock Homes", "Books are uniquely portable magic.--Steven King",
                     "We rise by lifting others.--Robert Ingersoll", "Our lives are defined by opportunities, even the ones we miss. --F. Scott Fitzgerald."],
          "musician": ["Music is like a dream. One that I cannot hear.―  Ludwig van Beethoven", "Musicians want to be the loud voices for so many quiet hears--Billy Joel",
                       "The older I get, the more I think birds are the best musicians on the planet--Brian Reitzell",
                       "I think musicians are always very generous promoting anything good they hear. Emmylou Harris",
                       "I see all the musicians in Blur with equal standing, really--Bernard Sumner"],
          "entrepreneur": ["All our dreams can come true, if we have the courage to pursue them.--Walt Disney", "Tough times never last, but tough people do.-- Robert Schuller",
                           "Remember why you started--unknown", "The way to get started is to quit talking and begin doing.--Walt Disney",
                           "The success of a company is always about the team.--Sassa Akervall"]
          }

user_input = None
while user_input != "q":
    user_input = input("Would you like a quote from an author, musician, or entrepreneur? Press q to quit.")
    if user_input in quotes:
        print(quotes[user_input][random.randint(0, 4)])
    else:
        print("invalid option try again")