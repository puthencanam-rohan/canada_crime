def read_crime_severity_data(params):
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
            df = pd.read_csv(zf.open(_csv_file, 'r'))
    else:
        df = pd.read_csv(_filename)

    status.update({'status': 'True', 'value': df})
    return status


def prepare_crime_severity_data(params):
    import pandas as pd
    

    status = {'status': 'False', 'value': None}
    df = params.get('dataframe', None)
    #project_parameters = params.get('project_parameters', None)
    values_of_interest = params.get('values_of_interest', ['Crime severity index'])
    select_columns = params.get('select_columns', [
                                                'REF_DATE',
                                                'GEO',
                                                'Statistics',
                                                'VALUE'
                                                ]
                               )
    clean_function_dict = params.get('clean_function_dict', {'Statistics':
                                                            lambda x: x.replace(' ', '_').lower()
                                                            })

    pdf = df[select_columns]
    print("Before data preparation...")
    display(pdf.head(10))
    pdf = df[df.Statistics.isin(values_of_interest)]
    
    for a_key in clean_function_dict.keys():
        pdf[a_key] = pdf[a_key].apply(clean_function_dict.get(a_key))

    pdf = (pdf
           .pivot_table('VALUE', ['REF_DATE', 'GEO'], 'Statistics')
           .reset_index()
    )
    pdf = pdf.rename(columns={a_col: a_col.lower() for a_col in pdf.columns})
    print("After data preparation...")
    display(pdf.head(50))

    status.update({'status': 'True', 'value': pdf})
    return status