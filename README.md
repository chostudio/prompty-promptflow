DO THESE COMMANDS THEN RUN IT AND IT WORKS:

source .venv/bin/activate
pip3 install python-dotenv==1.0.1



Install the VSCode Prompty Extension so the .prompty file works
Not sure if you also need to install the PromptFlow extension too but we'll see.

(for somereadon don't need to run this command for promptflow to work?)
pip install promptflow

pf flow test --flow flow:chat --inputs question="What's the capital of France?"

Top part of the .prompty file is in YAML. After that is the prompt template which is in Jinja format.


follow this one:
https://github.com/Azure-Samples/rag-data-openai-python-promptflow/tree/main


maybe these idk
# Test prompty with default inputs
pf flow test --flow path/to/prompty.prompty

# Test prompty with specified inputs
pf flow test --flow path/to/prompty.prompty --inputs first_name=John last_name=Doh question="What is the capital of France?"

# Test prompty with sample file
pf flow test --flow path/to/prompty.prompty --inputs path/to/sample.json