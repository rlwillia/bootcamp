def ratio(x,y):
    """The ratio of 'x' to 'y',"""
    return x/y

def answer_to_everything():
    """Simple Program"""
    return 42

def complement_base(base, material='DNA'):
    """Return the Watson-Crick complement of a base"""

    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
    elif base in 'Tt':
        return 'A'
    elif base in 'Gg':
        return 'C'
    elif base in 'Cc':
        return 'G'
    else:
         return 'X'

def reverse_complement(seq, material='material'):
    """Compute reverse complement of a DNA sequence."""

    #initialize empty string
    rev_comp = ''

    #loop through and add new rev comp bases
    for base in reversed(seq):
        rev_comp += complement_base(base)
    return rev_comp
