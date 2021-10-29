python main.py --algo backtrack --layout easy_classroom
python main.py --algo backtrack --layout fail_classroom

python main.py --algo backtrack --layout easy_sudoku
python main.py --algo backtrack --layout harder_sudoku
python main.py --algo backtrack+fc --layout easy_sudoku
python main.py --algo backtrack+ac3 --layout easy_sudoku
python main.py --algo backtrack+fc --layout harder_sudoku
python main.py --algo backtrack+ac3 --layout harder_sudoku

python main.py --algo hill_climbing --layout 8_nqueens
python main.py --algo hill_climbing --layout easy_sudoku
@REM %0