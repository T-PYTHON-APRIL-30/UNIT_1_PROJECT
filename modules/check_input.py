def check_add(movie, movie_name, movie_reviwe, movie_rating, movie_section):
    if type(movie_name) != str:
        raise Exception("Enter a real movie..")
    elif len(movie_reviwe) > 200:
        raise Exception("You have exceeded the limit!!")
    
    if movie_section == "1":
        movie["section"] = "watching"
    elif movie_section == "2":
        movie["section"] = "completed"
    elif movie_section == "3":
        movie["section"] = "plan to watch"
    else:
        raise Exception("type a correct number")
    
    if movie_rating == "1":
        movie["rating"] = "★☆☆☆☆"
    elif movie_rating == "2":
        movie["rating"] = "★★☆☆☆"
    elif movie_rating == "3":
        movie["rating"] = "★★★☆☆"
    elif movie_rating == "4":
        movie["rating"] = "★★★★☆"
    elif movie_rating == "5":
        movie["rating"] = "★★★★★"
    else:
        raise Exception("type a correct number")