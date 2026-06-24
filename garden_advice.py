# Dictionary holding gardening advice for each season
season_advice = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers.",
    "spring": "Watch for new growth and start planting seedlings.",
    "autumn": "Clear fallen leaves and prepare beds for winter."
}

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

season_plants = {
    "summer": ["tomatoes", "sunflowers", "peppers"],
    "winter": ["kale", "garlic", "broad beans"],
    "spring": ["lettuce", "carrots", "daffodils"],
    "autumn": ["pumpkins", "Brussels sprouts", "chrysanthemums"]
}


def get_user_input():
    season = input("Enter a season: ")
    plant_type = input("Enter a plant: ")
    return season, plant_type


def get_season_advice(season):
    return season_advice.get(season, "No advice for this season.")


def get_plant_advice(plant_type):
    return plant_advice.get(plant_type, "No advice for this type of plant.")


def get_plant_recommendations(season):
    recommended = season_plants.get(season)
    if recommended:
        return f"\nRecommended plants for {season}: {', '.join(recommended)}."
    return ""


def build_advice(season, plant_type):
    advice = f"{get_season_advice(season)}\n{get_plant_advice(plant_type)}"
    advice += get_plant_recommendations(season)
    return advice


def main():
    season, plant_type = get_user_input()
    advice = build_advice(season, plant_type)
    print(advice)

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
