# Lai A., 2024.

import sys, csv, re

codes = [{"code":"39452","system":"prod"},{"code":"5848","system":"prod"},{"code":"9281","system":"prod"},{"code":"7011","system":"prod"},{"code":"6305","system":"prod"},{"code":"11075","system":"prod"},{"code":"39276","system":"prod"},{"code":"4080100","system":"prod"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chemotherapy-medication-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["valproic-chemotherapy-medication---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["valproic-chemotherapy-medication---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["valproic-chemotherapy-medication---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
