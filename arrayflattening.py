def flatten_array(nested_array):
    flattened = []
    
    for element in nested_array:
        try:
            for item in element:
                flattened.extend(flatten_array([item])) 
        except TypeError:
            flattened.append(element)
            
    return flattened