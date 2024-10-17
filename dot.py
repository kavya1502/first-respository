import concurrent.futures

def dot_product_parallel(v1, v2):
    def partial_dot(start, end):
        return sum(v1[i] * v2[i] for i in range(start, end))

    size = len(v1)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(partial_dot, i, i + size // 2) for i in range(0, size, size // 2)]
        result = sum(f.result() for f in futures)
    return result

