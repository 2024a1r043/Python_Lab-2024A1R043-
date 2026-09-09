#Write a python program to detect whether a comment is spam or not. A comment should be treated as spam if it contains any of these keywords: "make a lot of money","but now", "subscribe this",or"click this".,
comment = input("Enter a comment: ").lower()
spam_keywords = ["make a lot of money", "but now", "subscribe this", "click this"]
if any(keyword in comment for keyword in spam_keywords):
    print("This comment is spam.")
else:
    print("This comment is not spam.")