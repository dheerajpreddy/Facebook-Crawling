import facebook, json

graph = facebook.GraphAPI(access_token="EAAHH6Hycz8oBALZABeTlHcZBuPxM9kN7Dqc0hOZAtoP7aQgpmLjrrTvwgPRIZC7QWZBF8fZAUuodCnvLF5wptuRvap50srCK0JZCYIBEREMM192x9r2WeNqoxLhwMywqD5EI5I5juxjQssq29Gt7wIHTJmmf7DyHBieZCoTZCKVYrxXt2dGYi23hVTx70hTvSXKZAwwWOJibwTPQZDZD", version="2.12")

# 1040592242770263
# eFgen0aGTMnwnuBCHOm30ZXEi2Y

# reacts = graph.get_connections(id='2091410757591159_2071635996235302', connection_name='insights')
reacts = graph.request("/2091410757591159_1957383250993911?fields=reactions.type(LOVE).limit(0).summary(total_count).as(reactions_love),reactions.type(WOW).limit(0).summary(total_count).as(reactions_wow),reactions.type(HAHA).limit(0).summary(total_count).as(reactions_haha)")
# with open('reacts.json', 'w') as fp:
#     json.dump(reacts, fp)
print(reacts)


# 2092400917492143
