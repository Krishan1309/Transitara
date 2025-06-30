
from attractions import get_top_attractions
from planner import generate_itinerary
from export import save_to_csv, save_trip_plan

def get_ai_trip_plan(destination, days_str):
    """
    Generates a trip plan for the web application.
    Takes destination and days as strings from the web form.
    Returns the itinerary as a string.
    """
    try:
        days = int(days_str)
    except ValueError:
        return "Error: Number of days must be a valid integer."

    if not destination or days <= 0:
        return "Error: Please provide a valid destination and positive number of days."

    # Fetch attractions (using your existing attractions.py)
    attractions = get_top_attractions(destination)
    if not attractions:
        return f"Could not find top attractions for {destination}. Please try another destination or refine your query."

    # You can format attractions for display if needed
    attractions_list_str = "\nTop Attractions:\n"
    for i, attr in enumerate(attractions, 1):
        attractions_list_str += f"{i}. {attr['name']} - {attr['description']}\n"

    # Generate itinerary (using your existing planner.py)
    itinerary = generate_itinerary(destination, days, attractions)

    # Combine results for display on the web
    full_plan_output = f"🌟 AI Trip Plan for {destination} ({days} days) 🌟\n\n"
    full_plan_output += attractions_list_str
    full_plan_output += "\n\n✈️ Your Detailed Itinerary:\n"
    full_plan_output += itinerary

    

    return full_plan_output