# import csv
# import json

# x_label, y_label = [], []
# body = []

# with open("./data/data.csv") as f:
#     render = csv.reader(f)
#     body = [list(row) for row in render]
        
        
# with open("./data/x_label.csv") as f:
#     render = csv.reader(f)
#     x_label = [list(row) for row in render]
        
        
# with open("./data/y_label.csv") as f:
#     render = csv.reader(f)
#     y_label = [list(row) for row in render]
        
        
        
# json_strategy = {
#     "x_label": x_label,
#     "y_label": y_label,
#     "body": body
# }

# with open("./data/output_statics.json", mode="w") as f:
#     f.write(json.dumps(json_strategy, ensure_ascii=False))
