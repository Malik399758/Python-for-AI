# list


from tkinter import Image


image_features = [0.8, 0.6, 0.9, 0.7, 0.5]

# 1. Display complete list
print("Image Features:", image_features)

# 2. Access first feature
print("First Feature:", image_features[0])

# 3. Access last feature
print("Last Feature:", image_features[-1])

# 4. Add a new feature
image_features.append(0.95)
print("After Append:", image_features)

# 5. Insert a feature at index 1
image_features.insert(1, 0.75)
print("After Insert:", image_features)

# 6. Update a feature
image_features[0] = 0.85
print("After Update:", image_features)

# 7. Remove a feature by value
image_features.remove(0.7)
print("After Remove:", image_features)

# 8. Remove the last feature
removed = image_features.pop()
print("Removed Feature:", removed)
print("After Pop:", image_features)

# 9. Find number of features
print("Total Features:", len(image_features))

# 10. Find maximum and minimum
print("Maximum Feature:", max(image_features))
print("Minimum Feature:", min(image_features))

# 11. Calculate sum and average
print("Sum:", sum(image_features))
print("Average:", sum(image_features) / len(image_features))

# 12. Sort features
image_features.sort()
print("Ascending Order:", image_features)

# 13. Reverse the list
image_features.reverse()
print("Reversed List:", image_features)

# 14. Check whether a feature exists
print("Is 0.9 present?", 0.9 in image_features)


# Tuple

image_size = (224, 224)

print("Image Size:", image_size)
print("Width:", image_size[0])
print("Height:", image_size[1])



# Set

labels = {"Cat", "Dog", "Cat", "Bird", "Dog"}

print("Unique Labels:", labels)
print("Number of Unique Labels:", len(labels))



# Dictionary


image = {
    "name": "image1.jpg",
    "label": "Cat",
    "width": 224,
    "height": 224
}

# 1. Display complete dictionary
print("Complete Image:", image)

# 2. Access values
print("Image Name:", image["name"])
print("Image Label:", image["label"])
print("Image Width:", image["width"])
print("Image Height:", image["height"])

# 3. Add a new key-value pair
image["format"] = "JPEG"
print("After Adding Format:", image)

# 4. Update an existing value
image["label"] = "Dog"
print("After Updating Label:", image["label"])

# 5. Access a value safely using get()
print("Image Format:", image.get("format"))
print("Image Size:", image.get("size", "Not Available"))

# 6. Display all keys
print("Keys:", list(image.keys()))

# 7. Display all values
print("Values:", list(image.values()))

# 8. Display all key-value pairs
print("Items:", list(image.items()))

# 9. Check whether a key exists
print("Is label available?", "label" in image)

# 10. Remove a key-value pair
removed_value = image.pop("format")
print("Removed Format:", removed_value)

# 11. Count total key-value pairs
print("Total Properties:", len(image))

# 12. Display final dictionary
print("Final Image Record:", image)


# Functions


def calculate_average(features):
    average = sum(features) / len(features)
    return average

image_features = [0.8, 0.6, 0.9, 0.7, 0.5]

result = calculate_average(image_features)

print("Average Feature Value:", result)



 # Practical: Image Classification Data

 # AI image data
image = {
    "name": "cat.jpg",
    "size": (224, 224),
    "labels": {"cat", "animal", "cat"},
    "features": [120, 150, 180]
}

# Function
def calculate_average(features):
    return sum(features) / len(features)

average = calculate_average(image["features"])

print("Image:", image["name"])
print("Size:", image["size"])
print("Labels:", image["labels"])
print("Average Feature:", average)