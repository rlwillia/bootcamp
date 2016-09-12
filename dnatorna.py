"""
Convert DNA sequence to RNA
"""

def rna(seq):
    """
    Convert a DNA sequence to RNA.
    """

    #Convert sequence to uppercase
    seq = seq.upper()

    return seq.replace('T', 'U')
    
