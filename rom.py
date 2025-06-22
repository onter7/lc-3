import pandas as pd

def write_logisim_hex(input_excel, output_hex):
    df = pd.read_excel(input_excel)

    # Drop the 'State' column if it exists
    df = df.drop(columns=["State"], errors='ignore')

    # Replace empty cells with 0 and cast all to int
    df = df.fillna(0).astype(int)

    with open(output_hex, "w") as f:
        for i, row in df.iterrows():
            bits = ''.join(row.astype(str).tolist())

            if len(bits) != 52:
                raise ValueError(f"Row {i} does not have exactly 52 bits: {len(bits)} bits found.")

            hex_str = hex(int(bits, 2))[2:].zfill(13)  # 52 bits = 13 hex digits
            f.write(hex_str + '\n')

write_logisim_hex("lc3_states.xlsx", "microcode.hex")
