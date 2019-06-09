import pickle

f1 = open("../data/user_review", "rb")
user_reviews = pickle.load(f1)

print(type(user_reviews))
print(len(user_reviews))
