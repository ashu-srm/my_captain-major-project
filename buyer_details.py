import csv
def write_into_csv(take_list):
    with open('buyer_data.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        arr=["Name","Password","Contact number","Email_Id"]
        if(csv_file.tell()==0):
          writer.writerow(arr)

        writer.writerow(take_list)
class e_commerce:
    def take_data():
        flag=True
        buyer_num=1
        while (flag):
          buyer_data=input("please enter info for buyer#{} following order:Name Password Contact_no email_ID:-".format(buyer_num))
          buyer_data_list=buyer_data.split(" ")
          print("\nThe entered information is:-\nName:{}\nPassword:{}\nContact number:{}\nEmail id:{}".format(buyer_data_list[0],buyer_data_list[1],buyer_data_list[2],buyer_data_list[3]))
          choice_option=input("Is the data corect:yes/no:-")
          if(choice_option=="yes"):
               write_into_csv(buyer_data_list)
               cond_check=input("write yes for more input else write no:")
               if(cond_check=="yes"):
                 buyer_num=buyer_num+1
                 flag=True
               elif(cond_check=="no"):
                 flag=False
          elif(choice_option=="no"):
             print("re-enter data")
    take_data()
