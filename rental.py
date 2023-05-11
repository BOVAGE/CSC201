class Scooter:
    """Scooter class"""

    def __init__(
        self,
        name_of_rental_company,
        starting_fee_for_a_ride,
        price_per_100_meters_ride,
        available_riding_distance,
    ):
        self.name_of_rental_company = name_of_rental_company
        self.starting_fee_for_a_ride = starting_fee_for_a_ride
        self.price_per_100_meters_ride = price_per_100_meters_ride
        self.available_riding_distance = available_riding_distance

    def price(self, length_of_ride):
        """returns the price of a ride taking into account the
        starting fee and price_per_100_meters_ride"""
        if length_of_ride <= self.available_riding_distance:
            return self.starting_fee_for_a_ride + (length_of_ride * 1000) * (
                self.price_per_100_meters_ride / 100
            )
        return 1000

    def ride(self, length_of_ride):
        """decrease the available_riding_distance by length_of_ride
        but set to zero if available_riding_distance becomes negative after the deduction
        """
        diff = self.available_riding_distance - length_of_ride
        if diff <= 0:
            self.available_riding_distance = 0
        else:
            self.available_riding_distance = diff

    def charge(self, number_of_kilometers):
        """increase the available_riding_distance by number_of_kilometers passed in"""
        print(f"Charged scooter by {number_of_kilometers} km")
        self.available_riding_distance += number_of_kilometers


class Rental:
    """Rental class for Scooter objects"""

    def __init__(self, list_of_scooters):
        self.list_of_scooters = list_of_scooters

    def display_choices(self, length_of_ride):
        """display the scooter available in ascending order (sorted by price)."""
        scooters_map = {}
        for scooter in self.list_of_scooters:
            price = scooter.price(length_of_ride)
            name = scooter.name_of_rental_company
            scooters_map[name] = price

        def sort_function_by_price(item):
            price = item[1]
            return price

        sorted_scooter_list = sorted(scooters_map.items(), key=sort_function_by_price)
        for name, price in sorted_scooter_list:
            print(f"Name: {name}, Price: {price}")

    def rent(self, name_of_scooter, length_of_ride):
        """ride a scooter whose name is passed in
        if the length_of_ride does not exceed
        the scooter's available_riding_distance"""
        matched_scooters = list(
            filter(
                lambda scooter: scooter.name_of_rental_company.lower()
                == name_of_scooter.lower(),
                self.list_of_scooters,
            )
        )
        if matched_scooters:
            matched_scooter = matched_scooters[0]
            if length_of_ride <= matched_scooter.available_riding_distance:
                print(matched_scooter.price(length_of_ride))
                matched_scooter.ride(length_of_ride)
            else:
                print(
                    "The requested length exceed the available riding distance of the scooter"
                )

    def charge_scooter(self, name_of_scooter, number_of_kilometers):
        """charge a scooter whose name is passed in by the number_of_kilometers"""
        matched_scooters = list(
            filter(
                lambda scooter: scooter.name_of_rental_company.lower()
                == name_of_scooter.lower(),
                self.list_of_scooters,
            )
        )
        if matched_scooters:
            matched_scooter = matched_scooters[0]
            matched_scooter.charge(number_of_kilometers)


def main():
    list_of_scooters = []
    for i in range(3):
        scooter_detail = input("Enter each scooter details:\n")
        scooter_detail_info = scooter_detail.split(",")
        name = scooter_detail_info[0].strip()
        starting_fee_for_a_ride = float(scooter_detail_info[1].strip())
        price_per_100_meters_ride = float(scooter_detail_info[2].strip())
        available_riding_distance = float(scooter_detail_info[3].strip())
        scooter = Scooter(
            name,
            starting_fee_for_a_ride,
            price_per_100_meters_ride,
            available_riding_distance,
        )
        list_of_scooters.append(scooter)
    rental = Rental(list_of_scooters)
    rental.display_choices(2)
    rental.rent("Bolt", 3)
    rental.rent("Tuul", 18)
    rental.rent("Tuul", 5)
    rental.charge_scooter("Tuul", 5)
    rental.rent("Tuul", 2)


if __name__ == "__main__":
    main()
