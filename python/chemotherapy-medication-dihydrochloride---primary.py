# Lai A., 2024.

import sys, csv, re

codes = [{"code":"39387","system":"prod"},{"code":"40251","system":"prod"},{"code":"9686","system":"prod"},{"code":"3490","system":"prod"},{"code":"19402","system":"prod"},{"code":"595","system":"prod"},{"code":"29652","system":"prod"},{"code":"13600","system":"prod"},{"code":"12707","system":"prod"},{"code":"5010703","system":"prod"},{"code":"04020100/01020100","system":"prod"},{"code":"04020100/04030100","system":"prod"},{"code":"4020100","system":"prod"},{"code":"8010514","system":"prod"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chemotherapy-medication-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["chemotherapy-medication-dihydrochloride---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["chemotherapy-medication-dihydrochloride---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["chemotherapy-medication-dihydrochloride---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
