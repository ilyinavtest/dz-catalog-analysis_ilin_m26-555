# Каталог стримингового сервиса. Датасет.

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]

# Этап 1 Разминка: переменные, числа, math

import math

def average_rating(movies: list[dict]) -> float:
    if not movies:
        return 0.0
    total = sum(movie["rating"] for movie in movies)
    return round(total / len(movies), 1)

def catalog_age_stats(movies: list[dict], current_year: int = 2026) -> tuple:
    if not movies:
        return (0, 0, 0)
    ages = [current_year - movie["year"] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    average = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, average)

def duration_in_hours(minutes: int) -> str:
    hours = minutes // 60
    remainder = minutes % 60
    return f"{hours}ч {remainder}м"

# Этап 2. Условия и match

def rating_tier(rating: float) -> str:
    if rating >= 9:
        tier = "шедевр"
    elif rating >= 7:
        tier = "хорошо"
    elif rating >= 5:
        tier = "средне"
    else:
        tier = "слабо"
    return tier if rating >= 0 else "некорректная оценка"

def decade_label(year: int) -> str:
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"

# Этап 3. Циклы

def print_non_comedy(movies: list[dict]) -> None:
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])

def find_first_masterpiece(movies: list[dict]) -> None:
    index = 0
    while index < len(movies):
        if movies[index]["rating"] > 9.0:
            print(movies[index]["title"])
            break
        index += 1
    else:
        print("Шедевров не найдено")

def count_long_movies(movies: list[dict], threshold: int = 120) -> int:
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count

# Этап 4. Строки

def normalize_title(title: str) -> str:
    words = title.split()
    normalized = [word[0].upper() + word[1:] for word in words if word]
    return " ".join(normalized)

def make_slug(title: str) -> str:
    return normalize_title(title).lower().replace(" ", "-")

def format_report_line(movie: dict) -> str:
    title = normalize_title(movie["title"])
    genres = ", ".join(sorted(movie["genres"]))
    duration = duration_in_hours(movie["duration_min"])
    return (
        f"{title} ({movie['year']}) | "
        f"жанры: {genres} | "
        f"рейтинг: {movie['rating']} | "
        f"длительность: {duration}"
    )

# Этап 5. Списки

def titles_sorted_by_rating(movies: list[dict]) -> list[str]:
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]

def top_n_by_rating(movies: list[dict], n: int = 3) -> list[tuple[str, float]]:
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]