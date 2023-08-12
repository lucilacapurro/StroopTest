# StroopTest

Is a neuropsychological test extensively used to assess the ability to inhibit cognitive interference that occurs when the processing of a specific stimulus feature impedes the simultaneous processing of a second stimulus attribute, known as the Stroop Effect.

Experiment description: 

Subjects are required to read three different tables as fast as possible in 45 seconds. Two of them represent the “congruous condition” in which participants are required to read names of colors (henceforth referred to as color-words) printed in black ink (W) and name different color patches (C). Conversely, in the third table, named color-word (CW) condition, color-words are printed in an inconsistent color ink (for instance the word “red” is printed in green ink). Thus, in this incongruent condition, participants are required to name the color of the ink instead of reading the word.

# Configuration

## Installation guide

1. **Clone the repository.**
    
    ```bash
    git clone https://github.com/lcapurro/StroopTest.git
    cd StroopTest
    ```
  
2. **Create a Python virtual environment.**
    
    ```bash
    python -m venv env
    ```
    
3. **Activate the virtual environment and install the dependencies.**
    1. For MacOS / Linux
        
        ```bash
        ./env/Scripts/activate
        pip install -r requirements.txt
        ```
        
4. **Run the program.**
    1. For the experiments:
        
        ```bash
        python .\MenuPrincipal.py
        ```