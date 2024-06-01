# Lai A., 2024.

import sys, csv, re

codes = [{"code":"34727","system":"prod"},{"code":"22047","system":"prod"},{"code":"303","system":"prod"},{"code":"21809","system":"prod"},{"code":"35154","system":"prod"},{"code":"3703","system":"prod"},{"code":"606","system":"prod"},{"code":"10308","system":"prod"},{"code":"4125","system":"prod"},{"code":"8286","system":"prod"},{"code":"10318","system":"prod"},{"code":"41579","system":"prod"},{"code":"35349","system":"prod"},{"code":"15988","system":"prod"},{"code":"27290","system":"prod"},{"code":"27413","system":"prod"},{"code":"33131","system":"prod"},{"code":"20157","system":"prod"},{"code":"41502","system":"prod"},{"code":"38999","system":"prod"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chemotherapy-medication-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["chemotherapy-medication-180mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["chemotherapy-medication-180mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["chemotherapy-medication-180mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)