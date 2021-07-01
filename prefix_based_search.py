business_names = ["burger king", "McDonald's", "super duper burger's", "subway", "pizza hut"]
search_term = "bur"
result = []
for business in business_names:
    if search_term in business:
        result.append(business)

result.sort()
print(result)