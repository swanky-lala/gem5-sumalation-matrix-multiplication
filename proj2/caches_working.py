import m5
from m5.objects import Cache

# Add the common scripts to our path
m5.util.addToPath("../../../configs/")

from common import SimpleOpts

# Some specific options for caches
# For all options see src/mem/cache/BaseCache.py


class L1Cache(Cache):
    # Set the default size
    size = "64kB"
    """Simple L1 Cache with default values"""
    tag_latency = 1
    data_latency = 1
    response_latency = 20
    assoc = 2
    mshrs = 4
    tgts_per_mshr = 20
    # SimpleOpts.add_option(
    #     "--l1_size", help=f"L1 instruction cache size. Default: {size}"
    # )
    # SimpleOpts.add_option(
    #     "--l1_assoc", help=f"L1 instruction cache size. Default: {size}"
    # )
    def __init__(self, opts=None):
        super(L1Cache, self).__init__()
        if not opts or not opts.l1_size or not opts.l1_assoc:
            return
        self.size = opts.l1_size
        self.assoc = opts.l1_assoc
        pass
    def connectBus(self, bus):
        """Connect this cache to a memory-side bus"""
        self.mem_side = bus.cpu_side_ports

    def connectCPU(self, cpu):
        """Connect this cache's port to a CPU-side port
        This must be defined in a subclass"""
        raise NotImplementedError


class L1ICache(L1Cache):
    """Simple L1 instruction cache with default values"""
    # Set the default size
    size = "64kB"

    # SimpleOpts.add_option(
    #     "--l1i_size", help=f"L1 instruction cache size. Default: {size}"
    # )
    # SimpleOpts.add_option(
    #     "--l1i_assoc", help=f"L1 instruction cache size. Default: {size}"
    # )

    def __init__(self, opts=None):
        super(L1ICache, self).__init__(opts)
        if not opts or not opts.l1i_size or not opts.l1i_assoc:
            return
        self.size = opts.l1i_size
        self.assoc = opts.l1i_assoc

    def connectCPU(self, cpu):
        """Connect this cache's port to a CPU icache port"""
        self.cpu_side = cpu.icache_port


class L1DCache(L1Cache):
    """Simple L1 data cache with default values"""

    # Set the default size
    size = "128kB"

    # SimpleOpts.add_option(
    #     "--l1d_size", help=f"L1 data cache size. Default: {size}"
    # )
    # SimpleOpts.add_option(
    #     "--l1d_assoc", help=f"L1 data cache size. Default: {size}"
    # )

    def __init__(self, opts=None):
        super(L1DCache, self).__init__(opts)
        if not opts or not opts.l1d_size or not opts.l1d_assoc:
            return
        self.size = opts.l1d_size
        self.assoc = opts.l1d_assoc

    def connectCPU(self, cpu):
        """Connect this cache's port to a CPU dcache port"""
        self.cpu_side = cpu.dcache_port


class L2Cache(Cache):
    """Simple L2 Cache with default values"""
    tag_latency = 10
    data_latency = 10
    response_latency = 100

    # Default parameters
    size = "2MB"
    assoc = 4
    mshrs = 20
    tgts_per_mshr = 12

    # SimpleOpts.add_option("--l2_size", help=f"L2 cache size. Default: {size}")
    # SimpleOpts.add_option("--l2_assoc", help=f"L2 cache size. Default: {size}")

    def __init__(self, opts=None):
        super(L2Cache, self).__init__()
        if not opts or not opts.l2_size or not opts.l2_assoc:
            return
        self.size = opts.l2_size
        self.assoc = opts.l2_assoc

    def connectCPUSideBus(self, bus):
        self.cpu_side = bus.mem_side_ports

    def connectMemSideBus(self, bus):
        self.mem_side = bus.cpu_side_ports
