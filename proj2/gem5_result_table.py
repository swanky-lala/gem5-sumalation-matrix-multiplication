

import pandas as pd

# Define the data for each part
part1_data = {
    'Cache': ['Unified L1 cache'],
    'Hits': [11810614],
    'Misses': [3490],
    'AvgMissLatency': [89913.753582]
}

part2_data = {
    'Cache': ['L1 data and instruction caches'],
    'Dcache_Hits': [3312982],
    'Dcache_Misses': [2285],
    'Dcache_AvgMissLatency': [79097.592998],
    'Icache_Hits': [8497655],
    'Icache_Misses': [1182],
    'Icache_AvgMissLatency': [76206.429780]
}

part3_data = {
    'Cache': ['Unified L1 cache (Associativity=1)', 'Unified L1 cache (Associativity=2)', 'Unified L1 cache (Associativity=4)',
              'Unified L1 cache (Associativity=8)', 'Unified L1 cache (Associativity=16)', 'Unified L1 cache (Associativity=32)',
              'L1 data and instruction caches (Associativity=1)', 'L1 data and instruction caches (Associativity=2)',
              'L1 data and instruction caches (Associativity=4)', 'L1 data and instruction caches (Associativity=8)',
              'L1 data and instruction caches (Associativity=16)', 'L1 data and instruction caches (Associativity=32)'],
    'Hits': [11810614, 11810614, 11810632, 11810634, 11810636, 11810638, 3312982, 3312982, 3312983, 3312983, 3312983, 3312983],
    'Misses': [3490, 3490, 3472, 3470, 3468, 3466, 2285, 2285, 2284, 2284, 2284, 2284],
    'AvgMissLatency': [89913.753582, 89913.753582, 89985.311060, 90031.988473, 90078.719723, 90125.504905, 79097.592998, 79097.592998,
                       79131.786340, 79131.786340, 79131.786340, 79131.786340]
}

part4_data = {
    'Cache': ['Size=(l1i_size=64kB, l1d_size=128kB, l2_size=2MB)', 'Size=(l1i_size=64kB, l1d_size=128kB, l2_size=4MB)',
              'Size=(l1i_size=64kB, l1d_size=256kB, l2_size=2MB)', 'Size=(l1i_size=64kB, l1d_size=256kB, l2_size=4MB)',
              'Size=(l1i_size=128kB, l1d_size=128kB, l2_size=2MB)', 'Size=(l1i_size=128kB, l1d_size=128kB, l2_size=4MB)',
              'Size=(l1i_size=128kB, l1d_size=256kB, l2_size=2MB)', 'Size=(l1i_size=128kB, l1d_size=256kB, l2_size=4MB)',
              'Size=(l1i_size=256kB, l1d_size=128kB, l2_size=2MB)', 'Size=(l1i_size=256kB, l1d_size=128kB, l2_size=4MB)',
              'Size=(l1i_size=256kB, l1d_size=256kB, l2_size=2MB)', 'Size=(l1i_size=256kB, l1d_size=256kB, l2_size=4MB)',
              'Size=(l1i_size=64kB, l1d_size=64kB, l2_size=2MB)', 'Size=(l1i_size=64kB, l1d_size=64kB, l2_size=4MB)',
              'Size=(l1i_size=64kB, l1d_size=32kB, l2_size=2MB)', 'Size=(l1i_size=64kB, l1d_size=32kB, l2_size=4MB)',
              'Size=(l1i_size=32kB, l1d_size=64kB, l2_size=2MB)', 'Size=(l1i_size=32kB, l1d_size=64kB, l2_size=4MB)',
              'Size=(l1i_size=32kB, l1d_size=32kB, l2_size=2MB)', 'Size=(l1i_size=32kB, l1d_size=32kB, l2_size=4MB)',
              'Size=(l1i_size=128kB, l1d_size=64kB, l2_size=2MB)', 'Size=(l1i_size=128kB, l1d_size=64kB, l2_size=4MB)',
              'Size=(l1i_size=128kB, l1d_size=32kB, l2_size=2MB)', 'Size=(l1i_size=128kB, l1d_size=32kB, l2_size=4MB)',
              'Size=(l1i_size=256kB, l1d_size=64kB, l2_size=2MB)', 'Size=(l1i_size=256kB, l1d_size=64kB, l2_size=4MB)',
              'Size=(l1i_size=256kB, l1d_size=32kB, l2_size=2MB)', 'Size=(l1i_size=256kB, l1d_size=32kB, l2_size=4MB)'],
    'Dcache_Hits': [3312982, 3312982, 3312982, 3312982, 3312982, 3312982, 3312982, 3312982,
                     3312982, 3312982, 3312982, 3312982, 3312982, 3312982, 3312982, 3312982,
                     3312982, 3312982, 3312982, 3312982, 3312982, 3312982, 3312982, 3312982,
                     3312982, 3312982, 3312982, 3312982],
    'Dcache_Misses': [2285, 2285, 2285, 2285, 2285, 2285, 2285, 2285,
                       2285, 2285, 2285, 2285, 2285, 2285, 2285, 2285,
                        2285, 2285, 2285, 2285, 2285, 2285, 2285, 2285,
                        2285, 2285, 2285, 2285],
    'Dcache_AvgMissLatency': [79097.592998, 79097.592998, 79131.786340, 79131.786340, 79097.592998, 79097.592998,
                               79131.786340, 79131.786340, 79097.592998, 79097.592998, 79131.786340, 79131.786340,
                               79097.592998, 79097.592998, 79131.786340, 79131.786340, 79097.592998, 79097.592998,
                               79131.786340, 79131.786340, 79097.592998, 79097.592998, 79131.786340, 79131.786340,
                               79097.592998, 79097.592998, 79131.786340, 79131.786340],
    'Icache_Hits': [8497655, 8497655, 8497655, 8497655, 8497653, 8497653, 8497655, 8497655,
                     8497655, 8497655, 8497653, 8497653, 8497655, 8497655, 8497653, 8497653,
                     8497655, 8497655, 8497653, 8497653, 8497655, 8497655, 8497653, 8497653,
                     8497655, 8497655, 8497653, 8497653],
    'Icache_Misses': [1182, 1182, 1182, 1182, 1184, 1184, 1182, 1182,
                       1182, 1182, 1184, 1184, 1182, 1182, 1184, 1184,
                       1182, 1182, 1184, 1184, 1182, 1182, 1184, 1184,
                       1182, 1182, 1184, 1184],
    'Icache_AvgMissLatency': [76206.429780, 76206.429780, 76206.429780, 76206.429780, 76206.429780, 76206.429780,
                               76206.429780, 76206.429780, 76206.429780, 76206.429780, 76206.429780, 76206.429780,
                               76206.429780, 76206.429780, 76206.429780, 76206.429780, 76206.429780, 76206.429780,
                               76206.429780, 76206.429780, 76206.429780, 76206.429780, 76206.429780, 76206.429780,
                               76206.429780, 76206.429780, 76206.429780, 76206.429780],
    'L2cache_Hits': [299, 299, 299, 164, 164, 164, 76, 76, 76, 252, 252, 252, 117, 117, 117, 29, 29, 29, 226, 226,
                     226, 91, 91, 91, 3, 3, 3, 3],
    'L2cache_Misses': [3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468,
                       3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468],
    'L2cache_AvgMissLatency': [169391.580161, 169391.580161, 169391.580161, 169227.797001, 169227.797001,
                               169227.797001, 169389.850058, 169389.850058, 169389.850058, 169488.754325,
                               169488.754325, 169488.754325, 169313.437140, 169313.437140, 169313.437140,
                               169628.604383, 169628.604383, 169628.604383, 169666.666667, 169666.666667,
                               169666.666667, 169117.935409, 169117.935409, 169117.935409, 169158.592849,
                               169158.592849, 169158.592849,169158.592849],

    # 'Icache_size': [32, 64, 128],
    # 'Dcache_size': [64, 128, 256],
    # 'L2cache_size': [1024, 2048, 4096]
}

# Create pandas DataFrames for each part
part1_df = pd.DataFrame(part1_data)
part2_df = pd.DataFrame(part2_data)
part3_df = pd.DataFrame(part3_data)
part4_df = pd.DataFrame(part4_data)

# Add percentage columns and format
part1_df['Hit_Percentage'] = (part1_df['Hits'] / (part1_df['Hits'] + part1_df['Misses'])) * 100

part2_df['Dcache_Hit_Percentage'] = (part2_df['Dcache_Hits'] / (part2_df['Dcache_Hits'] + part2_df['Dcache_Misses'])) * 100
part2_df['Icache_Hit_Percentage'] = (part2_df['Icache_Hits'] / (part2_df['Icache_Hits'] + part2_df['Icache_Misses'])) * 100

part3_df['Hit_Percentage'] = (part3_df['Hits'] / (part3_df['Hits'] + part3_df['Misses'])) * 100

part4_df['Dcache_Hit_Percentage'] = (part4_df['Dcache_Hits'] / (part4_df['Dcache_Hits'] + part4_df['Dcache_Misses'])) * 100
part4_df['Icache_Hit_Percentage'] = (part4_df['Icache_Hits'] / (part4_df['Icache_Hits'] + part4_df['Icache_Misses'])) * 100
part4_df['L2cache_Hit_Percentage'] = (part4_df['L2cache_Hits'] / (part4_df['L2cache_Hits'] + part4_df['L2cache_Misses'])) * 100

# Set formatting for columns
pd.options.display.float_format = '{:,.2f}'.format

# Print the DataFrames
print("Part 1:")
print(part1_df.to_string(index=False))
print("\nPart 2:")
print(part2_df.to_string(index=False))
print("\nPart 3:")
print(part3_df.to_string(index=False))
print("\nPart 4:")
print(part4_df.to_string(index=False))


