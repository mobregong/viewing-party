# # Wave 1

def create_movie(title, genre, rating):
    movie = {}
    if title and genre and rating:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
    else: 
        movie = None
    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data

# # Wave 2

def get_watched_avg_rating(user_data):
    watched_ratings = []
    for movie in user_data["watched"]:
        watched_ratings.append(movie["rating"])
    number_watched = len(watched_ratings)
    if number_watched:
        watched_avg_rating = sum(watched_ratings)/number_watched
    else:
        watched_avg_rating = 0.0
    return watched_avg_rating

def get_most_watched_genre(user_data):
    watched_genres = {}
    if user_data["watched"]:
        for movie in user_data["watched"]:
                genre = movie["genre"]
                if genre in watched_genres:
                    watched_genres[genre] += 1
                else:
                    watched_genres[genre] = 1
        max_watched_genre_freq = max(watched_genres.values())
        for genre, freq in watched_genres.items():
            if freq == max_watched_genre_freq:
                most_watched_genre = genre
        return most_watched_genre

# # Wave 3

def create_user_watched_set(user_data):
    user_watched_set = set()
    for movie in user_data["watched"]:
        user_watched_set.add(movie["title"])
    return user_watched_set

def create_friends_watched_set(user_data):
    friends_watched_set = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_set.add(movie["title"])
    return friends_watched_set

def get_unique_watched(user_data):
    user_watched_set = create_user_watched_set(user_data)
    friends_watched_set = create_friends_watched_set(user_data)
    
    user_unique_watched_list = []
    user_unique_watched_set = user_watched_set - friends_watched_set
    for movie in user_unique_watched_set:
        user_unique_watched_list.append({"title": movie})
    return user_unique_watched_list

def get_friends_unique_watched(user_data):
    user_watched_set = create_user_watched_set(user_data)
    friends_watched_set = create_friends_watched_set(user_data)
    friends_unique_watched_list = []
    friends_unique_watched_set = friends_watched_set - user_watched_set
    for movie in friends_unique_watched_set:
        friends_unique_watched_list.append({"title": movie})
    return friends_unique_watched_list

# # Wave 4

def is_movie_in_user_watched(user_watched_set, movie):
    if not movie["title"] in user_watched_set:
        movie_not_in_user_watched = True
    else:
        movie_not_in_user_watched = False
    return movie_not_in_user_watched

def get_available_recs(user_data):
    recommended_movies = []
    user_watched_set = create_user_watched_set(user_data)
    movie_rec = {}
    already_recommended = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["host"] in user_data["subscriptions"]:
                host_available = True
            else:
                host_available = False
            if is_movie_in_user_watched(user_watched_set, movie) and host_available:
                if not movie["title"] in already_recommended:
                    movie_rec = {"title": movie["title"], "host": movie["host"]}
                    recommended_movies.append(movie_rec)
                    already_recommended.append(movie["title"])
    return recommended_movies

# # Wave 5

def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    user_watched_set = create_user_watched_set(user_data)
    recommended_movies = []
    already_recommended = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["genre"] == most_watched_genre:
                matching_genre = True
            else:
                matching_genre = False
            if is_movie_in_user_watched(user_watched_set, movie) and matching_genre:
                if not movie["title"] in already_recommended:
                    movie_rec = {"title": movie["title"], "genre": movie["genre"]}
                    recommended_movies.append(movie_rec)
                    already_recommended.append(movie["title"])
    return recommended_movies

def get_rec_from_favorites(user_data):
    recommended_movies = []
    friends_watched_set = create_friends_watched_set(user_data)
    for movie in user_data["favorites"]:
        if not movie["title"] in friends_watched_set:
            movie_rec = {"title": movie["title"]}
            recommended_movies.append(movie_rec)
    return recommended_movies