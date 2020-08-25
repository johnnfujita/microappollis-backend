#directory naming
def artist_directory_path(instance, filename):
    return 'artist_{0}/{1}'.format(instance.artist.name, filename).lower().replace(" ","_")

def location_directory_path(instance, filename):
    return 'location_{0}/{1}'.format(instance.name, filename).lower().replace(" ","_")