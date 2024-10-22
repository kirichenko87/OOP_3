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

    def appointment_booking(self, time: str, date: str ):
        self.__appointment_booking = f"{self.__name} вы записаны на {time}, {date} "

    
    def __str__(self):
        return(f"""
ФИО пациента: {self.__name} {self.__last_name}, {self.__second_name}
Возраст: {self.__year}
Заболевание: {self.__ill}
Запись к врачу: {self.__appointment_booking}

              """)






class Program:
    
    @staticmethod
    def main():
        p = Patient("Роман", "Викторович", "Топоров", 49, "Притворство", )
        p.appointment_booking("13:30", "12/12/2024")
        print(p)

Program.main()