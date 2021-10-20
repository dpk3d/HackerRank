"""
Two signals are generated as part of a simulation. A program monitors the signal.
Whenever two signals become equal, then frequency is noted. A record is maintained for maximum
simultaneous frequency seen so far. Each time a higher simultaneous frequency is noted this variable
maxequal is updated to higher frequency.

Note:
     Both signals start at t=0 , but their duration might be different. In this case the comparision of
     equality is performed only until the end of shorter signal.

     If both signals has equal frequency at given time, but the frequency is less than or equal to the
     current maximum frequency, maxequal is not updated

The Running time of both signals are given, denoted by n and m respectively. During the course of
simulation how many times is the maxequal variable is updated.

Complete the updated times function.

"""


def updatedTimes(signalOne, signalTwo):
    updates = 0
    maxFrequency = 0
    lengthSingal1 = len(signalOne)
    lengthSingal2 = len(signalTwo)
    frequencyTaken = min(lengthSingal1, lengthSingal2) - 1
    if frequencyTaken > 0:
        newSignal1 = signalOne[:frequencyTaken]
        newSignal2 = signalTwo[:frequencyTaken]
        for one, two in zip(newSignal1, newSignal2):
            if one == two:
                if maxFrequency < one:
                    updates = updates + 1
                    maxFrequency = one

        return updates
    else:
        return 0


signal1 = [1, 2, 3, 3, 3, 5, 4]
signal2 = [1, 2, 3, 4, 3, 5, 4]

print("Number of times maxequal variable updates is :", updatedTimes(signal1, signal2))
# Number of times maxequal variable updates is : 4
