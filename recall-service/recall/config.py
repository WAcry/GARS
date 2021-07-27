import os

config = {
    'dataset_path': '/home/ziyuan/PycharmProjects/gars/dataset',
    'deepwalk': {
        'sample_length': 10,
        'sample_count': 100 * 1000
    },
    'item2vec': {
        'vector_size': 5,
        'max_iter': 5,
        'window_size': 10
    },
    'redis': {
        'host': '127.0.0.1',
        'port': 6379,
        'db': 0
    },
    'most_rating': {
        'shuffle_sample': True
    },
    'high_rating': {
        'shuffle_sample': True
    }
}
