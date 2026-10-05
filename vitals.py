class Vitals:
    def __init__(self, heart_rate, blood_pressure, o2_saturation, timestamp):
        if not 1 <= heart_rate <= 300:
            raise ValueError
        if not 40 <= blood_pressure[0] <= 300:
            raise ValueError
        if not 20 <= blood_pressure[1] <= 200:
            raise ValueError
        if not 50 <= o2_saturation < 100:
            raise ValueError
        
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

    def __str__(self):
        return f"HR: {self._heart_rate} bpm | BP: {self._blood_pressure[0]}/{self._blood_pressure[1]} | O2: {self._o2_saturation} % | {self._timestamp}" 

def main():
    v1 = Vitals(62, (91, 50), 90.2, "2024-03-10 09:30")
    # print("hella")
    # print(v1.get_timestamp(), "!")
    # print(v1.is_abnormal(), "~~~~~~")

    print(str(v1))

if __name__ == "__main__":
    main()

