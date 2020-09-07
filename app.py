import train
import predict

print("Choose an option:")
print('1 - Train and Run')
print('2 - Train')
print('3 - Run')

selected = int(input())

if selected == 1:
    train.execute()
    predict.execute()
elif selected == 2:
    train.execute()
elif selected == 3:
    predict.execute()

print('Program closed')
