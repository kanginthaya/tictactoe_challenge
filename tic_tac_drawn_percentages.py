import numpy as np

i1, i2 = (np.arange(9).tolist() for i in range(2)) # Initialize lists from 1 to 9

# Initialize tic-tac-toe board
X = ['', '', '',
     '', '', '',
     '', '', '']

## Optionally visualize the entries
# print(X[0],'|',X[1],'|',X[2])
# print('----------')
# print(X[3],'|',X[4],'|',X[5])
# print('----------')
# print(X[6],'|',X[7],'|',X[8],'\n')

def check_gameover(X):
    '''Check if game is over.
    '''
    
    # Check for X's     
    game_over = False
    
    if ((X[0] == 'X') and (X[1] == 'X') and (X[2] == 'X')):
        game_over = True
        return game_over
    
    if ((X[3] == 'X') and (X[4] == 'X') and (X[5] == 'X')):
        game_over = True
        return game_over
    
    if ((X[6] == 'X') and (X[7] == 'X') and (X[8] == 'X')):
        game_over = True
        return game_over    

    if ((X[0] == 'X') and (X[3] == 'X') and (X[6] == 'X')):
        game_over = True
        return game_over
    
    if ((X[1] == 'X') and (X[4] == 'X') and (X[7] == 'X')):
        game_over = True
        return game_over    
    
    if ((X[2] == 'X') and (X[5] == 'X') and (X[8] == 'X')):
        game_over = True
        return game_over   
    
    if ((X[0] == 'X') and (X[4] == 'X') and (X[8] == 'X')):
        game_over = True
        return game_over
    
    if ((X[2] == 'X') and (X[4] == 'X') and (X[6] == 'X')):
        game_over = True
        return game_over
    
    # Check for O's
    if ((X[0] == 'O') and (X[1] == 'O') and (X[2] == 'O')):
        game_over = True
        return game_over
    
    if ((X[3] == 'O') and (X[4] == 'O') and (X[5] == 'O')):
        game_over = True
        return game_over
    
    if ((X[6] == 'O') and (X[7] == 'O') and (X[8] == 'O')):
        game_over = True
        return game_over    

    if ((X[0] == 'O') and (X[3] == 'O') and (X[6] == 'O')):
        game_over = True
        return game_over
    
    if ((X[1] == 'O') and (X[4] == 'O') and (X[7] == 'O')):
        game_over = True
        return game_over    
    
    if ((X[2] == 'O') and (X[5] == 'O') and (X[8] == 'O')):
        game_over = True
        return game_over    
    
    if ((X[0] == 'O') and (X[4] == 'O') and (X[8] == 'O')):
        game_over = True
        return game_over
    
    if ((X[2] == 'O') and (X[4] == 'O') and (X[6] == 'O')):
        game_over = True
        return game_over
    
    return game_over

## Test case for check_gameover()
# gameover = check_gameover(X)
# print(gameover)
# result = 'Decisive' if gameover is True else 'Draw'
# print(result)
    
total_runs = 0 # Initialize total game runs
total_wins = 0 # Initialize total number of games ending in a win
    
for item1 in i1:
    
    X[item1] = 'X'
    i22 = i2.copy()
    i22.remove(item1)
    
    for item2 in i22:
        X[item2] = 'O'
        i33 = i22.copy()
        i33.remove(item2)
        
        for item3 in i33:
            X[item3] = 'X'
            i44 = i33.copy()
            i44.remove(item3)
            
            for item4 in i44:
                X[item4] = 'O'
                i55 = i44.copy()
                i55.remove(item4)
                
                for item5 in i55:
                    X[item5] = 'X'
                    
                    if (check_gameover(X) == True): # No need to check for wins until the 5th step
                        total_runs = total_runs + 1
                        total_wins = total_wins + 1
                        X[item5] = ''
                        continue
                    
                    i66 = i55.copy()
                    i66.remove(item5)
                    
                    for item6 in i66:
                        X[item6] = 'O'
                        
                        if (check_gameover(X) == True):
                            total_runs = total_runs + 1
                            total_wins = total_wins + 1
                            X[item6] = ''
                            continue
                        
                        i77 = i66.copy()
                        i77.remove(item6)
                        
                        for item7 in i77:
                            X[item7] = 'X'
                            
                            if (check_gameover(X) == True):
                                total_runs = total_runs + 1
                                total_wins = total_wins + 1
                                X[item7] = ''
                                continue
                            
                            i88 = i77.copy()
                            i88.remove(item7)
                            
                            for item8 in i88:
                                X[item8] = 'O'
                                
                                if (check_gameover(X) == True):
                                    total_runs = total_runs + 1
                                    total_wins = total_wins + 1
                                    X[item8] = ''
                                    continue
                                
                                i99 = i88.copy()
                                i99.remove(item8)
                                
                                for item9 in i99:
                                    X[item9] = 'X'
                                    
                                    if (check_gameover(X) == True):
                                        total_runs = total_runs + 1
                                        total_wins = total_wins + 1
                                        X[item9] = ''
                                        
                                    else: 
                                        total_runs = total_runs + 1
                                        X[item9] = ''
                                
                                X[item8] = ''
                            
                            X[item7] = ''
                            
                        X[item6] = ''
                        
                    X[item5] = ''
                    
                X[item4] = ''
                
            X[item3] = ''
            
        X[item2] = ''
        
    X[item1] = ''

print('Total number of possible games: {}'.format(total_runs))
print('Total number of wins: {}'.format(total_wins))
print('Percentage of drawn games = {:.3f}%'.format(((total_runs-total_wins)/total_runs)*100))

                        
        
    
    
