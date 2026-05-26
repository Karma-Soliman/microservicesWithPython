from app.database import SessionLocal, engine
from app.models import Base, Game

GAMES = [
    {
        "title": "Hollow Knight",
        "genre": "metroidvania",
        "platform": "PC",
        "release_year": 2017,
        "cover_url": "https://example.com/hollow-knight.jpg",
    },
    {
        "title": "Celeste",
        "genre": "platformer",
        "platform": "PC",
        "release_year": 2018,
        "cover_url": "https://example.com/celeste.jpg",
    },
    {
        "title": "Stardew Valley",
        "genre": "simulation",
        "platform": "PC",
        "release_year": 2016,
        "cover_url": "https://example.com/stardew-valley.jpg",
    },
    {
        "title": "Hades",
        "genre": "roguelike",
        "platform": "PC",
        "release_year": 2020,
        "cover_url": "https://example.com/hades.jpg",
    },
    {
        "title": "The Legend of Zelda: Breath of the Wild",
        "genre": "adventure",
        "platform": "Switch",
        "release_year": 2017,
        "cover_url": "https://example.com/breath-of-the-wild.jpg",
    },
]


def run():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    imported = 0

    for data in GAMES:
        existing = db.query(Game).filter(Game.title == data["title"]).first()
        if existing:
            continue

        game = Game(**data)
        db.add(game)
        imported += 1

    db.commit()
    db.close()
    print(f"Imported {imported} games.")


if __name__ == "__main__":
    run()
