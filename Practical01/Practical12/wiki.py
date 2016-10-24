"""
Practical 12

API - wikipedia
"""

import wikipedia

phrase = input("Enter in a search phrase (leave blank to quit): ")

while len(phrase) > 0:
    print("Searching Wikipedia. Please wait...")
    try:
        search_results = wikipedia.summary(phrase)
        print("Summary:\n{}".format(search_results))
        print("Searching Wikipedia for more Deatils.  Please wait...")
        page = wikipedia.page(phrase)
        print("\nTitle:\n{}".format(page.title))
        print("Summary:\n{}".format(page.summary))
        print("URL:\n{}".format(page.url))
    except wikipedia.exceptions.DisambiguationError as wiki_error:
        print("Disambiguation Error.  Please be more concise. Suggestions:")
        for topic in wiki_error.options:  # I wish I could use list comprehension ...
            print(topic)
        print("Please be more specific....")
    phrase = input("Enter in a search phrase (leave blank to quit): ")


