'''
Problem Statement:
An automobile company manufactures both two-wheelers (TW) and
four-wheelers (FW). A company manager wants to determine
production quantities based on:
Total number of vehicles (V) = TW + FW
Total number of wheels (W)
Calculate how many two-wheelers and four-wheelers need to be
manufactured.
'''

def calculate_vehicles(V, W):
    # Calculate the number of four-wheelers (FW)
    FW = (W - 2 * V) // 2
    
    # Calculate the number of two-wheelers (TW)
    TW = V - FW
    
    return TW, FW