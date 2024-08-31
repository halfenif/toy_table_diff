from datetime import datetime

def get_date_filename(pathname, categoryname, extname):
    return f"{pathname}/{categoryname}_{datetime.now().strftime("%Y-%m-%d_%H%M%S")}.{extname}"