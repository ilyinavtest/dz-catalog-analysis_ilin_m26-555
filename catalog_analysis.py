import math

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

# Этап.6. Словари

def count_by_genre(movies: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies: list[dict]) -> dict[str, list[str]]:
    filmography: dict[str, list[str]] = {}
    for movie in movies:
        for actor in movie["actors"]:
            filmography.setdefault(actor, []).append(movie["title"])
    return filmography


def above_average_ratings(movies: list[dict]) -> dict[str, float]:
    avg = average_rating(movies)
    return {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > avg
    }

# Этап 7. Множества

def all_genres(movies: list[dict]) -> set[str]:
    genres: set[str] = set()
    for movie in movies:
        genres |= movie["genres"]
    return genres


def common_actors(movie1: dict, movie2: dict) -> set[str]:
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a: list[dict], movies_b: list[dict]) -> set[str]:
    return all_genres(movies_a) - all_genres(movies_b)

# Этап 8. Итераторы и генераторы

def iter_high_rated(movies: list[dict], min_rating: float = 8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def demo_high_rated(movies: list[dict]) -> None:
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))


def total_duration_above_seven(movies: list[dict]) -> int:
    return sum(
        movie["duration_min"]
        for movie in movies
        if movie["rating"] > 7
    )

# Этап 9. Итоговый отчет

def build_report(movies: list[dict]) -> None:
    print("=" * 40)
    print(" " * 11, "ОТЧЁТ ПО КАТАЛОГУ")
    print("=" * 40)

    avg = average_rating(movies)
    oldest, newest, avg_age = catalog_age_stats(movies)
    total_minutes = sum(movie["duration_min"] for movie in movies)
    print("\nОбщая статистика:")
    print(f"  Всего фильмов: {len(movies)}")
    print(f"  Средний рейтинг: {avg}")
    print(f"  Возраст самого старого фильма: {oldest} лет")
    print(f"  Возраст самого нового фильма: {newest} лет")
    print(f"  Средний возраст: {avg_age} лет")
    print(f"  Суммарная длительность: {duration_in_hours(total_minutes)}")

    print("\nТоп-3 фильма по рейтингу:")
    for position, (title, rating) in enumerate(top_n_by_rating(movies, 3), start=1):
        print(f"  {position}. {normalize_title(title)} — {rating}")

    print("\nФильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    sorted_genres = sorted(
        genre_counts.items(),
        key=lambda item: item[1],
        reverse=True,
    )
    for genre, count in sorted_genres:
        print(f"  {genre}: {count}")

    print("\nВсе жанры каталога:")
    print("  " + ", ".join(sorted(all_genres(movies))))

if __name__ == "__main__":
    build_report(movies)