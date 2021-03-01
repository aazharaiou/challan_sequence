import os
import csv
import datetime

year = '21'
semester = '1'
semesterTitle = 'A21'
issue_date = '2021-03-01'
na = 'Please Fill'

def generate():
    with open(os.getcwd() + os.path.sep + 'output' + os.path.sep + "challans_" + str(int(datetime.datetime.timestamp(datetime.datetime.now()))) + '.csv' , 'w') as outpt:
        out_csv = csv.DictWriter(outpt, fieldnames=['challan_number', 'semester','issue_date','name','fathername','cnic','programme','courses','roll_number','registration_number','contact_number','due_date','amount_within_due_date','validity_date','amount_after_due_date','origin','origin_id'])
        out_csv.writeheader()
        with open(os.getcwd() + os.path.sep + 'input' + os.path.sep + "list.csv") as inpt:
            inp_csv = csv.DictReader(inpt)
            for line in inp_csv:
                c_list = [x for x in range(int(line['From']),int(line['To'])+1)]
                zc_list = [str(x).zfill(6) for x in c_list]
                for c in zc_list:
                    out_csv.writerow({'programme':line['LevelProgram'],'challan_number':year + semester + line['LevelProgram'] + c, 'semester':semesterTitle,'issue_date':issue_date,'name':na,'fathername':na,'cnic':na,'courses':na,'roll_number':na,'registration_number':na,'contact_number':na,'due_date':line['DueDate'],'amount_within_due_date':line['AmountWithinDueDate'] +'00','validity_date':line['ValidityDate'],'amount_after_due_date':line['AmountAfterDueDate'] +'00','origin':'Prospectus','origin_id':line['LevelProgram']+c})

if __name__ == '__main__':
    generate()