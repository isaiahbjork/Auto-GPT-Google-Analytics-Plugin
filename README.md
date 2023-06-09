# Auto-GPT Google Analytics Plugin 📊
The AutoGPT Google Analytics Plugin is a software tool that allows you to connect Google Analytics to Auto-GPT.

[![GitHub Repo stars](https://img.shields.io/github/stars/isaiahbjork/Auto-GPT-Google-Analytics-Plugin?style=social)](https://github.com/isaiahbjork/Auto-GPT-Google-Analytics-Plugin/stargazers)



## 💡 Key Features:
- 📊 **Get Website Analytics**
- ⏰ **Get Past/Future Date**

## 🔧 Installation

Follow these steps to configure the Auto-GPT Google Analytics Plugin:

### 1. Clone the Auto-GPT-Google-Analytics-Plugin repository
Clone this repository and navigate to the `Auto-GPT-Google-Analytics-Plugin` folder in your terminal:

```bash
git clone https://github.com/isaiahbjork/Auto-GPT-Google-Analytics-Plugin.git
```

### 2. Install required dependencies
Execute the following command to install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### 3. Package the plugin as a Zip file
Compress the `Auto-GPT-Google-Analytics-Plugin` folder or [download the repository as a zip file](https://github.com/isaiahbjork/Auto-GPT-Google-Analytics-Plugin/archive/refs/heads/master.zip).

### 4. Install Auto-GPT
If you haven't already, clone the [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT) repository, follow its installation instructions, and navigate to the `Auto-GPT` folder.

You might have to run this in the Auto-GPT file if you get an error saying "No Moudle Found".

```bash
pip install gaapi4py
```

### 5. Copy the Zip file into the Auto-GPT Plugin folder
Transfer the zip file from step 3 into the `plugins` subfolder within the `Auto-GPT` repo.

### 6. Locate the `.env.template` file
Find the file named `.env.template` in the main `/Auto-GPT` folder.

### 7. Create and rename a copy of the file
Duplicate the `.env.template` file and rename the copy to `.env` inside the `/Auto-GPT` folder.

### 8. Edit the `.env` file
Open the `.env` file in a text editor. Note: Files starting with a dot might be hidden by your operating system.

### 9. Add Google Analytics configuration settings
Append the following configuration settings to the end of the file:

```ini
################################################################################
### GOOGLE ANALYTICS
################################################################################
GOOGLE_APPLICATION_CREDENTIALS=firebase.json
GOOGLE_ANALYTICS_VIEW_ID=
```
- Go to Google Cloud, enable the Google Analytics Reporting API, credentials > keys > Add Key > Create New Key > JSON, add this to the auto-gpt and rename it firebase.json.
- Add the email address in the JSON to your Google Analytics (Admin -> View Access Management).


### 10. Allowlist Plugin
In your `.env` search for `ALLOWLISTED_PLUGINS` and add this Plugin:

```ini
################################################################################
### ALLOWLISTED PLUGINS
################################################################################
#ALLOWLISTED_PLUGINS - Sets the listed plugins that are allowed (Example: plugin1,plugin2,plugin3)
ALLOWLISTED_PLUGINS=AutoGPTGoogleAnalyticsPlugin
```

## 🧪 Test the Auto-GPT Google Analytics Plugin

Experience the plugin's capabilities by getting your website analytics.

- Use this format for dates YYYY-MM-DD

1. **Configure Auto-GPT:**
   Set up Auto-GPT with the following parameters:
   - Name: `AnalyticsGPT`
   - Role: `Web Analytics Expert`
   - Goals:
     1. Goal 1: `Get pageviews for the past 30 days`
     2. Goal 2: `Terminate`

2. **Run Auto-GPT:**
   Launch Auto-GPT, which should use the Google Analytics plugin.


3. **Sample response:**
<img width="1063" alt="auto-gpt-email-plugin" src="https://i.ibb.co/ScRR4tv/Screen-Shot-2023-04-22-at-4-10-10-PM.png">


