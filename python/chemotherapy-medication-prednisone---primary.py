# Lai A., 2024.

import sys, csv, re

codes = [{"code":"34748","system":"prod"},{"code":"578","system":"prod"},{"code":"9727","system":"prod"},{"code":"31327","system":"prod"},{"code":"28375","system":"prod"},{"code":"2704","system":"prod"},{"code":"28376","system":"prod"},{"code":"34452","system":"prod"},{"code":"34978","system":"prod"},{"code":"34404","system":"prod"},{"code":"2368","system":"prod"},{"code":"557","system":"prod"},{"code":"34914","system":"prod"},{"code":"3557","system":"prod"},{"code":"8306","system":"prod"},{"code":"34660","system":"prod"},{"code":"34461","system":"prod"},{"code":"41745","system":"prod"},{"code":"05011000/08020200/10020100/06030200/01050200","system":"prod"},{"code":"6030200","system":"prod"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chemotherapy-medication-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["chemotherapy-medication-prednisone---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["chemotherapy-medication-prednisone---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["chemotherapy-medication-prednisone---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
