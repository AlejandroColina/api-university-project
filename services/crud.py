from db.models.person import Person
from db.conn import SessionLocal


db = SessionLocal()


def get_all():
    return db.query(Person).all()


def get_a_Person(id_Person):
    response = db.query(Person).filter(Person.id == id_Person).first()

    if not response:
        return {'msg': 'Dont exist the id in DB'}
    else:
        return response


def create_Person(Person):
    m = Person(device=Person.device, consumo=Person.consumo, date=Person.date)
    db.add(m)
    db.commit()
    return m


def update_Person(id_Person, parameters):
    response = db.query(Person).filter(Person.id == id_Person).first()
    if not response:
        return {'msg': 'Dont exist the id in DB'}
    else:
        if len(parameters.consumo) and len(parameters.date) and len(parameters.device):
            response.consumo = parameters.consumo
            response.device = parameters.device
            response.date = parameters.date
            db.commit()
            info = db.query(Person).filter(Person.id == id_Person).first()
            return info

        elif len(parameters.consumo) and len(parameters.date) == 0 and len(parameters.device) == 0  :
            response.consumo = parameters.consumo
            db.commit()
            info = db.query(Person).filter(Person.id == id_Person).first()
            return info

        elif len(parameters.device) and len(parameters.date) == 0 and len(parameters.consumo) == 0:
            response.device = parameters.device
            db.commit()
            info = db.query(Person).filter(Person.id == id_Person).first()
            return info

        else:
            response.date = parameters.date
            db.commit()
            info = db.query(Person).filter(Person.id == id_Person).first()
            return info


def delete_Person(id_Person):
    response = db.query(Person).filter(Person.id == id_Person).first()
    if not response:
        return {'msg': 'Dont exist the id in DB'}
    else:
        db.delete(response)
        db.commit()
        return {'msg':'deleted!'}