import numpy as np

def add_patch(big, small, x,y):
	br, bc = big.shape
	sr,sc = small.shape
	result = big.copy()
	result[x:x+sr, y:y+sc] += small
	
	return result


def reconstruct_from_noisy_patches(input_dict, shape):
 
    M = np.zeros(shape)
    black_count = np.zeros(shape)
    white_count = np.zeros(shape)
    mid_count = np.zeros(shape)
    mid_total = np.zeros(shape)


    for topleft_row, topleft_col, bottomright_row, bottomright_col in input_dict:
        tlr, tlc, brr, brc = topleft_row, topleft_col, bottomright_row, bottomright_col
        patch = input_dict[(tlr, tlc, brr, brc)]
        
        bc = patch.copy()
        bc[patch==0] =1
        bc[patch!=0] =0
        black_count = add_patch(black_count, bc, tlr, tlc)

        wc = patch.copy()
        wc[patch==255] =1
        wc[patch!=255] =0
        white_count = add_patch(white_count, wc, tlr, tlc)        

        mc = patch.copy()
        
        mc[(patch!=0) & (patch!=255)] =1
        mc[(patch==0) ^ (patch==255)] =0
        mid_count = add_patch(mid_count, mc, tlr, tlc)

        mt = patch.copy()
        mt[(patch==0) ^ (patch==255)] =0
        mid_total = add_patch(mid_total, mt, tlr, tlc)


    
    M[(mid_count==0) & (black_count<=white_count)]= 255
    M[(mid_count==0) & (black_count>white_count)] = 0
    M[mid_count!=0] = np.around(mid_total[mid_count!=0]/mid_count[mid_count!=0])

    M[(mid_count==0) & (white_count==0) & (black_count==0)]= 0
    

    
    return M 