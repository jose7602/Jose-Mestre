##Jose Mestre##

review_material = []

media_type = input ("What media type is it? ")

review_material.append(media_type)

genre = input ("What genre is it? ")

review_material.append(genre)

title = input ("What is the title? ")

review_material.append(title)

year = input ("What year was it created? ")

review_material.append(year)

description = input ("A short description of the media type? ")

review_material.append(description)

rating = float(input("On a scale of 1 to 10 what to you rate this media? "))
review_material.append(rating)

print (review_material)
