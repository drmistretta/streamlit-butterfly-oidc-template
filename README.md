# streamlit-butterfly-oidc-template
Streamlit starter with Google OIDC + accessibility + tabs
Perfect — thank you.
Below is a **ready-to-paste `README.md`** customized **exactly** for your template repository:

👉 **[https://github.com/drmistretta/streamlit-butterfly-oidc-template](https://github.com/drmistretta/streamlit-butterfly-oidc-template)**

You can copy **everything below** and paste it directly into your repo’s `README.md`.

---

# 🦋 Streamlit Butterfly App — Google OIDC Starter (Template)

**Instructor:** Dr. Mistretta
**Course Context:** Master’s-level educators learning to *vibe code* and deploy responsive Streamlit applications using GitHub and Streamlit Community Cloud.

This repository is a **GitHub Template Repository**.
Students should **not fork** it — they should use **“Use this template”** to create their own independent Streamlit app.

---

## 🎯 What this starter app demonstrates

* A **clean, responsive Streamlit UI** that works on:

  * mobile phones
  * tablets
  * laptops
  * desktop computers
* **Google OpenID Connect (OIDC)** login using:

  * `st.login()`
  * `st.logout()`
  * `st.user` (captures name + email)
* A **tab-based layout**:

  * Login
  * Butterfly Prediction (demo logic)
* **Accessibility-forward design**, including:

  * adjustable text size
  * high-contrast mode
  * dyslexia-friendly font option
  * reduced-motion support
* A professional **starter-template workflow** used in industry

---

## 🚀 Student Instructions (Start Here)

### Step 1 — Create your own repository from this template

1. Go to:
   👉 [https://github.com/drmistretta/streamlit-butterfly-oidc-template](https://github.com/drmistretta/streamlit-butterfly-oidc-template)
2. Click the green **Use this template** button.
3. Choose **Create a new repository**.
4. Name your repository (example):

   ```
   lastname-butterfly-app
   ```
5. Click **Create repository from template**.

> ✅ You now have your **own repo** with no shared history.

---

### Step 2 — Deploy your app on Streamlit Community Cloud

You must deploy **before** configuring Google login so you know your app’s URL.

1. Go to **Streamlit Community Cloud**.
2. Click **Deploy app**.
3. Select:

   * **Repository:** your new repo
   * **Branch:** `main`
   * **Main file path:** `app.py`
4. Click **Deploy**.

After deployment, copy your app URL. It will look like:

```
https://your-app-name.streamlit.app
```

---

## 🔐 Google Login (OIDC) Setup — Required

Each student must complete these steps **individually** because each deployed app has a unique URL.

### Step 3 — Create Google OAuth credentials

In **Google Cloud Console**:

1. Create or select a project.
2. Configure the **OAuth consent screen** (basic setup is sufficient).
3. Create an **OAuth Client ID**:

   * Application type: **Web application**
4. Add this **Authorized redirect URI**
   (must match exactly):

```
https://your-app-name.streamlit.app/oauth2callback
```

5. Copy:

   * **Client ID**
   * **Client Secret**

---

### Step 4 — Add secrets to Streamlit (do NOT commit these)

1. Open your deployed app in Streamlit Community Cloud.
2. Go to **Settings → Secrets**.
3. Paste the following (replace values):

```toml
[auth]
redirect_uri = "https://your-app-name.streamlit.app/oauth2callback"
cookie_secret = "generate-a-long-random-string"
client_id = "YOUR_GOOGLE_CLIENT_ID"
client_secret = "YOUR_GOOGLE_CLIENT_SECRET"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"
```

4. Click **Save**.
5. Wait for the app to restart.

---

### Step 5 — Test your app

1. Open your app URL.
2. Go to the **Login** tab.
3. Click **Log in with Google**.
4. Confirm:

   * Your name appears
   * Your email address appears
5. Navigate to the **Butterfly Prediction** tab.

🎉 Your app is now live, public, and authenticated.

---

## 🧠 How this app is designed (for learning)

* The app is **public**, but identity is only available after login.
* Google OIDC provides **authentication** (who you are).
* Any **authorization rules** (who can see what) are enforced by *your code*.
* The prediction logic is intentionally simple and designed to be replaced.

---

## 📁 Repository contents

```
app.py                  # Main Streamlit app
requirements.txt        # Includes streamlit[auth]
.gitignore              # Protects secrets
README.md               # This file
.streamlit/config.toml  # (optional) theme defaults
```

---

## ⚠️ Common Issues & Fixes

### ❌ “redirect_uri_mismatch” error

* Your Google OAuth redirect URI does **not exactly match**:

  ```
  https://your-app-name.streamlit.app/oauth2callback
  ```
* Fix it in **Google Cloud Console**, then redeploy.

### ❌ Login button does nothing

* Check **Settings → Secrets** in Streamlit.
* Confirm:

  * `client_id` is present
  * `client_secret` is present
  * `cookie_secret` is present

### ❌ App works locally but not deployed

* Confirm `requirements.txt` includes:

  ```
  streamlit[auth]
  ```
* Do **not** rely on runtime installs.

---

## 📚 Instructor Notes (not for students)

* This repository is intentionally minimal.
* Students are expected to:

  * modify the UI
  * add accessibility features
  * replace demo prediction logic
  * iterate using vibe coding
* This mirrors professional workflows using **starter templates**.

---

## ✅ License

In this application, we will not add a license.


