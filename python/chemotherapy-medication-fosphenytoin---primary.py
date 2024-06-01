# Lai A., 2024.

import sys, csv, re

codes = [{"code":"24637","system":"prod"},{"code":"380","system":"prod"},{"code":"14857","system":"prod"},{"code":"34699","system":"prod"},{"code":"5587","system":"prod"},{"code":"34144","system":"prod"},{"code":"2782","system":"prod"},{"code":"4490","system":"prod"},{"code":"6594","system":"prod"},{"code":"6504","system":"prod"},{"code":"6624","system":"prod"},{"code":"9678","system":"prod"},{"code":"107","system":"prod"},{"code":"3068","system":"prod"},{"code":"27113","system":"prod"},{"code":"2128","system":"prod"},{"code":"1370","system":"prod"},{"code":"25903","system":"prod"},{"code":"34592","system":"prod"},{"code":"2062","system":"prod"},{"code":"04070300/04080100","system":"prod"},{"code":"04080100/04080200","system":"prod"},{"code":"02030203/04080100/04080200","system":"prod"},{"code":"04070300/04080100/23000000","system":"prod"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chemotherapy-medication-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["chemotherapy-medication-fosphenytoin---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["chemotherapy-medication-fosphenytoin---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["chemotherapy-medication-fosphenytoin---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
