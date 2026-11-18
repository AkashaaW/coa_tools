from coa_tools.cache import access_cache

cache_lines = [None, None, None, None]
addresses = [16, 19, 0, 16]

hits = 0
misses = 0

for address in addresses:
    result = access_cache(address, cache_lines)
    print(f"Address {address}: {result}")

    if result == "HIT":
        hits += 1
    else:
        misses += 1

total = hits + misses
hit_rate = hits / total if total > 0 else 0

print(f"Hits: {hits}")
print(f"Misses: {misses}")
print(f"Hit rate: {hit_rate:.1%}")