import numpy as np

def calculate_prediction_accuracy(data, threshold):
    correct = 0
    for entry in data:
        performance = entry['module1_correct'] / entry['module1_total']
        predicted = 'hard' if performance >= threshold else 'easy'
        if predicted == entry['module2_difficulty_received']:
            correct += 1
    return correct / len(data)

def find_optimal_threshold(data):
    best_threshold = 0.5
    best_accuracy = 0
    for threshold in np.arange(0.3, 0.8, 0.05):
        acc = calculate_prediction_accuracy(data, threshold)
        if acc > best_accuracy:
            best_accuracy = acc
            best_threshold = threshold
    return best_threshold
