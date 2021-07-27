from recall.context import Context
from typing import List
import recall.strategy as strategy
import concurrent.futures
import time
from recall.model.lsh import get_item_lsh
from recall.dataset.embedding import get_one_item_embedding
from recall import util

strategies: List[strategy.RecallStrategy] = [
    strategy.UserEmbeddingStrategy(),
    strategy.HighRatingStrategy(),
    strategy.MostRatingStrategy(),
]


def anime_recall(context: Context, n=20) -> List[int]:
    """
    returns a list of anime ids
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        outputs = executor.map(lambda s: run_strategy(s, context, n), strategies)
        # outputs = [[1, 2, 3], [3, 4, 5]]
        outputs = [aid for l in outputs for aid in l]
        # outputs = [1, 2, 3, 3, 4, 5]
        outputs = list(dict.fromkeys(outputs))
        # outputs = [1, 2, 3, 4, 5]
        print(f'Got {len(outputs)} uniq recall results')
        return outputs


def similar_animes(context: Context, n=20) -> List[int]:
    lsh = get_item_lsh()
    target_item_emb = get_one_item_embedding(context.anime_id)
    outputs = lsh.search(target_item_emb, n=n)
    return outputs


def run_strategy(strategy: strategy.RecallStrategy, context: Context, n):
    start_time = time.time()
    res = strategy.recall(context, n=n)
    elapse_time = time.time() - start_time
    print('Strategy %s took %.2fms' % (strategy.name(), elapse_time * 1000))
    return res
