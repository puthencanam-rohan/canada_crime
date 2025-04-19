def save_pandas_data_to_parquet(params):
    import os
    import os.path
    import pandas as pd
    

    status = {'status': 'False', 'value': None}
    output_path = params.get('output_path', None)
    data_df = params.get('input_dataframe', None)

    data_df.to_parquet(output_path)
    
    status.update({'status': 'True', 'value': data_df})
    return status