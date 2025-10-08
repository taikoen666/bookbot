def count_words(content: str) -> int:
    return len(content.split())


def count_letters(content: str):
    result = {}
    for c in content.lower():
        result[c] = result[c] + 1 if c in result else 1
    return result


def sorted_hist(hist: dict):
    result = [{'char': k, 'num': v} for k, v in hist.items()]
    result.sort(key=lambda x: x['num'], reverse=True)
    return result
