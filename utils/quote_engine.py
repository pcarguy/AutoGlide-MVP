import googlemaps
import os

def calculate_quote(pickup_zip, delivery_zip, vehicle_type, transport_type):
    base_rate = 300
    rate_per_mile = 1.2  # Default per-mile base rate

    # Apply transport type multipliers
    multiplier = {
        "Open": 1.0,
        "Enclosed": 1.3,
        "Inoperable": 1.5,
        "Expedited": 1.6
    }.get(transport_type, 1.0)

    # Connect to Google Maps API
    api_key = os.getenv("API_KEY") or os.getenv("GOOGLE_MAPS_API_KEY")
    gmaps = googlemaps.Client(key=api_key)

    try:
        result = gmaps.distance_matrix(pickup_zip, delivery_zip, mode="driving")
        distance = result["rows"][0]["elements"][0]["distance"]["value"] / 1609.34  # meters to miles
    except Exception:
        distance = 800  # fallback to average

    quote = base_rate + (distance * rate_per_mile * multiplier)
    return round(quote, 2)
