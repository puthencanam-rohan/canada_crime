def read_downloaded_data(params):
    import zipfile
    import os
    import os.path
    import pandas as pd
    

    status = {'status': 'False', 'value': None}
    filename = params.get('filename', None)
    is_zipped = params.get('is_zipped', True)
    project_parameters = params.get('project_parameters', None)
    data_folder = project_parameters.data_folder
    compression = None
    _filename = f'{data_folder}/{filename}'
    
    if is_zipped:
        _csv_file = (os.path.basename(_filename)
                     .split('.')[0]
                     .replace('eng', '')
                     .replace('-', '')
                     + '.csv')
        with zipfile.ZipFile(_filename) as zf:
            df = pd.read_csv(zf.open(_csv_file, 'r'),low_memory=False)
    else:
        df = pd.read_csv(_filename)

    status.update({'status': 'True', 'value': df})
    return status

def prepare_incidents_data(params_ivd):
    status = {'status': False,
              'value' : None
             }
    param_df_ivd = params_ivd.get('dataframe',None)
    param_val_ivd = params_ivd.get('statistics_values_of_interest',['Actual incidents'])
    param_select_ivd = params_ivd.get('columns_of_interest',[
    'REF_DATE',
    'GEO',
    'Statistics',
    'VALUE'
])

    param_clean_ivd = params_ivd.get('clean_function_dict',{'Statistics':
                                                            lambda x: x.replace(' ', '_').lower()
                                                            })
    
    df_ivd = param_df_ivd[param_select_ivd]
    #print("Before data preparation...")
    display(df_ivd.head(10))
    pdf_ivd = param_df_ivd[param_df_ivd.Statistics.isin(param_val_ivd)]
    for a_key in param_clean_ivd.keys():
        pdf_ivd = param_df_ivd[param_df_ivd.Statistics.isin(param_val_ivd)].copy()


    pdf_ivd = (pdf_ivd
           .pivot_table('VALUE', ['REF_DATE', 'GEO'], 'Statistics')
           .reset_index()
    )
    pdf_ivd = pdf_ivd.rename(columns={a_col: a_col.lower() for a_col in pdf_ivd.columns})
    print("After data preparation...")
    display(pdf_ivd.head(50))

    status.update({'status': 'True', 'value': pdf_ivd})
    return status
    