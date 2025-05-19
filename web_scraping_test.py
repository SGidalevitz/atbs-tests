import webbrowser
address = '123 Main Street, New York City, NY'

for i in range(1, 10):
    webbrowser.open('https://www.google.com/maps/place/' + str(i) + ' Main Street, New York City, NY')