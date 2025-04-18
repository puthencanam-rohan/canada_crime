def download_statcan_data(params):
    """
    This function downloads 
    """
    import urllib.request
    import zipfile
    import os
    import os.path
    import ssl
    
    status = {'status': 'False', 'value': None}
    project_parameters = params.get('project_parameters', None)
    data_key = params.get('data_key', None)

    # For SSL errors
    ssl._create_default_https_context = ssl._create_unverified_context

    data_folder = project_parameters.data_folder
    crime_severity_url = project_parameters.url_dict[data_key]
    zipfilename = os.path.basename(crime_severity_url)
    #print(zipfilename)

    # Save zipfile in downloads folder
    with (urllib.request.urlopen(crime_severity_url) as testfile,
        open(f'{data_folder}/{zipfilename}', 'wb') as zf):
        zf.write(testfile.read())
        
    status.update({'status': 'True', 'zipfilename': zipfilename})
    return status