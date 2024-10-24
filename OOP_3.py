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

    def appointment_booking(self, time: str, date: str):
        self.__appointment_booking = f"{self.__name} вы записаны на {time}, {date} "

    def __str__(self):
        return (f"""
ФИО пациента: {self.__name} {self.__last_name}, {self.__second_name}
Возраст: {self.__year}
Заболевание: {self.__ill}
Запись к врачу: {self.__appointment_booking}

              """)


class TouristSpot:

    def __init__(self, name_place: str,
                 country: str,
                 type_place: str
                 ):
        self.__name_place = name_place
        self.__country = country
        self.__type_place = type_place

    def visit_place(self, name: str):
        return f"Уважаемый {name} , вы посетили уникальное место {self.__name_place}"

    def __str__(self):
        return f"""
Страна: {self.__country}
Туристическое место: {self.__name_place}
Тип достопремичательности: {self.__type_place}
    """


class ModelWindow:
    HORIZONTAl = 1960
    VERTICAL = 1080

    def __init__(self, title: str,
                 coord_left_up_x: int,
                 coord_left_up_y: int,
                 size_horizont: int,
                 size_vertical: int,
                 color_window: str,
                 visibility: bool,
                 frame: str
                 ):

        self.__title = title
        self.__cocoord_left_up_x = coord_left_up_x
        self.__cocoord_left_up_y = coord_left_up_y
        self.__size_horizont = size_horizont
        self.__size_vertical = size_vertical
        self.__color_window = color_window
        self.__visibility = "Невидимое"
        self.__frame = "Невидимое"

    def move_horizontal_right(self, new_move_x: int):

        if not isinstance(new_move_x, int):
            raise "TypeError"

        if new_move_x + self.__size_horizont > ModelWindow.HORIZONTAl or \
                new_move_x + self.__size_vertical < 0:
            raise 'Превышен диапазон'

        self.__cocoord_left_up_x += new_move_x


    def move_vertical(self, new_move_y: int):

        if new_move_y + self.__size_horizont > ModelWindow.VERTICAL or \
                new_move_y + self.__size_vertical < 0:
            raise "TypeError"

        if new_move_y - self.__size_horizont < 0:
            raise 'Превышен диапазон'

        self.__cocoord_left_up_x += new_move_y

    def set_size_window_horizontal(self, new_size: int):
        if not isinstance(new_size, int):
            raise "TypeError"
        if self.__size_horizont > ModelWindow.HORIZONTAl or\
                self.__size_horizont < 0:
            raise "Размеры окна вне допустимого диапазона"

        self.__size_horizont = new_size

    def set_size_window_vertical(self, new_size: int):
        if not isinstance(new_size, int):
            raise "TypeError"
        if self.__size_horizont > ModelWindow.VERTICAL or \
                self.__size_vertical < 0:
            raise "Размеры окна вне допустимого диапазона"

        self.__size_vertical = new_size

    def set_color_window(self, new_color: str):
        if not isinstance(new_color, str):
            raise "Неверный тип данных"

        self.__color_window = new_color

    def get_status_window(self):
        return self.__visibility

    def set_status_window(self, new_status: str):
        self.__visibility = new_status

    def __str__(self):
        return f"""
Название окна: {self.__title}
Координаты окна: оси Х = {self.__cocoord_left_up_x} оси Y = {self.__cocoord_left_up_y}
Размеры окна: по горизонтали {self.__size_horizont} по вертикали {self.__size_vertical} 
Видимость окна: {self.__visibility}
Наличие рамки окна: {self.__frame}
"""

class Program:

    @staticmethod
    def main():
        p = Patient("Роман", "Викторович", "Топоров", 49, "Притворство", )
        p.appointment_booking("13:30", "12/12/2024")
        print(p)

        t = TouristSpot("Озеро Байкал", "Россия", "Природа")
        print(t)

        w = ModelWindow("Главное", 50, 70, 1000, 600, "Синее", "Видимое!", "Отсутствует")
        w.set_color_window("Баклажан")
        w.get_status_window()
        w.set_status_window("Какое еще раз?")
        w.set_size_window_vertical(4000)
        w.set_size_window_horizontal(100)
        print(w)

Program.main()
