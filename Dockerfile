# Базовый образ
FROM python:3.13-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем весь проект внутрь контейнера
COPY . .

# По умолчанию запускаем bash, можно переопределить
CMD ["bash"]