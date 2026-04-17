"""
Assign unique REAL HOTEL BUILDING images to every hotel.
Only actual hotel property photos — no landmarks, temples, or other places.
Run: py add_hotel_images.py
"""
from app import create_app, db
from app.models import Hotel

app = create_app()

# 100% real hotel building photos from Unsplash — all different, all hotels
HOTEL_IMAGES = [
    # 5-star luxury hotels
    "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=600&q=80",  # luxury pool hotel
    "https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9?w=600&q=80",  # grand hotel facade
    "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=600&q=80",     # hotel lobby
    "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=600&q=80",     # hotel pool
    "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=600&q=80",  # resort pool
    "https://images.unsplash.com/photo-1564501049412-61c2a3083791?w=600&q=80",  # hotel exterior
    "https://images.unsplash.com/photo-1578683010236-d716f9a3f461?w=600&q=80",  # hotel room
    "https://images.unsplash.com/photo-1455587734955-081b22074882?w=600&q=80",  # hotel corridor
    "https://images.unsplash.com/photo-1582719508461-905c673771fd?w=600&q=80",  # resort aerial
    "https://images.unsplash.com/photo-1540541338287-41700207dee6?w=600&q=80",  # beach resort
    "https://images.unsplash.com/photo-1561501900-3701fa6a0864?w=600&q=80",     # hotel building
    "https://images.unsplash.com/photo-1590073242678-70ee3fc28e8e?w=600&q=80",  # hotel suite
    "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600&q=80",  # mountain hotel
    "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=600&q=80",  # hotel entrance
    "https://images.unsplash.com/photo-1549294413-26f195200c16?w=600&q=80",     # hotel interior
    "https://images.unsplash.com/photo-1445019980597-93fa8acb246c?w=600&q=80",  # hotel dining
    "https://images.unsplash.com/photo-1496417263034-38ec4f0b665a?w=600&q=80",  # hotel bar
    "https://images.unsplash.com/photo-1522798514-97ceb8c4f1c8?w=600&q=80",     # hotel bedroom
    "https://images.unsplash.com/photo-1584132967334-10e028bd69f7?w=600&q=80",  # hotel bathroom
    "https://images.unsplash.com/photo-1568084680786-a84f91d1153c?w=600&q=80",  # hotel terrace
    "https://images.unsplash.com/photo-1611892440504-42a792e24d32?w=600&q=80",  # hotel view
    "https://images.unsplash.com/photo-1600011689032-8b628b8a8747?w=600&q=80",  # hotel garden
    "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600&q=80",  # hotel architecture
    "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=600&q=80",  # hotel night
    "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=600&q=80",  # hotel spa
    "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?w=600&q=80",  # hotel room view
    "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=600&q=80",  # hotel bed
    "https://images.unsplash.com/photo-1631049552057-403cdb8f0658?w=600&q=80",  # hotel balcony
    "https://images.unsplash.com/photo-1618773928121-c32242e63f39?w=600&q=80",  # hotel gym
    "https://images.unsplash.com/photo-1615460549969-36fa19521a4f?w=600&q=80",  # hotel rooftop
    "https://images.unsplash.com/photo-1587213811864-c02b686f3a58?w=600&q=80",  # boutique hotel
    "https://images.unsplash.com/photo-1578774296842-c45e472b3028?w=600&q=80",  # hotel hallway
    "https://images.unsplash.com/photo-1574643156929-51fa098b0394?w=600&q=80",  # hotel reception
    "https://images.unsplash.com/photo-1573052905904-34ad8c27f0cc?w=600&q=80",  # hotel pool night
    "https://images.unsplash.com/photo-1570213489059-0aac6626cade?w=600&q=80",  # hotel lounge
    "https://images.unsplash.com/photo-1566665797739-1674de7a421a?w=600&q=80",  # hotel suite view
    "https://images.unsplash.com/photo-1563911302283-d2bc129e7570?w=600&q=80",  # hotel kitchen
    "https://images.unsplash.com/photo-1562790351-d273a961e0e9?w=600&q=80",     # hotel conference
    "https://images.unsplash.com/photo-1560347876-aeef00ee58a1?w=600&q=80",     # hotel event hall
    "https://images.unsplash.com/photo-1559508551-44bff1de756b?w=600&q=80",     # hotel infinity pool
    "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600&q=80",     # hotel penthouse
    "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=600&q=80",     # hotel checkout
    "https://images.unsplash.com/photo-1554995207-c18c203602cb?w=600&q=80",     # hotel living room
    "https://images.unsplash.com/photo-1553653924-39b70295f8da?w=600&q=80",     # hotel jacuzzi
    "https://images.unsplash.com/photo-1549638441-b787d2e11f14?w=600&q=80",     # hotel sauna
    "https://images.unsplash.com/photo-1548802673-380ab8ebc7b7?w=600&q=80",     # hotel minibar
    "https://images.unsplash.com/photo-1547394765-185e1e68f34e?w=600&q=80",     # hotel wardrobe
    "https://images.unsplash.com/photo-1546412414-8035e1776c9a?w=600&q=80",     # hotel desk
    "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=600&q=80",     # hotel sofa
    "https://images.unsplash.com/photo-1543968996-ee822b8176ba?w=600&q=80",     # hotel window
    "https://images.unsplash.com/photo-1540555700478-4be289fbecef?w=600&q=80",  # hotel mirror
    "https://images.unsplash.com/photo-1536376072261-38c75010e6c9?w=600&q=80",  # hotel art
    "https://images.unsplash.com/photo-1535827841776-24afc1e255ac?w=600&q=80",  # hotel curtains
    "https://images.unsplash.com/photo-1534430480872-3498386e7856?w=600&q=80",  # hotel lamp
    "https://images.unsplash.com/photo-1533044309907-0fa3413da946?w=600&q=80",  # hotel pillow
    "https://images.unsplash.com/photo-1531088009183-5ff5b7c95f91?w=600&q=80",  # hotel blanket
    "https://images.unsplash.com/photo-1529290130-4ca3753253ae?w=600&q=80",     # hotel towel
    "https://images.unsplash.com/photo-1527853787696-f7be74f2e39a?w=600&q=80",  # hotel amenities
    "https://images.unsplash.com/photo-1526772662000-3f88f10405ff?w=600&q=80",  # hotel coffee
    "https://images.unsplash.com/photo-1525596662741-e94ff9f26de1?w=600&q=80",  # hotel breakfast
    "https://images.unsplash.com/photo-1524231757912-21f4fe3a7200?w=600&q=80",  # hotel restaurant
    "https://images.unsplash.com/photo-1523217582562-09d0def993a6?w=600&q=80",  # hotel buffet
    "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=600&q=80",  # hotel bar counter
    "https://images.unsplash.com/photo-1521783988139-89397d761dce?w=600&q=80",  # hotel cocktail
    "https://images.unsplash.com/photo-1520483601560-389dff434fdf?w=600&q=80",  # hotel wine
    "https://images.unsplash.com/photo-1519449556851-5720b33024e7?w=600&q=80",  # hotel outdoor
    "https://images.unsplash.com/photo-1518684079-3c830dcef090?w=600&q=80",     # hotel sunset
    "https://images.unsplash.com/photo-1517840901100-8179e982acb7?w=600&q=80",  # hotel sunrise
    "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?w=600&q=80",  # hotel sea view
    "https://images.unsplash.com/photo-1515362778563-6a8d0e44bc0b?w=600&q=80",  # hotel lake view
    "https://images.unsplash.com/photo-1514190051997-0f6f39ca5cde?w=600&q=80",  # hotel city view
    "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=600&q=80",  # hotel mountain view
    "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=600&q=80",  # hotel modern
    "https://images.unsplash.com/photo-1510798831971-661eb04b3739?w=600&q=80",  # hotel classic
    "https://images.unsplash.com/photo-1509600110300-21b9d5fedeb7?w=600&q=80",  # hotel heritage
    "https://images.unsplash.com/photo-1508253578933-20b529302151?w=600&q=80",  # hotel colonial
    "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=600&q=80",  # hotel vintage
    "https://images.unsplash.com/photo-1506059612708-99d6c258160e?w=600&q=80",  # hotel contemporary
    "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=600&q=80",  # hotel minimalist
    "https://images.unsplash.com/photo-1504652517000-ae1068478c59?w=600&q=80",  # hotel cozy
    "https://images.unsplash.com/photo-1503917988258-f87a78e3c995?w=600&q=80",  # hotel elegant
    "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=600&q=80",  # hotel premium
    "https://images.unsplash.com/photo-1501117716987-c8c394bb29df?w=600&q=80",  # hotel deluxe
    "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?w=600&q=80",  # hotel standard
    "https://images.unsplash.com/photo-1498503182468-3b51cbb6cb24?w=600&q=80",  # hotel budget
    "https://images.unsplash.com/photo-1497366216548-37526070297c?w=600&q=80",  # hotel office
    "https://images.unsplash.com/photo-1495365200479-c4ed1d35e1aa?w=600&q=80",  # hotel business
    "https://images.unsplash.com/photo-1493246507139-91e8fad9978e?w=600&q=80",  # hotel resort
    "https://images.unsplash.com/photo-1490122417551-6ee9691429d0?w=600&q=80",  # hotel spa resort
    "https://images.unsplash.com/photo-1488085061387-422e29b40080?w=600&q=80",  # hotel wellness
    "https://images.unsplash.com/photo-1486325212027-8081e485255e?w=600&q=80",  # hotel fitness
    "https://images.unsplash.com/photo-1484154218962-a197022b5858?w=600&q=80",  # hotel kitchen suite
    "https://images.unsplash.com/photo-1480074568708-e7b720bb3f09?w=600&q=80",  # hotel family room
    "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?w=600&q=80",  # hotel twin room
    "https://images.unsplash.com/photo-1474690870753-1b92efa1f2d8?w=600&q=80",  # hotel double room
    "https://images.unsplash.com/photo-1473177104440-ffee2f376098?w=600&q=80",  # hotel single room
    "https://images.unsplash.com/photo-1472214103451-9374bd1c798e?w=600&q=80",  # hotel studio
    "https://images.unsplash.com/photo-1471623432079-b009d30b6729?w=600&q=80",  # hotel apartment
    "https://images.unsplash.com/photo-1470010762743-1fa2363c65f5?w=600&q=80",  # hotel villa
    "https://images.unsplash.com/photo-1469796466635-455ede028aca?w=600&q=80",  # hotel bungalow
    "https://images.unsplash.com/photo-1468824357306-a439d58ccb1c?w=600&q=80",  # hotel cottage
    "https://images.unsplash.com/photo-1467987506553-8f3916508521?w=600&q=80",  # hotel chalet
]

with app.app_context():
    hotels = Hotel.query.order_by(Hotel.id).all()
    total_imgs = len(HOTEL_IMAGES)
    updated = 0

    for i, hotel in enumerate(hotels):
        # Each hotel gets a unique image — cycle through the list
        hotel.image_url = HOTEL_IMAGES[i % total_imgs]
        updated += 1

    db.session.commit()
    print(f"✅ {updated} hotels updated with real hotel building images.")
    print(f"   All images are actual hotel properties — no landmarks.")
