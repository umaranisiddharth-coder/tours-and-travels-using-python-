"""
Replace generic hotel names with real top Indian hotel names per city.
Run: py update_hotel_names.py
"""
from app import create_app, db
from app.models import Hotel

app = create_app()

# Real top hotel names for each city — 5 per city (5-star to 3-star)
CITY_HOTELS = {
    'Delhi': [
        ('The Taj Mahal Hotel New Delhi', 5, 4.9, 18000),
        ('The Imperial New Delhi', 5, 4.8, 15000),
        ('ITC Maurya New Delhi', 5, 4.8, 14000),
        ('The Leela Palace New Delhi', 4, 4.6, 8500),
        ('Radisson Blu Plaza Delhi', 3, 4.3, 4500),
    ],
    'Mumbai': [
        ('Taj Mahal Palace Mumbai', 5, 4.9, 22000),
        ('The Oberoi Mumbai', 5, 4.8, 20000),
        ('ITC Grand Central Mumbai', 5, 4.7, 16000),
        ('Trident Nariman Point', 4, 4.5, 9000),
        ('Hotel Marine Plaza Mumbai', 3, 4.2, 4200),
    ],
    'Bangalore': [
        ('The Leela Palace Bengaluru', 5, 4.9, 17000),
        ('ITC Windsor Bengaluru', 5, 4.8, 15000),
        ('Taj West End Bengaluru', 5, 4.7, 14000),
        ('Sheraton Grand Bengaluru', 4, 4.5, 8000),
        ('Lemon Tree Hotel Bengaluru', 3, 4.2, 3800),
    ],
    'Chennai': [
        ('ITC Grand Chola Chennai', 5, 4.9, 16000),
        ('Taj Coromandel Chennai', 5, 4.8, 14000),
        ('The Leela Palace Chennai', 5, 4.7, 13000),
        ('Radisson Blu Chennai', 4, 4.4, 7500),
        ('Hotel Savera Chennai', 3, 4.1, 3500),
    ],
    'Hyderabad': [
        ('Taj Falaknuma Palace', 5, 4.9, 25000),
        ('ITC Kohenur Hyderabad', 5, 4.8, 16000),
        ('The Westin Hyderabad', 5, 4.7, 14000),
        ('Novotel Hyderabad Convention', 4, 4.4, 7000),
        ('Lemon Tree Premier Hyderabad', 3, 4.2, 3800),
    ],
    'Pune': [
        ('JW Marriott Pune', 5, 4.8, 14000),
        ('Conrad Pune', 5, 4.7, 13000),
        ('The Westin Pune Koregaon Park', 5, 4.6, 12000),
        ('Novotel Pune Nagar Road', 4, 4.3, 6500),
        ('Lemon Tree Hotel Pune', 3, 4.1, 3500),
    ],
    'Jaipur': [
        ('Rambagh Palace Jaipur', 5, 4.9, 30000),
        ('Taj Jai Mahal Palace', 5, 4.8, 22000),
        ('ITC Rajputana Jaipur', 5, 4.7, 14000),
        ('Fairmont Jaipur', 4, 4.5, 9000),
        ('Hotel Pearl Palace Jaipur', 3, 4.3, 2500),
    ],
    'Kolkata': [
        ('The Oberoi Grand Kolkata', 5, 4.9, 16000),
        ('ITC Royal Bengal Kolkata', 5, 4.8, 15000),
        ('Taj Bengal Kolkata', 5, 4.7, 14000),
        ('Hyatt Regency Kolkata', 4, 4.4, 7500),
        ('Hotel Hindustan International', 3, 4.1, 3500),
    ],
    'Ahmedabad': [
        ('Hyatt Regency Ahmedabad', 5, 4.7, 10000),
        ('Novotel Ahmedabad', 5, 4.6, 9000),
        ('Courtyard by Marriott Ahmedabad', 4, 4.4, 6500),
        ('Lemon Tree Hotel Ahmedabad', 3, 4.2, 3200),
        ('Hotel Cama Ahmedabad', 3, 4.0, 2800),
    ],
    'Surat': [
        ('Lords Plaza Surat', 5, 4.6, 8000),
        ('Courtyard by Marriott Surat', 4, 4.5, 7000),
        ('Novotel Surat', 4, 4.4, 6500),
        ('Lemon Tree Hotel Surat', 3, 4.2, 3500),
        ('Hotel Ginger Surat', 3, 4.0, 2500),
    ],
    'Lucknow': [
        ('Taj Mahal Lucknow', 5, 4.8, 12000),
        ('Hyatt Regency Lucknow', 5, 4.7, 11000),
        ('Vivanta Lucknow', 4, 4.5, 7500),
        ('Radisson Hotel Lucknow', 4, 4.3, 6000),
        ('Lemon Tree Hotel Lucknow', 3, 4.1, 3200),
    ],
    'Nagpur': [
        ('Radisson Blu Nagpur', 5, 4.7, 9000),
        ('Le Meridien Nagpur', 5, 4.6, 8500),
        ('Tuli Imperial Nagpur', 4, 4.4, 6000),
        ('Hotel Centre Point Nagpur', 3, 4.2, 3500),
        ('Lemon Tree Hotel Nagpur', 3, 4.0, 3000),
    ],
    'Indore': [
        ('Marriott Indore', 5, 4.7, 9000),
        ('Radisson Blu Indore', 5, 4.6, 8500),
        ('Sayaji Hotel Indore', 4, 4.4, 6000),
        ('Lemon Tree Hotel Indore', 3, 4.2, 3200),
        ('Hotel Shreemaya Indore', 3, 4.0, 2800),
    ],
    'Bhopal': [
        ('Jehan Numa Palace Bhopal', 5, 4.8, 10000),
        ('Courtyard by Marriott Bhopal', 4, 4.5, 7000),
        ('Radisson Blu Bhopal', 4, 4.4, 6500),
        ('Hotel Palash Residency Bhopal', 3, 4.2, 3500),
        ('Lemon Tree Hotel Bhopal', 3, 4.0, 3000),
    ],
    'Patna': [
        ('Maurya Hotel Patna', 5, 4.7, 8000),
        ('Hotel Chanakya Patna', 4, 4.4, 5500),
        ('Lemon Tree Hotel Patna', 4, 4.3, 5000),
        ('Hotel Patliputra Ashok', 3, 4.1, 3200),
        ('Hotel Gargee Grand Patna', 3, 3.9, 2500),
    ],
    'Kochi': [
        ('Taj Malabar Resort Kochi', 5, 4.9, 16000),
        ('The Brunton Boatyard Kochi', 5, 4.8, 14000),
        ('Vivanta Kochi', 4, 4.5, 8000),
        ('Radisson Blu Kochi', 4, 4.4, 7000),
        ('Hotel Casino Kochi', 3, 4.2, 3500),
    ],
    'Goa': [
        ('Taj Exotica Resort Goa', 5, 4.9, 25000),
        ('The Leela Goa', 5, 4.8, 22000),
        ('Grand Hyatt Goa', 5, 4.7, 18000),
        ('Novotel Goa Dona Sylvia', 4, 4.4, 8000),
        ('Hotel Baga Marina Goa', 3, 4.2, 3500),
    ],
    'Amritsar': [
        ('Taj Swarna Amritsar', 5, 4.8, 12000),
        ('Hyatt Amritsar', 5, 4.7, 11000),
        ('Radisson Blu Amritsar', 4, 4.5, 7000),
        ('Hotel Mohan International', 3, 4.2, 3500),
        ('Lemon Tree Hotel Amritsar', 3, 4.0, 3000),
    ],
    'Varanasi': [
        ('Taj Ganges Varanasi', 5, 4.8, 14000),
        ('Ramada Plaza Varanasi', 5, 4.6, 10000),
        ('Radisson Hotel Varanasi', 4, 4.4, 7000),
        ('Hotel Surya Varanasi', 3, 4.2, 3500),
        ('Lemon Tree Hotel Varanasi', 3, 4.0, 3000),
    ],
    'Agra': [
        ('The Oberoi Amarvilas Agra', 5, 4.9, 35000),
        ('Taj Hotel & Convention Agra', 5, 4.8, 18000),
        ('ITC Mughal Agra', 5, 4.7, 16000),
        ('Radisson Hotel Agra', 4, 4.4, 7000),
        ('Hotel Amar Agra', 3, 4.1, 3200),
    ],
    'Chandigarh': [
        ('Taj Chandigarh', 5, 4.8, 12000),
        ('Hyatt Regency Chandigarh', 5, 4.7, 11000),
        ('JW Marriott Chandigarh', 5, 4.6, 10000),
        ('Radisson Blu Chandigarh', 4, 4.4, 6500),
        ('Lemon Tree Hotel Chandigarh', 3, 4.1, 3200),
    ],
    'Udaipur': [
        ('Taj Lake Palace Udaipur', 5, 4.9, 40000),
        ('The Oberoi Udaivilas', 5, 4.9, 38000),
        ('Trident Udaipur', 5, 4.7, 14000),
        ('Radisson Blu Udaipur', 4, 4.4, 7500),
        ('Hotel Hilltop Palace Udaipur', 3, 4.2, 3500),
    ],
    'Jodhpur': [
        ('Umaid Bhawan Palace Jodhpur', 5, 4.9, 45000),
        ('Taj Hari Mahal Jodhpur', 5, 4.8, 18000),
        ('Vivanta Jodhpur', 4, 4.5, 9000),
        ('Radisson Jodhpur', 4, 4.3, 6500),
        ('Hotel Haveli Inn Jodhpur', 3, 4.1, 3000),
    ],
    'Shimla': [
        ('Wildflower Hall Shimla', 5, 4.9, 20000),
        ('The Oberoi Cecil Shimla', 5, 4.8, 18000),
        ('Radisson Hotel Shimla', 4, 4.5, 8000),
        ('Hotel Combermere Shimla', 3, 4.2, 4000),
        ('Lemon Tree Hotel Shimla', 3, 4.0, 3500),
    ],
    'Manali': [
        ('Span Resort & Spa Manali', 5, 4.8, 15000),
        ('The Himalayan Manali', 5, 4.7, 12000),
        ('Solang Valley Resort', 4, 4.5, 8000),
        ('Hotel Rohtang Manali', 3, 4.2, 4000),
        ('Lemon Tree Hotel Manali', 3, 4.0, 3500),
    ],
    'Rishikesh': [
        ('Ananda in the Himalayas', 5, 4.9, 30000),
        ('Taj Rishikesh Resort & Spa', 5, 4.8, 20000),
        ('Radisson Blu Rishikesh', 4, 4.5, 8000),
        ('Hotel Ganga Kinare Rishikesh', 3, 4.3, 4000),
        ('Lemon Tree Hotel Rishikesh', 3, 4.0, 3200),
    ],
    'Mysore': [
        ('Radisson Blu Plaza Hotel Mysore', 5, 4.7, 10000),
        ('The Windflower Resort Mysore', 5, 4.6, 9000),
        ('Lalitha Mahal Palace Hotel', 4, 4.5, 8000),
        ('Hotel Metropole Mysore', 3, 4.2, 4000),
        ('Lemon Tree Hotel Mysore', 3, 4.0, 3200),
    ],
    'Coimbatore': [
        ('Vivanta Coimbatore', 5, 4.7, 9000),
        ('Radisson Blu Coimbatore', 5, 4.6, 8500),
        ('Hotel Residency Coimbatore', 4, 4.4, 5500),
        ('Lemon Tree Hotel Coimbatore', 3, 4.2, 3200),
        ('Hotel Sri Devi Coimbatore', 3, 4.0, 2500),
    ],
    'Visakhapatnam': [
        ('Novotel Visakhapatnam', 5, 4.7, 9000),
        ('The Park Visakhapatnam', 5, 4.6, 8500),
        ('Radisson Blu Visakhapatnam', 4, 4.4, 6500),
        ('Hotel Daspalla Visakhapatnam', 3, 4.2, 3500),
        ('Lemon Tree Hotel Vizag', 3, 4.0, 3000),
    ],
    'Bhubaneswar': [
        ('Mayfair Lagoon Bhubaneswar', 5, 4.7, 9000),
        ('Trident Bhubaneswar', 5, 4.6, 8500),
        ('Radisson Blu Bhubaneswar', 4, 4.4, 6500),
        ('Hotel Swosti Premium', 3, 4.2, 3500),
        ('Lemon Tree Hotel Bhubaneswar', 3, 4.0, 3000),
    ],
}

# Generic names for cities not in the list above
GENERIC_NAMES = [
    ('{city} Grand Residency', 5, 4.7, 9000),
    ('{city} Business Inn', 4, 4.4, 5500),
    ('{city} Heritage Hotel', 4, 4.3, 5000),
    ('{city} Comfort Suites', 3, 4.1, 3000),
    ('{city} Budget Inn', 3, 3.9, 2000),
]

with app.app_context():
    updated = 0

    # Get all cities
    cities = db.session.query(Hotel.city).distinct().order_by(Hotel.city).all()
    cities = [c[0] for c in cities]

    for city in cities:
        city_hotels = Hotel.query.filter_by(city=city).order_by(Hotel.star_rating.desc(), Hotel.id).all()
        real_names = CITY_HOTELS.get(city)

        for i, hotel in enumerate(city_hotels):
            if real_names and i < len(real_names):
                name, stars, rating, price = real_names[i]
                hotel.hotel_name = name
                hotel.star_rating = stars
                hotel.rating = rating
                hotel.min_price = price
            else:
                # Use generic but city-specific name
                tpl = GENERIC_NAMES[i % len(GENERIC_NAMES)]
                hotel.hotel_name = tpl[0].format(city=city)
                hotel.star_rating = tpl[1]
                hotel.rating = tpl[2]
                hotel.min_price = tpl[3]
            updated += 1

    db.session.commit()
    print(f"✅ {updated} hotels renamed with real Indian hotel names.")
    print(f"   Cities with real names: {len(CITY_HOTELS)}")
    print(f"\nSample hotels:")
    for h in Hotel.query.filter(Hotel.city.in_(['Delhi','Mumbai','Jaipur','Goa'])).order_by(Hotel.city, Hotel.star_rating.desc()).limit(12).all():
        print(f"  {h.city:15} | {h.star_rating}★ | {h.hotel_name}")
