"""
Auto-assign routes to buses that have none.
Assigns 2-4 routes per bus from a comprehensive city pair list.
Run: py auto_add_routes.py
"""
import random
from datetime import time
from app import create_app, db
from app.models import Bus, BusRoute

app = create_app()

# All major city pairs with realistic fares and durations
CITY_PAIRS = [
    # Maharashtra routes
    ("Mumbai",      "Pune",         180, "3h 00m",  "06:00", "09:00"),
    ("Mumbai",      "Nashik",       220, "4h 00m",  "07:00", "11:00"),
    ("Mumbai",      "Aurangabad",   350, "6h 30m",  "22:00", "04:30"),
    ("Mumbai",      "Nagpur",       650, "13h 00m", "18:00", "07:00"),
    ("Mumbai",      "Kolhapur",     400, "7h 30m",  "21:00", "04:30"),
    ("Mumbai",      "Solapur",      450, "8h 00m",  "20:00", "04:00"),
    ("Mumbai",      "Sangli",       380, "7h 00m",  "21:30", "04:30"),
    ("Mumbai",      "Miraj",        390, "7h 30m",  "21:00", "04:30"),
    ("Mumbai",      "Satara",       280, "5h 00m",  "07:00", "12:00"),
    ("Mumbai",      "Latur",        500, "9h 00m",  "20:00", "05:00"),
    ("Mumbai",      "Nanded",       550, "10h 00m", "19:00", "05:00"),
    ("Mumbai",      "Amravati",     600, "11h 00m", "18:00", "05:00"),
    ("Mumbai",      "Jalgaon",      350, "6h 30m",  "22:00", "04:30"),
    ("Mumbai",      "Dhule",        320, "6h 00m",  "22:00", "04:00"),
    ("Pune",        "Nashik",       200, "3h 30m",  "07:00", "10:30"),
    ("Pune",        "Aurangabad",   280, "5h 00m",  "07:00", "12:00"),
    ("Pune",        "Nagpur",       550, "11h 00m", "19:00", "06:00"),
    ("Pune",        "Kolhapur",     250, "4h 30m",  "07:00", "11:30"),
    ("Pune",        "Solapur",      280, "5h 00m",  "07:00", "12:00"),
    ("Pune",        "Sangli",       220, "4h 00m",  "08:00", "12:00"),
    ("Pune",        "Miraj",        230, "4h 30m",  "08:00", "12:30"),
    ("Pune",        "Satara",       150, "2h 30m",  "07:00", "09:30"),
    ("Pune",        "Latur",        380, "7h 00m",  "21:00", "04:00"),
    ("Pune",        "Nanded",       420, "8h 00m",  "20:00", "04:00"),
    ("Pune",        "Amravati",     480, "9h 00m",  "19:00", "04:00"),
    ("Pune",        "Goa",          450, "8h 30m",  "22:00", "06:30"),
    ("Nashik",      "Aurangabad",   200, "3h 30m",  "07:00", "10:30"),
    ("Nashik",      "Nagpur",       450, "9h 00m",  "20:00", "05:00"),
    ("Nashik",      "Pune",         200, "3h 30m",  "14:00", "17:30"),
    ("Nashik",      "Mumbai",       220, "4h 00m",  "14:00", "18:00"),
    ("Aurangabad",  "Nagpur",       380, "7h 00m",  "21:00", "04:00"),
    ("Aurangabad",  "Pune",         280, "5h 00m",  "14:00", "19:00"),
    ("Aurangabad",  "Mumbai",       350, "6h 30m",  "14:00", "20:30"),
    ("Kolhapur",    "Pune",         250, "4h 30m",  "14:00", "18:30"),
    ("Kolhapur",    "Mumbai",       400, "7h 30m",  "22:00", "05:30"),
    ("Kolhapur",    "Sangli",        80, "1h 30m",  "07:00", "08:30"),
    ("Kolhapur",    "Miraj",         90, "1h 45m",  "07:00", "08:45"),
    ("Kolhapur",    "Goa",          300, "5h 30m",  "07:00", "12:30"),
    ("Sangli",      "Pune",         220, "4h 00m",  "07:00", "11:00"),
    ("Sangli",      "Mumbai",       380, "7h 00m",  "22:00", "05:00"),
    ("Sangli",      "Kolhapur",      80, "1h 30m",  "14:00", "15:30"),
    ("Sangli",      "Miraj",         30, "0h 30m",  "07:00", "07:30"),
    ("Miraj",       "Pune",         230, "4h 30m",  "07:00", "11:30"),
    ("Miraj",       "Mumbai",       390, "7h 30m",  "22:00", "05:30"),
    ("Miraj",       "Kolhapur",      90, "1h 45m",  "14:00", "15:45"),
    ("Miraj",       "Sangli",        30, "0h 30m",  "14:00", "14:30"),
    ("Miraj",       "Solapur",      200, "3h 30m",  "07:00", "10:30"),
    ("Solapur",     "Pune",         280, "5h 00m",  "07:00", "12:00"),
    ("Solapur",     "Mumbai",       450, "8h 00m",  "22:00", "06:00"),
    ("Solapur",     "Hyderabad",    350, "6h 00m",  "07:00", "13:00"),
    ("Nagpur",      "Mumbai",       650, "13h 00m", "18:00", "07:00"),
    ("Nagpur",      "Pune",         550, "11h 00m", "18:00", "05:00"),
    ("Nagpur",      "Hyderabad",    500, "10h 00m", "19:00", "05:00"),
    ("Nagpur",      "Amravati",     150, "2h 30m",  "07:00", "09:30"),
    # Pan-India routes
    ("Mumbai",      "Bangalore",    900, "16h 00m", "17:00", "09:00"),
    ("Mumbai",      "Hyderabad",    750, "14h 00m", "18:00", "08:00"),
    ("Mumbai",      "Goa",          500, "9h 00m",  "22:00", "07:00"),
    ("Mumbai",      "Ahmedabad",    400, "7h 00m",  "22:00", "05:00"),
    ("Mumbai",      "Surat",        300, "5h 00m",  "07:00", "12:00"),
    ("Pune",        "Bangalore",    750, "14h 00m", "18:00", "08:00"),
    ("Pune",        "Hyderabad",    600, "11h 00m", "19:00", "06:00"),
    ("Pune",        "Chennai",      950, "18h 00m", "16:00", "10:00"),
    ("Bangalore",   "Hyderabad",    500, "9h 00m",  "22:00", "07:00"),
    ("Bangalore",   "Chennai",      350, "6h 00m",  "22:00", "04:00"),
    ("Bangalore",   "Goa",          550, "10h 00m", "21:00", "07:00"),
    ("Bangalore",   "Mumbai",       900, "16h 00m", "17:00", "09:00"),
    ("Hyderabad",   "Bangalore",    500, "9h 00m",  "22:00", "07:00"),
    ("Hyderabad",   "Chennai",      600, "11h 00m", "20:00", "07:00"),
    ("Hyderabad",   "Mumbai",       750, "14h 00m", "18:00", "08:00"),
    ("Hyderabad",   "Pune",         600, "11h 00m", "19:00", "06:00"),
    ("Chennai",     "Bangalore",    350, "6h 00m",  "22:00", "04:00"),
    ("Chennai",     "Hyderabad",    600, "11h 00m", "20:00", "07:00"),
    ("Delhi",       "Jaipur",       350, "5h 30m",  "07:00", "12:30"),
    ("Delhi",       "Agra",         250, "4h 00m",  "07:00", "11:00"),
    ("Delhi",       "Chandigarh",   300, "4h 30m",  "07:00", "11:30"),
    ("Delhi",       "Lucknow",      500, "8h 00m",  "22:00", "06:00"),
    ("Delhi",       "Amritsar",     450, "7h 00m",  "22:00", "05:00"),
    ("Jaipur",      "Delhi",        350, "5h 30m",  "14:00", "19:30"),
    ("Jaipur",      "Udaipur",      300, "5h 00m",  "07:00", "12:00"),
    ("Jaipur",      "Jodhpur",      280, "4h 30m",  "07:00", "11:30"),
    ("Ahmedabad",   "Mumbai",       400, "7h 00m",  "22:00", "05:00"),
    ("Ahmedabad",   "Surat",        200, "3h 30m",  "07:00", "10:30"),
    ("Ahmedabad",   "Pune",         500, "9h 00m",  "21:00", "06:00"),
    ("Goa",         "Mumbai",       500, "9h 00m",  "22:00", "07:00"),
    ("Goa",         "Pune",         450, "8h 30m",  "22:00", "06:30"),
    ("Goa",         "Bangalore",    550, "10h 00m", "21:00", "07:00"),
    ("Kolkata",     "Bhubaneswar",  400, "7h 00m",  "22:00", "05:00"),
    ("Kochi",       "Bangalore",    500, "9h 00m",  "22:00", "07:00"),
    ("Kochi",       "Chennai",      600, "11h 00m", "20:00", "07:00"),
    ("Indore",      "Bhopal",       200, "3h 30m",  "07:00", "10:30"),
    ("Indore",      "Mumbai",       550, "10h 00m", "20:00", "06:00"),
    ("Bhopal",      "Indore",       200, "3h 30m",  "14:00", "17:30"),
    ("Lucknow",     "Delhi",        500, "8h 00m",  "22:00", "06:00"),
    ("Lucknow",     "Varanasi",     300, "5h 00m",  "07:00", "12:00"),
    ("Varanasi",    "Lucknow",      300, "5h 00m",  "14:00", "19:00"),
    ("Patna",       "Varanasi",     250, "4h 30m",  "07:00", "11:30"),
]

# Departure times pool
DEPARTURE_TIMES = [
    "05:30", "06:00", "06:30", "07:00", "07:30", "08:00",
    "09:00", "10:00", "11:00", "12:00", "13:00", "14:00",
    "15:00", "16:00", "17:00", "18:00", "19:00", "20:00",
    "21:00", "21:30", "22:00", "22:30", "23:00", "23:30",
]

def time_from_str(t):
    h, m = map(int, t.split(':'))
    return time(h, m)

def add_hours(t_str, duration_str):
    """Add duration to departure time to get arrival time."""
    h, m = map(int, t_str.split(':'))
    dh = int(duration_str.split('h')[0])
    dm_part = duration_str.split('h')[1].strip().replace('m', '').strip()
    dm = int(dm_part) if dm_part else 0
    total_min = h * 60 + m + dh * 60 + dm
    total_min = total_min % (24 * 60)
    return f"{total_min // 60:02d}:{total_min % 60:02d}"

with app.app_context():
    # Get buses with no routes
    buses_no_routes = [b for b in Bus.query.all() if len(b.routes) == 0]
    print(f"Buses with no routes: {len(buses_no_routes)}")

    added = 0
    for bus in buses_no_routes:
        # Pick 2-3 random city pairs for this bus
        num_routes = random.randint(2, 3)
        chosen = random.sample(CITY_PAIRS, min(num_routes, len(CITY_PAIRS)))

        for from_city, to_city, base_fare, duration, dep_default, arr_default in chosen:
            # Vary departure time slightly
            dep = random.choice(DEPARTURE_TIMES)
            arr = add_hours(dep, duration)

            # Vary fare ±10%
            fare = round(base_fare * random.uniform(0.9, 1.1), 0)

            # Boarding/dropping points
            boarding = f"{from_city} Bus Stand, {from_city} Railway Station"
            dropping = f"{to_city} Bus Stand, {to_city} Railway Station"

            route = BusRoute(
                bus_id=bus.id,
                from_city=from_city,
                to_city=to_city,
                departure_time=time_from_str(dep),
                arrival_time=time_from_str(arr),
                duration=duration,
                fare=fare,
                frequency="Daily",
                boarding_points=boarding,
                dropping_points=dropping,
            )
            db.session.add(route)
            added += 1

        if added % 100 == 0:
            db.session.commit()
            print(f"  Committed {added} routes so far...")

    db.session.commit()
    print(f"\n✅ Added {added} routes to {len(buses_no_routes)} buses")

    # Final stats
    from sqlalchemy import func
    total = db.session.query(func.count(BusRoute.id)).scalar()
    print(f"✅ Total routes in DB: {total}")
