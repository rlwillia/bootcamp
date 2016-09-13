"""
Bootcamp Day 2 exercises
"""

#Open sequence file and get trimmed sequence
with open('data/salmonella_spi1_region.fna') as f:
    salm_lines = f.readlines()

salm_lines = salm_lines[1:]

trim_seq = ''

for line in salm_lines:
    trim_seq += line.rstrip()

#Break sequence into blocks and compute gc content

def gc_content(seq):
    """GC content of a given sequence"""
    seq = seq.upper()
    return (seq.count('G') + seq.count('C'))/len(seq)


def gc_blocks(seq, block_size):
    """breaks sequence into blocks returns tuple of gc_content of blocks"""
    start = 0
    blocks_gc = [0,] * int(len(seq)/block_size)
    for i, _ in enumerate(blocks_gc):
        block = seq[start:start + block_size]
        blocks_gc[i] = gc_content(block)
        start += block_size
    blocks_gc = tuple(blocks_gc)
    
    return blocks_gc

#Exercise 2.3B threshold gc content of sequence blocks, puts sequence with GC
#contect above threshold in uppercase

def gc_map(seq, block_size, gc_thresh):
    """returns formatted sequence with blocks of low GC content in lowercase"""
    seq = seq.upper()
    blocks_gc = gc_blocks(seq, block_size)
    block_start = 0
    block_end = block_start + block_size
    mapped_seq = ''
    for i, _ in enumerate(blocks_gc):
        block = seq[block_start:block_end]
        if blocks_gc[i] < gc_thresh:
             block = block.lower()
             mapped_seq += block
        else:
            mapped_seq += block
        block_start += block_size
        block_end += block_size

    return mapped_seq
