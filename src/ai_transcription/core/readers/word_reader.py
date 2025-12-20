def write_excel(df, output_path: str):
    df.to_excel(output_path, index=False)
