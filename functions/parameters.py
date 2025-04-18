class Project_Parameters:
    """
    This class will hold parameters or info that can
    be shared across different scripts on the project.
    """
    data_folder = './data'
    url_dict = {'crime_severity':
                    'https://www150.statcan.gc.ca/n1/tbl/csv/35100026-eng.zip'}
    
    def __init__(self):
        pass