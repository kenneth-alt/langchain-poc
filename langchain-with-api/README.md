## How to run the POC implemetation locally

1. Clone the repo and cd into the server directory 
   
2. Create a python virtual environment 
    python -m venv myenv

3. Activate the virtual environment
    source ./myenv/Scripts/activate

4. Install python dependencies using the requirements.txt
    pip install -r requirements.txt

5. Create apkikey,py file and store your openai api key in it
    echo 'apikey="your-openai-api-key"' > apikey.py

6. Run your fast api server
    uvicorn server:app --reload

7. cd into the client and run index.html page using LiveServer or any similar method.
