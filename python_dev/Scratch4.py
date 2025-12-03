    if letter == "L":
        #if remainder >= start_point:
        #    zero_count += 1
        
        new_pos = (start_point - number) % 100
        #passes = (number + (100 - prev_num)) // 100
        if number >= start_point + 1:
            zero_passed += (number - start_point) // 100 + 1
        else:
            zero_passed += (start_point - new_pos) // 100     
        
            
    elif letter == "R":
        
        new_pos = (start_point + number) % 100
        #new_total = (start_point + number) % 100
        #passes = (prev_num + number) // 100
        if number >= (100 - start_point) % 100:
            zero_passed += (number - (100 - start_point)) // 100 + 1
        else:
            zero_passed += (new_pos - start_point) // 100

    start_point = new_pos
 

    result.append(start_point)
        
        
    #print(result)

for n in result:
        if n == 0:
            zero_count += 1     