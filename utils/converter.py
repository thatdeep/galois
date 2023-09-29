import numpy as np
from galois_field import PrimeFieldElement


def to_integers(collection):
    if isinstance(collection, PrimeFieldElement):
        return collection.value
    if isinstance(collection, dict):
        return {key: to_integers(value) for key, value in collection.items()}
    if isinstance(collection, (list, set, tuple)):
        return type(collection)(map(to_integers, collection))
    if isinstance(collection, np.ndarray):
        return np.array(list(map(to_integers, collection.flatten()))).reshape(collection.shape)
    return collection

def to_prime_field_elements(collection, p):
    if isinstance(collection, (int, np.integer)):
        return PrimeFieldElement(collection, p)
    if isinstance(collection, dict):
        return {key: to_prime_field_elements(value, p) for key, value in collection.items()}
    if isinstance(collection, (list, set, tuple)):
        return type(collection)(map(lambda x: to_prime_field_elements(x, p), collection))
    if isinstance(collection, np.ndarray):
        reshaped_array = np.array(
            list(map(lambda x: to_prime_field_elements(x, p), collection.flatten())),
            dtype=object  # Explicitly set dtype to object
        )
        return reshaped_array.reshape(collection.shape)
    else:
        print(type(collection), isinstance(collection, int))
    return collection