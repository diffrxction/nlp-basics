import dateparser.search

text = "The meeting will be held next Tuesday at 10am."
date = dateparser.search.search_dates(text)
print(date)