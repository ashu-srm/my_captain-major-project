import csv
def write_into_csv(take_list):
    with open('cart_data.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        arr=["Name of product","Quantity","Serial_no","Price_in_Rs"]
        if(csv_file.tell()==0):
          writer.writerow(arr)

        writer.writerow(take_list)
class e_commerce:
    def take_data():
        flag=True
        Product_num=1
        while (flag):
          cart_data=input("please enter info for produt#{} following order:Name of product Quantity Serial_no Price_in_Rs:-".format(Product_num))
          cart_data_list=cart_data.split(" ")
          print("\nThe entered information is:-\nName of product:{}\nQuantity:{}\nSerial_no:{}\nPrice_in_Rs:{}".format(cart_data_list[0],cart_data_list[1],cart_data_list[2],cart_data_list[3]))
          choice_option=input("Is the data corect:yes/no:-")
          if(choice_option=="yes"):
               write_into_csv(cart_data_list)
               cond_check=input("write yes for more input else write no:")
               if(cond_check=="yes"):
                 Product_num=Product_num+1
                 flag=True
               elif(cond_check=="no"):
                 flag=False
          elif(choice_option=="no"):
             print("re-enter data")
    take_data()
