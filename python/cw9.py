class Vehicle:
    def __init__(self, vehicle_id: str, base_rate: float):
        self._vehicle_id = vehicle_id      
        self._base_rate = base_rate       

    def display_details(self) -> str:
        return f"Vehicle ID: {self._vehicle_id}, Base Rate: {self._base_rate}"

    def rental_charge(self) -> float:
        return 0.0


class Car(Vehicle):
    def __init__(self, vehicle_id: str, base_rate: float, num_seats: int):
        super().__init__(vehicle_id, base_rate)
        self.num_seats = num_seats

    def rental_charge(self) -> float:
        return self._base_rate * self.num_seats

