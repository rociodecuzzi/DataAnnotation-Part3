def decode(message_file):
    # Open the specified text file and read its content
    with open(message_file, 'r') as file:
        lines = file.readlines()

    words = {}

    # Iterate through each line in the file
    for line in lines:
        num, word = line.strip().split(' ')
        num = int(num)
        # Store the word in the dictionary with its corresponding number as the key
        words[num] = word

    # Find the maximum number
    max_num = len(words.keys())

    decoded_message = []

    current_line = 1
    current_id = 1
    
    # Iterate through the pyramid structure until the current ID exceeds the maximum number
    while current_id <= max_num:
        decoded_message.append(words[current_id])
        current_line += 1
        current_id += current_line
  
    # Join the words in the decoded message list with spaces to form the final decoded message
    return ' '.join(decoded_message)

decoded_message = decode("coding_qual_input.txt")
print(decoded_message)
