
import pandas as pd
import matplotlib.pyplot as plt
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

part3_data_unified = {
    'Cache': ['Unified L1 cache (Associativity=1)', 'Unified L1 cache (Associativity=2)', 'Unified L1 cache (Associativity=4)',
              'Unified L1 cache (Associativity=8)', 'Unified L1 cache (Associativity=16)', 'Unified L1 cache (Associativity=32)'],
    'Hits': [11798358, 11810614, 11810632, 11810634, 11810636, 11810638],
    'Misses': [15746, 3490, 3472, 3470, 3468, 3466],
    'AvgMissLatency': [72883.525975, 89913.753582, 89985.311060, 90031.988473, 90078.719723, 90125.504905]
}


part3_data_saperate = {
    'Cache': ['L1 data and instruction caches (Associativity=1)', 'L1 data and instruction caches (Associativity=2)',
              'L1 data and instruction caches (Associativity=4)', 'L1 data and instruction caches (Associativity=8)',
              'L1 data and instruction caches (Associativity=16)', 'L1 data and instruction caches (Associativity=32)'],
    'Dcache_Hits': [3312926, 3312982, 3312983, 3312983, 3312983, 3312983],
    'Dcache_Misses': [2341, 2285, 2284, 2284, 2284, 2284],
    'Dcache_AvgMissLatency': [80052.541649, 79097.592998, 79131.786340, 79131.786340, 79131.786340, 79131.786340],
    'Icache_Hits': [8497648, 8497655, 8497655, 8497655, 8497655, 8497655],
    'Icache_Misses': [1189, 1182, 1182, 1182, 1182, 1182],
    'Icache_AvgMissLatency': [75756.097561, 76206.429780, 76206.429780, 76206.429780, 76206.429780, 76206.429780]
}



unified_hit = part3_data_unified["Hits"]
unified_miss = part3_data_unified["Misses"]
unified_AvgMissLatency = part3_data_unified["AvgMissLatency"]

saperate_dhit = part3_data_saperate['Dcache_Hits']
saperate_dmiss = part3_data_saperate['Dcache_Misses']
saperate_dAvgMissLatency = part3_data_saperate['Dcache_AvgMissLatency']

saperate_ihit = part3_data_saperate['Icache_Hits']
saperate_imiss = part3_data_saperate['Icache_Misses']
saperate_iAvgMissLatency = part3_data_saperate['Icache_AvgMissLatency']

associativity = [1, 2, 4, 8, 16, 32]


# Calculation of hit rate
unified_hit_rate = [(unified_hit[i] / (unified_hit[i] + unified_miss[i]) * 100) for i in range(len(unified_hit))]
saperate_dhit_rate = [(saperate_dhit[i] / (saperate_dhit[i] + saperate_dmiss[i]) * 100) for i in range(len(saperate_dhit))]
saperate_ihit_rate = [(saperate_ihit[i] / (saperate_ihit[i] + saperate_imiss[i]) * 100) for i in range(len(saperate_dhit))]

saperate_hit_rate = [saperate_ihit_rate, saperate_dhit_rate]
saperate_AvgMissLatency = [saperate_iAvgMissLatency, saperate_dAvgMissLatency]
# Part 3: Varying associativity
# Plotting for part 3

plt.plot(associativity, unified_hit_rate, marker='o', label='Unified L1Cache')
plt.title('Unified_Cache_size = 256kB')
plt.xlabel(f"Associativity")
plt.ylabel('Hit Rate(%)')
plt.show()

cache_check = ["Icache", "Dcache"]
# Subplot for avg miss latency
plt.figure(figsize=(10, 6))
# Subplot for hit rate
plt.subplot(2, 1, 1)
for cache_type in range(len(cache_check)):
    plt.plot(associativity, saperate_hit_rate[cache_type], marker='o', label=f'{cache_check[cache_type]}')
plt.title('Icache_size = 256kB, Dcache_size = 256KB')
plt.xlabel('Associativity')
plt.ylabel('Hit Rate(%)')
plt.legend()

plt.subplot(2, 1, 2)
for cache_type in range(len(cache_check)):
    plt.plot(associativity, saperate_AvgMissLatency[cache_type], marker='o', label=f'{cache_check[cache_type]}')
plt.title('Icache_size = 256kB, Dcache_size = 256KB')
plt.xlabel('Associativity')
plt.ylabel('Average miss Latency (tick)')
plt.legend()
plt.tight_layout()
plt.show()


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
                      226, 91, 91, 91, 3, 3, 3],
    'L2cache_Misses': [3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468,
                        3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468, 3468],
    'L2cache_AvgMissLatency': [169391.580161, 169391.580161, 169391.580161, 169227.797001, 169227.797001,
                                  169227.797001, 169389.850058, 169389.850058, 169389.850058, 169488.754325,
                                  169488.754325, 169488.754325, 169313.437140, 169313.437140, 169313.437140,
                                  169628.604383, 169628.604383, 169628.604383, 169666.666667, 169666.666667,
                                  169666.666667, 169117.935409, 169117.935409, 169117.935409, 169158.592849,
                                  169158.592849, 169158.592849],

    'Icache_size': [32, 64, 128],
    'Dcache_size': [64, 128, 256],
    'L2cache_size': [1024, 2048, 4096]
}


# Icache_size = 32kB, Dcache_size = 64kB, varying L2cache_size
l2_size_p1 = part4_data["L2cache_size"]
i_hit_p1 = part4_data["Icache_Hits"][:3]
d_hit_p1 = part4_data["Dcache_Hits"][:3]
l2_hit_p1 = part4_data["L2cache_Hits"][:3]

i_miss_p1= part4_data["Icache_Misses"][:3]
d_miss_p1 = part4_data["Dcache_Misses"][:3]
l2_miss_p1 = part4_data["L2cache_Misses"][:3]

i_miss_latency_p1 = part4_data["Icache_AvgMissLatency"][:3]
d_miss_latency_p1 = part4_data["Dcache_AvgMissLatency"][:3]
l2_miss_latency_p1 = part4_data["L2cache_AvgMissLatency"][:3]


# Calculation of hit rate
i_hitrate_p1 = [(i_hit_p1[i] / (i_hit_p1[i] + i_miss_p1[i]) * 100) for i in range(len(l2_size_p1))]
d_hitrate_p1 = [(d_hit_p1[i] / (d_hit_p1[i] + d_miss_p1[i]) * 100) for i in range(len(l2_size_p1))]
l2_hitrate_p1 = [(l2_hit_p1[i] / (l2_hit_p1[i] + l2_miss_p1[i]) * 100) for i in range(len(l2_size_p1))]

# f1 = [f11, f12, f13]
# f2 = [y31, y32, y33]



# Icache_size = 32kB, L2cache_size = 1024kB, varying Dcache_size
d_size_p2 = part4_data["Dcache_size"]
i_hit_p2 = part4_data["Icache_Hits"][:8:3]
d_hit_p2 = part4_data["Dcache_Hits"][:8:3]
l2_hit_p2 = part4_data["L2cache_Hits"][:8:3]

i_miss_p2= part4_data["Icache_Misses"][:8:3]
d_miss_p2 = part4_data["Dcache_Misses"][:8:3]
l2_miss_p2 = part4_data["L2cache_Misses"][:8:3]

i_miss_latency_p2 = part4_data["Icache_AvgMissLatency"][:8:3]
d_miss_latency_p2 = part4_data["Dcache_AvgMissLatency"][:8:3]
l2_miss_latency_p2 = part4_data["L2cache_AvgMissLatency"][:8:3]


# Calculation of hit rate
i_hitrate_p2 = [((i_hit_p2[i] / (i_hit_p2[i] + i_miss_p2[i])) * 100) for i in range(len(d_size_p2))]
d_hitrate_p2 = [((d_hit_p2[i] / (d_hit_p2[i] + d_miss_p2[i])) * 100) for i in range(len(d_size_p2))]
l2_hitrate_p2 = [((l2_hit_p2[i] / (l2_hit_p2[i] + l2_miss_p2[i])) * 100) for i in range(len(d_size_p2))]



# Dcache_size = 64kB, L2cache_size = 4096kB, varying Icache_size
i_size_p3 = part4_data["Icache_size"]
i_hit_p3 = part4_data["Icache_Hits"][:26:9]
d_hit_p3 = part4_data["Dcache_Hits"][:26:9]
l2_hit_p3 = part4_data["L2cache_Hits"][:26:9]

i_miss_p3= part4_data["Icache_Misses"][:26:9]
d_miss_p3 = part4_data["Dcache_Misses"][:26:9]
l2_miss_p3 = part4_data["L2cache_Misses"][:26:9]

i_miss_latency_p3 = part4_data["Icache_AvgMissLatency"][:26:9]
d_miss_latency_p3 = part4_data["Dcache_AvgMissLatency"][:26:9]
l2_miss_latency_p3 = part4_data["L2cache_AvgMissLatency"][:26:9]

# Calculation of hit rate
i_hitrate_p3 = [(i_hit_p3[i] / (i_hit_p3[i] + i_miss_p3[i]) * 100) for i in range(len(i_size_p3))]
d_hitrate_p3 = [(d_hit_p3[i] / (d_hit_p3[i] + d_miss_p3[i]) * 100) for i in range(len(i_size_p3))]
l2_hitrate_p3 = [(l2_hit_p3[i] / (l2_hit_p3[i] + l2_miss_p3[i]) * 100) for i in range(len(i_size_p3))]


cache_size = [l2_size_p1, d_size_p2, i_size_p3]

i_hitrate = [i_hitrate_p1, i_hitrate_p2, i_hitrate_p3]
d_hitrate = [d_hitrate_p1, d_hitrate_p2, d_hitrate_p3]
l2_hitrate = [l2_hitrate_p1, l2_hitrate_p2, l2_hitrate_p3]
hit_rate = [i_hitrate, d_hitrate, l2_hitrate]

i_miss_latency = [i_miss_latency_p1, i_miss_latency_p2, i_miss_latency_p3]
d_miss_latency = [d_miss_latency_p1, d_miss_latency_p2, d_miss_latency_p3]
l2_miss_latency = [l2_miss_latency_p1, l2_miss_latency_p2, l2_miss_latency_p3]
avg_miss_latency = [i_miss_latency, d_miss_latency, l2_miss_latency]
cache_name = ["ICache", "DCache", "L2Cache"]

# Plotting for part 4
for plot in range(3):
    plt.figure(figsize=(10, 6))
    # Subplot for hit rate
    plt.subplot(2, 1, 1)
    for cache_type in range(len(cache_size)):
        # print(cache_size[plot], hit_rate[cache_type][plot])
        plt.plot(cache_size[plot], hit_rate[cache_type][plot], marker='o', label=f'{cache_name[cache_type]}')
    plt.title(f'Varying {cache_name[2-plot]}_size')
    plt.xlabel(f'{cache_name[2-plot]} size (kB)')
    plt.legend()
    plt.ylabel('Cache hit rate (%)')

    # Subplot for avg miss latency
    plt.subplot(2, 1, 2)
    for cache_type  in range(len(cache_size)):
        plt.plot(cache_size[plot], avg_miss_latency[cache_type][plot], marker='o', label=f'{cache_name[cache_type]}')
    plt.xlabel(f'{cache_name[2-plot]} size (kB)')
    plt.ylabel('Average miss Latency (tick)')
    plt.legend()
    plt.tight_layout()
    plt.show()













