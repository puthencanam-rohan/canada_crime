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