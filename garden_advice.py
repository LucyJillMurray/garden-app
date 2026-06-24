# Dictionary holding gardening advice for each season
season_advice = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers.",
    "spring": "Watch for new growth and start planting seedlings.",
    "autumn": "Clear fallen leaves and prepare beds for winter."
}

# Dictionary holding gardening advice for each plant type
plant_advice = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
    "herb": "Trim regularly to encourage bushy growth."
}
# Dictionary holding recommended plants for each season
season_plants = {
    "summer": ["tomatoes", "sunflowers", "peppers"],
    "winter": ["kale", "garlic", "broad beans"],
    "spring": ["lettuce", "carrots", "daffodils"],
    "autumn": ["pumpkins", "Brussels sprouts", "chrysanthemums"]
}

# Get user input
season = input("Enter a season: ")
plant_type = input("Enter a plant: ")


# Look up advice, with a fallback message if not found
season_message = season_advice.get(season, "No advice for this season.")
plant_message = plant_advice.get(plant_type, "No advice for this type of plant.")

# Combine and print the generated advice
advice = f"{season_message}\n{plant_message}"

# Look up recommended plants for the season, if any exist
recommended = season_plants.get(season)
if recommended:
    advice += f"\nRecommended plants for {season}: {', '.join(recommended)}."

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity
# - Recommend plants based on the entered season.
