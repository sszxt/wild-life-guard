## Getting Started
Follow theses steps to set up the environment and run the application.
1. Fork the repository

2. Clone the forked repository.

3. Create a python virtual environment.
    ``` bash
    python3 -m venv venv
    ```

4. Activate the virtual environment.

    
    - On Windows
    ``` bash
    venv\Scripts\activate
    ```

    - On Linux and macOS
    ``` bash
    source venv/bin/activate
    ```

5. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```
6. Run the application.
    ```python
    streamlit run './scripts/final.py'
    ```
