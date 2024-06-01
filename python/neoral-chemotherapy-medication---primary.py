# Lai A., 2024.

import sys, csv, re

codes = [{"code":"29948","system":"prod"},{"code":"1626","system":"prod"},{"code":"13105","system":"prod"},{"code":"973","system":"prod"},{"code":"2620","system":"prod"},{"code":"24494","system":"prod"},{"code":"16575","system":"prod"},{"code":"10435","system":"prod"},{"code":"972","system":"prod"},{"code":"16137","system":"prod"},{"code":"38080","system":"prod"},{"code":"1905","system":"prod"},{"code":"34039","system":"prod"},{"code":"6482","system":"prod"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chemotherapy-medication-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["neoral-chemotherapy-medication---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["neoral-chemotherapy-medication---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["neoral-chemotherapy-medication---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
