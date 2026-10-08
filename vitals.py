class Vitals:
    def __init__(self, heart_rate, blood_pressure, o2_saturation, timestamp):
        if not 1 <= heart_rate <= 300:
            raise ValueError ("Invalid heart rate: 400. Must be between 1 and 300.")
        if not 40 <= blood_pressure[0] <= 300:
            raise ValueError ("Invalid systolic blood pressure: 350. Must be between 40 and 300.")
        if not 20 <= blood_pressure[1] <= 200:
            raise ValueError ("Invalid diastolic blood pressure: 15. Must be between 20 and 200.")
        if not 50 <= o2_saturation < 100:
            raise ValueError ("Invalid O2 saturation: 49.0. Must be between 50.0 and 100.0.")
        
        self._heart_rate = heart_rate
        self._blood_pressure = blood_pressure
        self._o2_saturation = o2_saturation
        self._timestamp = timestamp

    def get_heart_rate(self):
        return self._heart_rate

    def get_blood_pressure(self):
        return self._blood_pressure

    def get_o2_saturation(self):
        return self._o2_saturation

    def get_timestamp(self):
        return self._timestamp

    # return true if any value is outside the normal range 
    def is_abnormal(self):
        if not 60 < self.get_heart_rate() < 100:
            return True

        systolic, diastolic = self.get_blood_pressure()
        if not 90 < systolic < 140:
            return True

        if not 60 < diastolic < 90:
            return True

        if not 95 < self.get_o2_saturation():
            return True

        return False

    def __str__(self):
        return f"HR: {self._heart_rate} bpm | BP: {self._blood_pressure[0]}/{self._blood_pressure[1]} | O2: {self._o2_saturation} % | {self._timestamp}" 

    def __repr__(self):
        return f"Vitals({self._heart_rate}, {self._blood_pressure}, {self._o2_saturation}, '{self._timestamp}')"

    # Returns True if all four values match.
    def __eq__(self, other):
        other_hr = other.get_heart_rate()
        other_sys, other_dys = other.get_blood_pressure()
        other_o2 = other.get_o2_saturation()

        # what is the difference between calling the get_heart_rate and doing self._heart_rate
        if self.get_heart_rate() != other_hr:
            return False

        sys,dys = self.get_blood_pressure()

        if sys != other_sys or dys != other_dys:
            return False

        if self.get_o2_saturation() != other_o2:
            return False

        return True

   
    def __lt__(self, other):
        return True if self.get_heart_rate() < other.get_heart_rate() else False


    def __gt__(self, other):
        return True if self.get_heart_rate() > other.get_heart_rate() else False



# def main():
#     v1 = Vitals(67, (91, 50), 90.2, "2024-03-10 09:30")
#     v2 = Vitals(65, (92, 51), 91.3, "2025-09-11 11:30")
#     # print("hella")

#     print(v1 > v2)

# if __name__ == "__main__":
#     main()

