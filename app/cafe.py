import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)

class Cafe:

    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated.")

        vaccine_info = visitor["vaccine"]
        expiration_date = vaccine_info.get("expiration_date")

        if expiration_date is None:
            raise OutdatedVaccineError("Visitor's vaccine expiration date missing.")

        # Якщо expiration_date - рядок, перетворюємо в дату
        if isinstance(expiration_date, str):
            try:
                expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d").date()
            except ValueError:
                raise OutdatedVaccineError("Visitor's vaccine expiration date is invalid.")

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Visitor's vaccine is outdated.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"
