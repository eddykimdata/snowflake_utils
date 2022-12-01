import re

def replace_sql_variables(query):
    """
    This function replaces SQL variable names with the value.  Comments out the SET command.  
    Snowflake variables must start with '$' 
    """
    # Detect variable names
    variables_dict = {}
    pattern = re.compile(r"^SET\s([a-zA-Z0-9_]+)\s=\s([a-zA-Z0-9_'\-]+);$", flags=re.IGNORECASE|re.MULTILINE)

    matches = re.findall(pattern, query)
    for variable_name, value in matches:
        query = query.replace(f"${variable_name}", value)
        
    # Comment out all lines that start with SET 
    pattern_startset = re.compile(r"^SET", flags=re.IGNORECASE|re.MULTILINE)
    query = re.sub(pattern_startset, "--SET", query)

    return query