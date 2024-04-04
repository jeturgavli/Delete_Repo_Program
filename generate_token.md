# How to Generate Personal Access Token for GitHub

Follow these steps to generate a Personal Access Token (PAT) for use with GitHub:

1. **Sign in to GitHub:**
   Go to [GitHub](https://github.com/) and sign in to your account if you haven't already.

2. **Access Personal Access Tokens:**
   - Click on your profile icon at the top-right corner of the page.
   - From the dropdown menu, select "Settings".

3. **Navigate to Developer Settings:**
   In the left sidebar of the Settings page, locate and click on "Developer settings".

4. **Generate New Token:**
   - In the Developer settings page, click on "Personal access tokens".
   - Click on the "Generate new token" button.

5. **Configure Token Settings:**
   - Give your token a descriptive name that reflects its purpose.
   - Choose the scopes or permissions for the token:
     - `repo`: Grants full control of private repositories. Required for accessing repositories.
     - `delete_repo`: Grants permission to delete repositories. Required if you intend to use the delete repository feature in your script.
   
     Note: Be cautious with the permissions you grant to your token. Grant only the permissions necessary for your intended use to minimize security risks.

6. **Generate Token:**
   After configuring the settings, click on the "Generate token" button.

7. **Copy Token:**
   Once the token is generated, GitHub will display it. Copy the token to your clipboard.

8. **Store Token Securely:**
   - Treat your token like a password and store it securely. Do not share it publicly or embed it directly in your scripts.
   - For your script, create a separate file (e.g., `critical_info.py`) to store the token securely. Ensure that this file is not included in your version control system (e.g., Git) to prevent accidental exposure.
   - You can reference the token in your script by importing it from the file where it's stored.

9. **Test Token:**
   Before using the token in your script, you can test it by making a simple API request using a tool like cURL or Postman to ensure that it's functioning correctly.

10. **Update Token if Necessary:**
    If you suspect that your token has been compromised or if you no longer need it, you can revoke it and generate a new one following the same process.

11. **Using the Token in the Script:**
    In your script (`delete_repo_program.py`), replace the placeholder `<access_token>` with the generated token.
   
12. **Select Repositories to Delete:**
    - Run the `delete_repo_program.py` script using Python.
    - The script will list all repositories associated with your GitHub account.
    - Enter the numbers corresponding to the repositories you want to delete, separated by spaces.

By following these steps, you can generate a Personal Access Token for use with GitHub and ensure that it's securely managed for your script or application. Remember to handle tokens with care to maintain the security of your GitHub account and repositories.
