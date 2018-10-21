import facebook

graph = facebook.GraphAPI(access_token="EAAHH6Hycz8oBAKkt3beUksRbX5KjFhlQd10EzFtcE2rIXZBq77i8qTcIUNQ6mgdKqtZAyoM4w7xTj3O5jpvsn7SXZAcJkUvI3kEoMoZCYzXslZCQZAWsihfmEQDywO1N5ZBv6DHXMXdXuPggEUXQDVZBzAJJYQ1dSjCZAfZA3qMFVQtf6G1melcKYjHC4925uqClxaGS7gfKSYHQZDZD", version="2.12")

# 1040592242770263
# eFgen0aGTMnwnuBCHOm30ZXEi2Y

post = graph.get_connections(id='me', connection_name='friends')
print(post)
