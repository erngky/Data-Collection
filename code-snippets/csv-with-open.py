import pandas as pd
import numpy as np
import csv



with open("names.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file) #DictReader da kullanılabilir <=
    

    with open("new_names.csv", "w") as new_file:
        csv_writer = csv.writer(new_file)
        
        for line in csv_reader:
            csv_writer.writerow(line)
            print(line)


    # with open("new-names.csv", 'w') as new_file:
    #     csv_writer = csv.writer(new_file, delimiter= "\t")

    #     for line in csv_reader:
    #         csv_writer.writerow(line)
   
        
df = pd.read_csv("new_names.csv")
print(df)

#pandas kütüphanesi csv okurken \t kabul etmedi!

    