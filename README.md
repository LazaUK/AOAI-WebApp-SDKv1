# Python Flask Web app with Azure OpenAI Integration
This guide walks you through deploying minimalistic Flask application with Azure OpenAI's GPT integration to an Azure Web App.

### 1. Provision GPT model in Azure OpenAI:
- in Azure OpenAI / AI Studio deploy required GPT-x model;
- take a note of Azire OpenAI resource's endpoint, GPT model's deployment name and decide which API version you plan to use.

### 2. Prepare Azure Web App resource:
- in Azure create new Web app and select Python as your target language platform;
- in Web app's **Environment Variable** settings, create _AZURE_OPENAI_API_BASE_, _AZURE_OPENAI_API_DEPLOY_ and _AZURE_OPENAI_API_VERSION_ variables and set them to values collected from Step # 1 above;
- in Web app's **Environment Variable** settings, create _SCM_DO_BUILD_DURING_DEPLOYMENT_ variable and set its value to "**true**";
> Note: SCM_DO_BUILD_DURING_DEPLOYMENT setting will ensure that Web app downloads required Python packages, listed in the provided _**requirements.txt**_ file.
- if setup correctly, your Web app settings should look like this:
![step2_env_var](images/env_var.png)
