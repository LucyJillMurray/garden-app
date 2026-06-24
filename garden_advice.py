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


def get_user_input():
    """Ask the user for a season and plant type."""
    season = input("Enter a season: ")
    plant_type = input("Enter a plant: ")
    return season, plant_type


def get_season_advice(season):
    """Look up advice for the given season, with a fallback message."""
    return season_advice.get(season, "No advice for this season.")


def get_plant_advice(plant_type):
    """Look up advice for the given plant type, with a fallback message."""
    return plant_advice.get(plant_type, "No advice for this type of plant.")


def get_plant_recommendations(season):
    """Return a recommendation string for the given season, or an empty string if none exist."""
    recommended = season_plants.get(season)
    if recommended:
        return f"\nRecommended plants for {season}: {', '.join(recommended)}."
    return ""


def build_advice(season, plant_type):
    """Combine season advice, plant advice, and recommendations into one string."""
    advice = f"{get_season_advice(season)}\n{get_plant_advice(plant_type)}"
    advice += get_plant_recommendations(season)
    return advice


def main():
    """Run the gardening advice program."""
    season, plant_type = get_user_input()
    advice = build_advice(season, plant_type)
    print(advice)


if __name__ == "__main__":
    main()