from datetime import datetime

class SuperDate(datetime):
    # Метод для получения сезона года
    def get_season(self):
        seasons = {
            'Winter': (12, 1, 2),
            'Spring': (3, 4, 5),
            'Summer': (6, 7, 8),
            'Autumn': (9, 10, 11)
        }
        month = self.month
        for season, months in seasons.items():
            if month in months:
                return season
        return None

    # Метод для получения времени суток
    def get_time_of_day(self):
        times_of_day = {
            'Morning': range(6, 12),
            'Day': range(12, 18),
            'Evening': range(18, 24),
            'Night': range(0, 6)
        }
        hour = self.hour
        for time_of_day, hours in times_of_day.items():
            if hour in hours:
                return time_of_day
        return None

# Пример работы класса
a = SuperDate(2024, 2, 22, 12)
print(a.get_season())        # Winter
print(a.get_time_of_day())   # Day
