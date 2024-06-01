# Lai A., 2024.

import sys, csv, re

codes = [{"code":"27642","system":"prod"},{"code":"32229","system":"prod"},{"code":"16540","system":"prod"},{"code":"877","system":"prod"},{"code":"7337","system":"prod"},{"code":"40281","system":"prod"},{"code":"32865","system":"prod"},{"code":"18890","system":"prod"},{"code":"40371","system":"prod"},{"code":"17672","system":"prod"},{"code":"08010300/23000000","system":"prod"},{"code":"08010300/10010300/01050300/23000000/13050300","system":"prod"},{"code":"08010300/10010300/01050300/13050300","system":"prod"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chemotherapy-medication-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["chemotherapy-medication-methotrexate---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["chemotherapy-medication-methotrexate---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["chemotherapy-medication-methotrexate---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
