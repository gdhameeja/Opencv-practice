# utils for the opencv tutorial


def get_image_list(path):
    """ Function to return the list of images under a particular directory """
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]
