
user1_count = 0
user2_count = 0
number_of_games = int(input('Number of plays: '))
for i in range(number_of_games):
    user1 = input()
    user2 = input()
    if user1 == user2:
        print('Tie')
    elif user1 == 'Scissors' and user2 == 'Rock':
        user1_count += 1
        print('User2 Win',user2_count)
        print('Rock win')
    elif user2 == 'Scissors' and user1 == 'Rock':
        print('User1 Win',user1_count )
        user2_count += 1
        print('Rock win')
    elif user1 == 'Paper' and user2 == 'Rock':
        user1_count += 1
        print('User1 Win',user1_count )
        print('Paper win')
    elif user2 == 'Paper' and user1 == 'Rock':
        user2_count += 1
        print('User2 Win',user2_count)
        print('Paper win')
    elif user1 == 'Scissors' and user2 == 'Paper':
        user1_count += 1
        print('User1 Win',user1_count )
        print('Scissors Win')
    elif user2 == 'Scissors' and user1 == 'Paper':
        print('User2 Win',user2_count)
        user2_count += 1
        print('Scissors Win')
		
print(user1_count)
print(user2_count)