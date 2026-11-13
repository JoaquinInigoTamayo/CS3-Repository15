from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass

class TempSensor(Sensor):
    def get_reading(self):
        return "24.5°C"

class PHSensor(Sensor):
    def get_reading(self):
        return "7.2 pH"

phSensor = PHSensor()
tempSensor = TempSensor()
print("--- Lab Inventory System ---")
print("[pH Sensor] Reading:", phSensor.get_reading(), "(Neutral)")
print("[Temperature Sensor] Reading:", tempSensor.get_reading())
print("----------------------------")


