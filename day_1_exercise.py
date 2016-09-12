def complement_base(base, material= 'material'):
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

def reverse_complement(seq, material= 'DNA'):
    """Compute reverse complement of a DNA sequence."""

    #initialize empty string
    rev_comp = ''

    #loop through and add new rev comp bases
    for i in range(len(seq)):
        rev_comp += seq[-(i+1)]
    return rev_comp
