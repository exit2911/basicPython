#pop method will yield a list empty after all elements are taken

unprinted_designs = ["iphone case","robot pendant","dodecahedron"] 


completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
 
    
    print("printing model: " + current_design)
    
    completed_models.append(current_design)
    
    
for completed_model in completed_models:
    print(completed_models)
    
