def bankingApp
    myBalance = 0
    puts "Welcome to the banking app"
    puts "Insert the password please: (anything will work)"
    myPass = gets.chomp
    while true do
        puts "What would you like to do? (option: balance/deposit/withdraw/finish)"
        input = gets.chomp
        if input == "balance"
            puts "Your balance is $" + myBalance.to_s
            myBalance += myBalance
        elsif input == "deposit"
            puts "How much would you like to deposit?"
            myDeposit = gets.chomp
            myDeposit = myDeposit.to_i
            myBalance += myDeposit
            puts"Your balance is $" + myBalance.to_s
        elsif input == "withdraw"
            puts "How much would you like to withdraw?"
            myWith = gets.chomp
            myWith = myWith.to_i
            myBalance -= myWith
            if myBalance <= 0
                puts "You cannot withdraw this amount"
                myBalance += myWith
            else
                puts "Your balance is $" + myBalance.to_s
            end
        elsif input == "finish"
            puts "Goodbye"
            break 
        else
            puts "Invalid selection!"
        end
    end
end

bankingApp