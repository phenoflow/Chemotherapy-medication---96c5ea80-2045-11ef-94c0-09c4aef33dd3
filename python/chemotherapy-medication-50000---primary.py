# Lai A., 2024.

import sys, csv, re

codes = [{"code":"23122","system":"prod"},{"code":"38435","system":"prod"},{"code":"22332","system":"prod"},{"code":"15790","system":"prod"},{"code":"22505","system":"prod"},{"code":"26314","system":"prod"},{"code":"21070","system":"prod"},{"code":"21476","system":"prod"},{"code":"24580","system":"prod"},{"code":"28797","system":"prod"},{"code":"11881","system":"prod"},{"code":"18485","system":"prod"},{"code":"14136","system":"prod"},{"code":"13116","system":"prod"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chemotherapy-medication-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["chemotherapy-medication-50000---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["chemotherapy-medication-50000---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["chemotherapy-medication-50000---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
