#Part 1
echo "Part1: Unified L1 cache" > src/learning_gem5/proj2/filtered_output_p1.txt
build/X86/gem5.opt src/learning_gem5/proj2/simple_cache.py --part1='True' --l1_size='256kB' --l1_assoc='2'
grep -E "system\.cpu\.(l1|i|d|l2)cache\.overall(Hits|Misses|AvgMissLatency)::total" m5out/stats.txt >> src/learning_gem5/proj2/filtered_output_p1.txt

#Part 2
echo "Part2: L1 data and instruction caches" > src/learning_gem5/proj2/filtered_output_p2.txt
build/X86/gem5.opt src/learning_gem5/proj2/simple_cache.py --part2='True' --l1i_size='256kB' --l1d_size='256kB' --l1i_assoc='2' --l1d_assoc='2'
grep -E "system\.cpu\.(l1|i|d|l2)cache\.overall(Hits|Misses|AvgMissLatency)::total" m5out/stats.txt >> src/learning_gem5/proj2/filtered_output_p2.txt

#Part 3
assocArr=('1' '2' '4' '8' '16' '32')
echo "Part3: Varying associativity" > src/learning_gem5/proj2/filtered_output_p3.txt
echo "Unified L1 cache" >> src/learning_gem5/proj2/filtered_output_p3.txt
for str in ${assocArr[@]}; do
    echo " " >> src/learning_gem5/proj2/filtered_output_p3.txt
    echo "-----Associativity=${str}--------" >> src/learning_gem5/proj2/filtered_output_p3.txt
    build/X86/gem5.opt src/learning_gem5/proj2/simple_cache.py --part1='True' --l1_size='256kB' --l1_assoc=${str}
    grep -E "system\.cpu\.(l1|i|d|l2)cache\.overall(Hits|Misses|AvgMissLatency)::total" m5out/stats.txt >> src/learning_gem5/proj2/filtered_output_p3.txt
done
echo "L1 data and instruction caches" >> src/learning_gem5/proj2/filtered_output_p3.txt
for str in ${assocArr[@]}; do
    echo " " >> src/learning_gem5/proj2/filtered_output_p3.txt
    echo "-----Associativity=${str}--------" >> src/learning_gem5/proj2/filtered_output_p3.txt
    build/X86/gem5.opt src/learning_gem5/proj2/simple_cache.py --part2='True' --l1i_size='256kB' --l1d_size='256kB' --l1i_assoc=${str} --l1d_assoc=${str}
    grep -E "system\.cpu\.(l1|i|d|l2)cache\.overall(Hits|Misses|AvgMissLatency)::total" m5out/stats.txt >> src/learning_gem5/proj2/filtered_output_p3.txt
done

#Part 4
x=('32kB' '64kB' '128kB')
y=('64kB' '128kB' '256kB')
z=('1MB' '2MB' '4MB')
echo "Part4: L1 data and instruction caches with unified L2 cache, varying cache size" > src/learning_gem5/proj2/filtered_output_p4.txt
for str1 in ${x[@]}; do
    for str2 in ${y[@]}; do
        for str3 in ${z[@]}; do
            echo " " >> src/learning_gem5/proj2/filtered_output_p4.txt
            echo "-----Size=(l1i_size=${str1}, l1d_size=${str2}, l2_size=${str3})--------" >> src/learning_gem5/proj2/filtered_output_p4.txt
            build/X86/gem5.opt src/learning_gem5/proj2/simple_cache.py --part4='True' --l1i_size=${str1} --l1d_size=${str2} --l2_size=${str3} --l1i_assoc='2' --l1d_assoc='2' --l2_assoc='4'
            grep -E "system\.(cpu\.(l1|i|d)|l2)cache\.overall(Hits|Misses|AvgMissLatency)::total" m5out/stats.txt >> src/learning_gem5/proj2/filtered_output_p4.txt
        done
    done
done
