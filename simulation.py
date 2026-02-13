# --- IMAGINARY LOGIC GATE SIMULATION ---
# Based on research by Pearl Bipin Pulickal

class ImaginaryLogic:
    """
    Implements a Quad-State logic system:
    1: High, 0: Neutral, -1: Low, 'i': Imaginary
    """
    
    STATES = [1, 0, -1, 'i']

    @staticmethod
    def i_not(a):
        """Negation logic including the imaginary unit."""
        if a == 1: return -1
        if a == -1: return 1
        if a == 0: return 0
        if a == 'i': return 'i' # Imaginary state is its own complement in this framework
        return None

    @staticmethod
    def i_nand(a, b):
        """
        Universal Imaginary NAND Gate logic as derived in the research.
        """
        # Rule 1: Output is High (1) if any input is Low (-1)
        if a == -1 or b == -1:
            return 1
            
        # Rule 2: Output is Neutral (0) if any input is Neutral (0)
        if a == 0 or b == 0:
            return 0
            
        # Rule 3: Output is Imaginary ('i') if BOTH inputs are Imaginary ('i')
        if a == 'i' and b == 'i':
            return 'i'
            
        # Rule 4: Output is Low (-1) if both are High (1), 
        # or if one is High (1) and the other is Imaginary ('i')
        if (a == 1 or a == 'i') and (b == 1 or b == 'i'):
            return -1
            
        return 0

def run_truth_table():
    """Generates and displays the quad-state truth table for the Imaginary NAND gate."""
    logic = ImaginaryLogic()
    
    print("--- Universal Imaginary NAND Truth Table ---")
    print(f"{'Input A':<10} | {'Input B':<10} | {'Output':<10}")
    print("-" * 35)
    
    for a in logic.STATES:
        for b in logic.STATES:
            result = logic.i_nand(a, b)
            print(f"{str(a):<10} | {str(b):<10} | {str(result):<10}")

if __name__ == "__main__":
    run_truth_table()
