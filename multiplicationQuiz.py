# Asks user 10 questions on multiplication and verifies answers.abs

import pyinputplus as pyip
import time, random

numberOfQuestions = 10 # set number of questions in a single game
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    # Pick two random numbers:0
    
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = '%s: %s x %s = ' % (questionNumber, num1, num2)

    try:
        # Right answers are handled by allowRegexes.
        # Wrong asnwers are handled by blockRegexes.
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                                blockRegexes=[('.*', 'Incorrect!')],
                                timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correctAnswers += 1
    
    time.sleep(1) # Brief pause to let user see the result.and

print('Score: %s / %s' % (correctAnswers, numberOfQuestions))