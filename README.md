# Python Flask Web app with Azure OpenAI Integration
This guide walks you through deploying minimalistic Flask application with Azure OpenAI's GPT integration to an Azure Web App.

### Step 1. Provision GPT model in Azure OpenAI:
- in Azure OpenAI / AI Studio deploy required GPT-x model;
- take a note of Azire OpenAI resource's endpoint, GPT model's deployment name and decide which API version you plan to use.

### Step 2. Prepare Azure Web App resource:
- in Azure create new Web app and select Python as your target language platform;
- in Web app's **Environment Variables** settings, create _AZURE_OPENAI_API_BASE_, _AZURE_OPENAI_API_DEPLOY_ and _AZURE_OPENAI_API_VERSION_ variables and set them to values collected from Step # 1 above;
- in Web app's **Environment Variables** settings, create _SCM_DO_BUILD_DURING_DEPLOYMENT_ variable and set its value to "**true**";
> Note: SCM_DO_BUILD_DURING_DEPLOYMENT setting will ensure that Web app downloads required Python packages, listed in the provided _**requirements.txt**_ file.
- if setup correctly, your Web app settings should look like this:
![step2_env_var](images/env_var.png)

### Step 3. Configure Authentication:
- in Web app's **Identity** settings, set the status of system-assigned managed identity _ON_.
> Note: this demo shows how to authenticate with managed identity. You may implementation detals of other potential options [here](managed_identity.png).
![step3_managed_identity](images/managed_identity.png)
- in Azure OpenAI's **Access Control (IAM)** settings, assign Web app's managed identity _Cognitive Services OpenAI User_ role.

### Step 4. Deploy Flask Web App:
- ZIP provided _app.py_, _requirements.txt_ and content of _static_ and _templates_ folders (4 files in total);
- Deploy your ZIP file with the following Azure CLI command, and ensure that you use the right Resource Group, Web App and ZIP file names:
``` BASH
az webapp deploy --resource-group <Web_App_RG> --name <Web_App_Name> --src-path <Source_ZIP_file>
```
- As we enabled "build during deployment" in Step 2 above, we can verify from the Web app log that it pulled required Python packages into target Python virtual environment:
![step4_app_log](images/app_log.png)

### Step 5. Web App UI:
- The home page of the Flask web app is super-minimalistic. You type your question, click **Ask** button and Web app adds new pair of question/answers to its Web page:
![step5_app_ui](images/app_ui.png)
