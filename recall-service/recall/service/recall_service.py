from recall.context import Context
from typing import List
import recall.strategy as strategy
import concurrent.futures
import time
from recall.model.lsh import get_item_lsh, get_item_meta_lsh
from recall.dataset.embedding import get_one_item_embedding, get_one_item_meta_embedding
from recall import util

strategies: List[strategy.RecallStrategy] = [
    strategy.UserEmbeddingStrategy(),
    strategy.HighRatingStrategy(),
    strategy.MostRatingStrategy(),
    strategy.RecentClickStrategy()
]


def anime_recall(context: Context, n=20):
    """
    returns a list of anime ids
    """

    # AB test
    # A (bucket 0): strategy 0, 1, 2
    # B (bucket 1): strategy 0
    experiment_strategies = strategies
    bucket = util.bucketize(context.user_id, 2)
    if bucket == 1:
        experiment_strategies = strategies[:1]
    print(f"user_id {context.user_id}, ab strategy {bucket}")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        outputs = executor.map(lambda s: run_strategy(s, context, n), experiment_strategies)
        # outputs = [[1, 2, 3], [3, 4, 5]]
        outputs = [aid for l in outputs for aid in l]
        # outputs = [1, 2, 3, 3, 4, 5]
        outputs = list(dict.fromkeys(outputs))
        # outputs = [1, 2, 3, 4, 5]
        print(f'Got {len(outputs)} uniq recall results')
        return [{'anime_id': id, 'ab_recall': bucket} for id in outputs]


# def similar_animes(context: Context, n=20):
#     lsh = get_item_lsh()
#     target_item_emb = get_one_item_embedding(context.anime_id)
#     outputs = lsh.search(target_item_emb, n=n)
#     return [{'anime_id': id} for id in outputs]

def similar_animes(context: Context, n=20) -> List[int]:
    lsh = get_item_meta_lsh()
    target_item_emb = get_one_item_meta_embedding(context.anime_id)
    outputs = lsh.search(target_item_emb, n=n)
    return [{'anime_id': int(id)} for id in outputs]

def run_strategy(strategy: strategy.RecallStrategy, context: Context, n):
    start_time = time.time()
    res = strategy.recall(context, n=n)
    elapse_time = time.time() - start_time
    print('Strategy %s took %.2fms' % (strategy.name(), elapse_time * 1000))
    return res
