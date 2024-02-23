
from Account import Account

def main():
        # Khởi tạo 2 tài khoản
        account1 = Account(123456, 0.0)
        account2 = Account(789012, 0.0)

        # Ghi có 100 USD vào tài khoản 1
        account1.credit(100.0)
        account2.credit(200.0)
        # Ghi nợ 50 USD vào tài khoản 2
        account2.debit(50.0)

        # Chuyển 70 USD từ tài khoản 1 vào tài khoản 2
        account1.transferTo(account2, 70.0)

        # Xuất thông tin 2 tài khoản
        print(account1)
        print(account2)
if __name__ == "__main__":
    main()

    
