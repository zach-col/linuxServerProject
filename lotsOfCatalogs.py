from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Catalog, Base, CatalogItem, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create filler info
User1 = User(
    name="billy",
    email="example@gmail.com",
    picture='none')
session.add(User1)
session.commit()

catalog1 = Catalog(
    user_id=1,
    name="Baseball")
session.add(catalog1)
session.commit()

catalogItem = CatalogItem(
    user_id=1,
    name="Helmet",
    description="The Helmet is used to protect the batters head.",
    catalog=catalog1)
session.add(catalogItem)
session.commit()

# Create filler info
User2 = User(
    name="bob",
    email="example@example.com",
    picture='none')
session.add(User2)
session.commit()

catalog2 = Catalog(
    user_id=2,
    name="Football")
session.add(catalog2)
session.commit()

catalogItem2 = CatalogItem(
    user_id=2,
    name="Football",
    description="Cleats are used to provide addational traction on slippery or soft surfaces",
    catalog=catalog2)
session.add(catalogItem2)
session.commit()

print "added catalogs and catalog items"
