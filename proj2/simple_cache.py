# import the m5 (gem5) library created when gem5 is built
import m5

# import all of the SimObjects
from m5.objects import *
from caches_working import *

import argparse

parser = argparse.ArgumentParser(description='A simple system with 2-level cache.')
parser.add_argument("--part1",
                    help=f"Simulate a simple l1 cache for both data and instruction (True)")
parser.add_argument("--part2",
                    help=f"Simulate separate l1 instruction and data caches ")
parser.add_argument("--part4",
                    help=f"Simulate separate l1 instruction and data caches and a unified l2")

parser.add_argument("--l1_assoc",
                    help=f"L1 cache associativity. Default: 2.")
parser.add_argument("--l1i_assoc",
                    help=f"L1 instruction associativity. Default: 2.")
parser.add_argument("--l1d_assoc",
                    help="L1 data associativity. Default: Default: 2.")
parser.add_argument("--l2_assoc",
                    help="L2 associativity. Default: 2.")

parser.add_argument("--l1_size",
                    help=f"L1 cache size. Default: 16kB.")
parser.add_argument("--l1i_size",
                    help=f"L1 instruction cache size. Default: 16kB.")
parser.add_argument("--l1d_size",
                    help="L1 data cache size. Default: Default: 64kB.")
parser.add_argument("--l2_size",
                    help="L2 cache size. Default: 256kB.")

options = parser.parse_args()
# print(f"part4: {options.part4}")
# print(options)

# create the system we are going to simulate
system = System()

# Set the clock frequency of the system (and all of its children)
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = "1GHz"
system.clk_domain.voltage_domain = VoltageDomain()

# Set up the system
system.mem_mode = "timing"  # Use timing accesses
system.mem_ranges = [AddrRange("4GB")]  # Create an address range

# Create a simple CPU
system.cpu = X86TimingSimpleCPU()

if (options.part1 == 'True'):
    system.cpu.l1cache = L1Cache(options)
    print(f"L1 Size: {system.cpu.l1cache.size}, Associativity: {system.cpu.l1cache.assoc}")

    #create a bus to connect the I and D cache ports of the CPU to a unified l1 cache
    system.l1bus = SystemXBar()
    system.cpu.icache_port = system.l1bus.cpu_side_ports
    system.cpu.dcache_port = system.l1bus.cpu_side_ports

    #Connect l1 to bus between cpu and l1
    system.cpu.l1cache.cpu_side = system.l1bus.mem_side_ports

    # Connect to membus
    system.membus = SystemXBar()
    system.cpu.l1cache.mem_side = system.membus.cpu_side_ports

elif (options.part2 == 'True'):
    # Create L1 Caches
    system.cpu.icache = L1ICache(options)
    print(f"L1I Size: {system.cpu.icache.size}, Associativity: {system.cpu.icache.assoc}")
    system.cpu.dcache = L1DCache(options)
    print(f"L1D Size: {system.cpu.dcache.size}, Associativity: {system.cpu.dcache.assoc}")

    # Connect the I and D cache ports of the CPU to the memobj.
    # Since cpu_side is a vector port, each time one of these is connected, it will
    # create a new instance of the CPUSidePort class
    system.cpu.icache.connectCPU(system.cpu)
    system.cpu.dcache.connectCPU(system.cpu)

    # Create a memory bus, a coherent crossbar, in this case
    system.membus = SystemXBar()

    # Hook the L1 caches up to the memory bus
    system.cpu.icache.connectBus(system.membus)
    system.cpu.dcache.connectBus(system.membus)

elif (options.part4 == 'True'):
    # Create L1 Caches
    system.cpu.icache = L1ICache(options)
    print(f"L1I Size: {system.cpu.icache.size}, Associativity: {system.cpu.icache.assoc}")
    system.cpu.dcache = L1DCache(options)
    print(f"L1D Size: {system.cpu.dcache.size}, Associativity: {system.cpu.dcache.assoc}")

    # Connect the I and D cache ports of the CPU to the memobj.
    # Since cpu_side is a vector port, each time one of these is connected, it will
    # create a new instance of the CPUSidePort class
    system.cpu.icache.connectCPU(system.cpu)
    system.cpu.dcache.connectCPU(system.cpu)

    # Create L2 bus to connect L1 caches to L2
    system.l2bus = L2XBar()
    system.cpu.icache.connectBus(system.l2bus)
    system.cpu.dcache.connectBus(system.l2bus)

    # Create L2 cache
    system.l2cache = L2Cache(options)
    print(f"L2 Size: {system.l2cache.size}, Associativity: {system.l2cache.assoc}")
    system.l2cache.connectCPUSideBus(system.l2bus)
    # Create a memory bus, a coherent crossbar, in this case
    system.membus = SystemXBar()

    # Hook the L2 cache up to the memory bus
    system.l2cache.connectMemSideBus(system.membus)



# create the interrupt controller for the CPU and connect to the membus
system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

# Connect the system up to the membus
system.system_port = system.membus.cpu_side_ports

# Create a DDR3 memory controller and connect it to the membus
system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

# Create a process for a simple "Hello World" application
process = Process()
# Set the command
# grab the specific path to the binary
thispath = os.path.dirname(os.path.realpath(__file__))
binpath = os.path.join(
    thispath, "../../../", "src/learning_gem5/proj2/mat-mult.out"
)
# cmd is a list which begins with the executable (like argv)
process.cmd = [binpath, 4,4,4,4]
# Set the cpu to use the process as its workload and create thread contexts
system.cpu.workload = process
system.cpu.createThreads()

system.workload = SEWorkload.init_compatible(binpath)

# set up the root SimObject and start the simulation
root = Root(full_system=False, system=system)
# instantiate all of the objects we've created above
m5.instantiate()

print(f"Beginning simulation!")
exit_event = m5.simulate()
print(f"Exiting @ tick {m5.curTick()} because {exit_event.getCause()}")
