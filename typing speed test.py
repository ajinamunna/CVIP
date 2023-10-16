#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import time

def generate_random_text():
    # List of words for typing practice
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

    # Generate a random sentence with 10 words
    sentence = " ".join(random.sample(words, 10))
    
    return sentence

def typing_speed_test():
    # Generate a random sentence
    sentence = generate_random_text()
    
    print("Type the following text:")
    print(sentence)
    
    input("Press Enter to start...")
    
    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()
    
    # Calculate typing speed
    time_elapsed = end_time - start_time
    words_typed = len(user_input.split())
    typing_speed = words_typed / (time_elapsed / 60)
    
    print(f"Typing speed: {typing_speed:.2f} WPM")
    
    # Calculate accuracy
    correct_words = sum(1 for a, b in zip(sentence.split(), user_input.split()) if a == b)
    accuracy = (correct_words / len(sentence.split())) * 100
    
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    while True:
        typing_speed_test()
        another_test = input("Do you want to test again? (yes/no): ")
        if another_test.lower() != "yes":
            break


# In[ ]:




