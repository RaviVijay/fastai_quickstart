
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: dev_nb/langmodel-classify-imdb-qs.ipynb

def return_path_dict(name, url):
    path = {}
    path[name] = untar_data(url)
    print(path[name])
    print(path[name].ls())
    return path