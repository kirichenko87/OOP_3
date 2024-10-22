class Patient:

    

    def __init__(self, 
                 name: str, 
                 second_name: str, 
                 last_name: str,
                 year: int,
                 ill: str):

        self.__name = name
        self.__second_name = second_name
        self.__last_name = last_name
        self.__year = year
        self.__ill = ill
        self.__appointment_booking = ''
        self.__time = ''
        self.__day = ''

    def input_name(self, name: str):
        self.__name = name

    def set_appointment_booking(self):
        self.appointment_booking = f"{self.__name} вы записаны на {self.time} время {self.day} числа"

    def set_time(self, hours: str, min: str):
        self.time = hours + ':' + min

    def set_day(self, day: str, mounth: str, year: str):
        self.day = day + '.' + '.' + year

    def get_appointment_booking(self):
        return self.appointment_booking
    
    def __str__(self):
        print(f"""
ФИО пациента: {self.__name} {self.__last_name}, {self.__second_name}
Возраст: {self.__year}
Заболевание: {self.__ill}
Время и дата записи: {self.__appointment_booking}
              """)
        
class Program:
    
    @staticmethod
    def main():
        p = Patient("Роман", "Викторович", "Топоров", 49, "Притворство")
        p.set_time("13", "30")
        p.set_day("30", "02", "2024")
        p.get_appointment_booking()
        print(p)

Program.main()