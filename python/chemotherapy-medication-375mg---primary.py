# Lai A., 2024.

import sys, csv, re

codes = [{"code":"13271","system":"prod"},{"code":"35865","system":"prod"},{"code":"3281","system":"prod"},{"code":"13972","system":"prod"},{"code":"31532","system":"prod"},{"code":"1063","system":"prod"},{"code":"8545","system":"prod"},{"code":"33990","system":"prod"},{"code":"22609","system":"prod"},{"code":"6523","system":"prod"},{"code":"691","system":"prod"},{"code":"33691","system":"prod"},{"code":"512","system":"prod"},{"code":"15016","system":"prod"},{"code":"1316","system":"prod"},{"code":"23270","system":"prod"},{"code":"14717","system":"prod"},{"code":"34903","system":"prod"},{"code":"23034","system":"prod"},{"code":"32876","system":"prod"},{"code":"2949","system":"prod"},{"code":"21125","system":"prod"},{"code":"40379","system":"prod"},{"code":"5653","system":"prod"},{"code":"29333","system":"prod"},{"code":"21964","system":"prod"},{"code":"13607","system":"prod"},{"code":"34344","system":"prod"},{"code":"34109","system":"prod"},{"code":"35402","system":"prod"},{"code":"32051","system":"prod"},{"code":"6412","system":"prod"},{"code":"13338","system":"prod"},{"code":"7992","system":"prod"},{"code":"227","system":"prod"},{"code":"30932","system":"prod"},{"code":"14789","system":"prod"},{"code":"1434","system":"prod"},{"code":"41515","system":"prod"},{"code":"34781","system":"prod"},{"code":"7436","system":"prod"},{"code":"34393","system":"prod"},{"code":"5089","system":"prod"},{"code":"33123","system":"prod"},{"code":"38989","system":"prod"},{"code":"4303","system":"prod"},{"code":"20703","system":"prod"},{"code":"21417","system":"prod"},{"code":"25926","system":"prod"},{"code":"32551","system":"prod"},{"code":"27922","system":"prod"},{"code":"9528","system":"prod"},{"code":"18132","system":"prod"},{"code":"34083","system":"prod"},{"code":"38540","system":"prod"},{"code":"26315","system":"prod"},{"code":"18024","system":"prod"},{"code":"1245","system":"prod"},{"code":"34272","system":"prod"},{"code":"17087","system":"prod"},{"code":"85","system":"prod"},{"code":"7548","system":"prod"},{"code":"41663","system":"prod"},{"code":"16425","system":"prod"},{"code":"38262","system":"prod"},{"code":"22660","system":"prod"},{"code":"32835","system":"prod"},{"code":"955","system":"prod"},{"code":"33988","system":"prod"},{"code":"19141","system":"prod"},{"code":"9590","system":"prod"},{"code":"21833","system":"prod"},{"code":"44","system":"prod"},{"code":"32064","system":"prod"},{"code":"2621","system":"prod"},{"code":"5298","system":"prod"},{"code":"38919","system":"prod"},{"code":"31984","system":"prod"},{"code":"228","system":"prod"},{"code":"10574","system":"prod"},{"code":"33803","system":"prod"},{"code":"32803","system":"prod"},{"code":"16570","system":"prod"},{"code":"40659","system":"prod"},{"code":"14344","system":"prod"},{"code":"3738","system":"prod"},{"code":"39887","system":"prod"},{"code":"4234","system":"prod"},{"code":"32772","system":"prod"},{"code":"28859","system":"prod"},{"code":"95","system":"prod"},{"code":"12150","system":"prod"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chemotherapy-medication-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["chemotherapy-medication-375mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["chemotherapy-medication-375mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["chemotherapy-medication-375mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
