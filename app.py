from flask import Flask, render_template, request

def levenshtein(s1, s2):
    #Create the cot matrix to store the results of the subproblems.
    #Dimensions are (len(s1) + 1) x (len(s2) + 1).
    D = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    #Initialization of the first row and first column.
    #The distance from a string to an empty string is its own size (only insertions/deletions).
    for i in range(len(s1) + 1):
        D[i][0] = i
    for j in range(len(s2) + 1):
        D[0][j] = j

    #Fill the rest of the matrix
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            #Cost of substitution (0 if the characters are equal, 1 if different)
            cost = 0 if s1[i -1] == s2[j - 1] else 1

            #The distance dp[i][j] is the minimum between three possible operations:
            #1. Deletion: dp[i-1][j] + 1
            #2. Insertion: dp[i][j-1] + 1
            #3. Replacement: dp[i-1][j-1] + cost
            D[i][j] = min(D[i - 1][j] + 1,          #Deletion
                          D[i][j -1] + 1,           #Insertion
                          D[i - 1][j - 1] + cost)   #Replacement

    #The final result is in the lower right corner of the matrix
    return D[len(s1)][len(s2)]

def correct_word(word, vocab):
    word = word.lower()
    if word in vocab:
        return [word]
    
    suggestions = []
    min_distance = float('inf')
    for vocab_word in vocab:
        distance = levenshtein(word, vocab_word)
        if distance < min_distance:
            min_distance = distance
            suggestions = [vocab_word]
        elif distance == min_distance:
            suggestions.append(vocab_word)

    if min_distance > 3:
        return []
    else:
        return suggestions
    
def load_vocab(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return {line.strip().lower() for line in file}
    
app = Flask(__name__)
VOCAB = load_vocab('dict.txt')

@app.route('/', methods=['GET', 'POST'])
def index():
    original_word = ""
    result = None

    if request.method == 'POST':
        original_word = request.form['word']
        if original_word:
            result = correct_word(original_word, VOCAB)

    return render_template('index.html', result=result, original_word=original_word)

if __name__ == '__main__':
    app.run(debug=True)